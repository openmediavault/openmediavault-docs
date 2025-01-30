"""Runner of rstcheck_core."""

from __future__ import annotations

import logging
import multiprocessing
import os
import pathlib
import re
import sys
import typing as t

from . import _sphinx, checker, config, types

logger = logging.getLogger(__name__)


class RstcheckMainRunner:
    """Main runner of rstcheck_core."""

    def __init__(
        self,
        check_paths: list[pathlib.Path],
        rstcheck_config: config.RstcheckConfig,
        *,
        overwrite_config: bool = True,
    ) -> None:
        """Initialize the :py:class:`RstcheckMainRunner` with a base config.

        :param check_paths: Files to check.
        :param rstcheck_config: Base configuration config from e.g. the CLI.
        :param overwrite_config: If file config overwrites current config; defaults to True
        """
        self.config = rstcheck_config
        self.overwrite_config = overwrite_config
        if rstcheck_config.config_path:
            self.load_config_file(
                rstcheck_config.config_path,
                warn_unknown_settings=rstcheck_config.warn_unknown_settings or False,
            )

        self.check_paths = check_paths
        self._files_to_check: list[pathlib.Path] = []
        self._nonexisting_paths: list[pathlib.Path] = []
        self.update_file_list()

        pool_size = multiprocessing.cpu_count()
        # NOTE: Work around https://bugs.python.org/issue45077
        self._pool_size = pool_size if sys.platform != "win32" else min(pool_size, 61)

        self.errors: list[types.LintError] = []

    @property
    def files_to_check(self) -> list[pathlib.Path]:
        """List of files to check.

        This list is updated via the :py:meth:`RstcheckMainRunner.update_file_list` method.
        """
        return self._files_to_check

    @property
    def nonexisting_paths(self) -> list[pathlib.Path]:
        """List of paths which do not exist.

        This list is updated via the :py:meth:`RstcheckMainRunner.update_file_list` method.
        """
        return self._nonexisting_paths

    def load_config_file(
        self, config_path: pathlib.Path, *, warn_unknown_settings: bool = False
    ) -> None:
        """Load config from file and merge with current config.

        If the loaded file config overwrites the current config depends on the
        ``self.overwrite_config`` attribute set on initialization.

        :param config_path: Path to config file; can be directory or file
        :param warn_unknown_settings: If a warning should be logged for unknown settings in config
            file;
            defaults to :py:obj:`False`
        """
        logger.info("Load config file for main runner: '%s'.", config_path)
        file_config = config.load_config_file_from_path(
            config_path, warn_unknown_settings=warn_unknown_settings
        )

        if file_config is None:
            logger.warning("Config file was empty or not found.")
            return

        logger.debug(
            "Merging config from file into main config. File config is dominant: %s",
            self.overwrite_config,
        )
        self.config = config.merge_configs(
            self.config, file_config, config_add_is_dominant=self.overwrite_config
        )

    def update_file_list(self) -> None:
        """Update file path list with paths specified on initialization.

        Uses paths from ``RstcheckMainRunner.check_paths``, resolves all file paths and
        saves them in :py:attr:`RstcheckMainRunner.files_to_check`.

        If a given path does not exist, it is filtered out and saved in
        :py:attr:`RstcheckMainRunner.files_to_check`.

        Clear the current file list. Then get the file and directory paths specified with
        ``self.check_paths`` attribute set on initialization and search them for rst files
        to check. Add those files to the file list.
        """
        logger.debug("Updating list of files to check.")
        paths = list(self.check_paths)
        self._files_to_check = []

        if len(paths) == 1 and paths[0].name == "-":
            logger.info("'-' detected. Using stdin for input.'")
            self._files_to_check.append(paths[0])
            return

        paths = self._filter_nonexisting_paths(paths)

        def checkable_rst_file(f: pathlib.Path) -> bool:
            return f.is_file() and not f.name.startswith(".") and f.suffix.casefold() == ".rst"

        while paths:
            path = paths.pop(0)
            resolved_path = path.resolve()
            if self.config.recursive and resolved_path.is_dir():
                for root, directories, children in os.walk(path):
                    root_path = pathlib.Path(root)
                    paths += [
                        root_path / f
                        for f in children
                        if checkable_rst_file((root_path / f).resolve())
                    ]
                    directories[:] = [d for d in directories if not d.startswith(".")]
                continue

            if checkable_rst_file(resolved_path):
                self._files_to_check.append(path)

    def _filter_nonexisting_paths(self, paths: list[pathlib.Path]) -> list[pathlib.Path]:
        """Filter nonexisting paths out.

        If recursive is not active only files are allowed, else directories are also allowed.

        :param paths: List of paths to filter
        :return: Filtered path list
        """
        self._nonexisting_paths = []
        _paths = list(paths)

        for path in _paths:
            resolved_path = path.resolve()

            if resolved_path.is_file():
                continue

            if self.config.recursive and resolved_path.is_dir():
                continue

            _paths.remove(path)
            self._nonexisting_paths.append(path)

            if self.config.recursive:
                logger.warning(
                    "Path does not exist or is neither a file nor a directory: '%s'.",
                    path,
                )
                continue

            logger.warning(
                "Path does not exist or is not a file: '%s'.",
                path,
            )

        return _paths

    def _run_checks_sync(self) -> list[list[types.LintError]]:
        """Check all files from the file list syncronously and return the errors.

        :return: List of lists of errors found per file
        """
        logger.debug("Runnning checks synchronically.")
        with _sphinx.load_sphinx_if_available():
            return [
                checker.check_file(file, self.config, self.overwrite_config)
                for file in self._files_to_check
            ]

    def _run_checks_parallel(self) -> list[list[types.LintError]]:
        """Check all files from the file list in parallel and return the errors.

        :return: List of lists of errors found per file
        """
        logger.debug(
            "Runnning checks in parallel with pool size of %s.",
            self._pool_size,
        )
        with _sphinx.load_sphinx_if_available(), multiprocessing.Pool(self._pool_size) as pool:
            return pool.starmap(
                checker.check_file,
                [(file, self.config, self.overwrite_config) for file in self._files_to_check],
            )

    def _update_results(self, results: list[list[types.LintError]]) -> None:
        """Take results and update error cache.

        Result normally come from :py:meth:`RstcheckMainRunner._run_checks_sync` or
        :py:meth:`RstcheckMainRunner._run_checks_parallel`.
        :param results: List of lists of errors found
        """
        self.errors = []
        for errors in results:
            self.errors += errors

    def check(self) -> None:
        """Check all files in the file list and save the errors.

        Multiple files are run in parallel.

        A new call overwrite the old cached errors.
        """
        logger.info("Run checks for all files.")
        results = (
            self._run_checks_parallel()
            if len(self._files_to_check) > 1
            else self._run_checks_sync()
        )
        self._update_results(results)

    def print_result(self, output_file: t.TextIO | None = None) -> int:
        """Print all cached error messages and return exit code.

        :param output_file: file to print to; defaults to sys.stderr (if ``None``)
        :return: exit code 0 if no error is printed; 1 if any error is printed
        """
        if len(self.errors) == 0 and len(self._nonexisting_paths) == 0:
            print("Success! No issues detected.", file=output_file or sys.stdout)
            return 0

        err_msg_regex = re.compile(r"\([A-Z]+/[0-9]+\)")

        for error in self.errors:
            err_msg = error["message"]
            if not err_msg_regex.match(err_msg):
                err_msg = "(ERROR/3) " + err_msg

            message = f"{error['source_origin']}:{error['line_number']}: {err_msg}"

            print(message, file=output_file or sys.stderr)

        print("Error! Issues detected.", file=output_file or sys.stderr)
        return 1

    def run(self) -> int:  # pragma: no cover
        """Run checks, print error messages and return the result.

        :return: exit code 0 if no error is printed; 1 if any error is printed
        """
        logger.info("Run checks and print results.")
        self.check()
        return self.print_result()
