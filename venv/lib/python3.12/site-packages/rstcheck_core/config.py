"""Rstcheck configuration functionality."""

from __future__ import annotations

import configparser
import contextlib
import enum
import logging
import pathlib
import re
import typing as t

import pydantic

from . import _extras

tomllib_imported = False
try:
    import tomllib

    tomllib_imported = True
except ModuleNotFoundError:
    if _extras.TOMLI_INSTALLED:  # pragma: no cover
        import tomli as tomllib  # type: ignore[import-not-found,no-redef]


logger = logging.getLogger(__name__)


CONFIG_FILES = [".rstcheck.cfg", "setup.cfg"]
"""Supported default config files."""
if _extras.TOMLI_INSTALLED or tomllib_imported:  # pragma: no cover
    CONFIG_FILES = [".rstcheck.cfg", "pyproject.toml", "setup.cfg"]


class ReportLevel(enum.Enum):
    """Report levels supported by docutils."""

    INFO = 1
    WARNING = 2
    ERROR = 3
    SEVERE = 4
    NONE = 5


ReportLevelMap = {
    "info": 1,
    "warning": 2,
    "error": 3,
    "severe": 4,
    "none": 5,
}
"""Map docutils report levels in text form to numbers."""


DEFAULT_REPORT_LEVEL = ReportLevel.INFO
"""Default report level."""


def _split_str_validator(value: t.Any) -> list[str] | None:  # noqa: ANN401
    """Validate and parse strings and string-lists.

    Comma separated strings are split into a list.

    :param value: Value to validate
    :raises ValueError: If not a :py:class:`str` or :py:class:`list` of :py:class:`str`
    :return: List of strings
    """
    if value is None:
        return None

    if isinstance(value, str):
        return [v.strip() for v in value.split(",") if v.strip()]

    if isinstance(value, list) and all(isinstance(v, str) for v in value):
        return [v.strip() for v in value if v.strip()]

    msg = "Not a string or list of strings"
    raise TypeError(msg)


class RstcheckConfigFile(pydantic.BaseModel):
    """Rstcheck config file.

    :raises ValueError: If setting has incorrect value or type
    :raises pydantic.ValidationError: If setting is not parsable into correct type
    """

    report_level: t.Optional[ReportLevel] = None  # noqa: UP007
    ignore_directives: t.Optional[t.List[str]] = None  # noqa: UP007,UP006
    ignore_roles: t.Optional[t.List[str]] = None  # noqa: UP007,UP006
    ignore_substitutions: t.Optional[t.List[str]] = None  # noqa: UP007,UP006
    ignore_languages: t.Optional[t.List[str]] = None  # noqa: UP007,UP006
    ignore_messages: t.Optional[t.Pattern[str]] = None  # noqa: UP007

    @pydantic.field_validator("report_level", mode="before")
    @classmethod
    def valid_report_level(cls, value: t.Any) -> ReportLevel | None:  # noqa: ANN401
        """Validate the report_level setting.

        :param value: Value to validate
        :raises ValueError: If ``value`` is not a valid docutils report level
        :return: Instance of :py:class:`ReportLevel` or None if emptry string.
        """
        if value is None:
            return None

        if isinstance(value, ReportLevel):
            return value

        if value == "":
            return DEFAULT_REPORT_LEVEL

        if isinstance(value, bool):
            msg = "Invalid report level"
            raise TypeError(msg)

        if isinstance(value, str):
            if value.casefold() in set(ReportLevelMap):
                return ReportLevel(ReportLevelMap[value.casefold()])

            with contextlib.suppress(ValueError):
                value = int(value)

        max_report_lvl = 5
        min_report_lvl = 1
        if isinstance(value, int) and min_report_lvl <= value <= max_report_lvl:
            return ReportLevel(value)

        msg = "Invalid report level"
        raise TypeError(msg)

    @pydantic.field_validator(
        "ignore_directives",
        "ignore_roles",
        "ignore_substitutions",
        "ignore_languages",
        mode="before",
    )
    @classmethod
    def split_str(cls, value: t.Any) -> list[str] | None:  # noqa: ANN401
        """Validate and parse the following ignore_* settings.

        - ignore_directives
        - ignore_roles
        - ignore_substitutions
        - ignore_languages

        Comma separated strings are split into a list.

        :param value: Value to validate
        :raises ValueError: If not a :py:class:`str` or :py:class:`list` of :py:class:`str`
        :return: List of things to ignore in the respective category
        """
        return _split_str_validator(value)

    @pydantic.field_validator("ignore_messages", mode="before")
    @classmethod
    def join_regex_str(cls, value: t.Any) -> str | t.Pattern[str] | None:  # noqa: ANN401
        """Validate and concatenate the ignore_messages setting to a RegEx string.

        If a list ist given, the entries are concatenated with "|" to create an or RegEx.

        :param value: Value to validate
        :raises ValueError: If not a :py:class:`str` or :py:class:`list` of :py:class:`str`
        :return: A RegEx string with messages to ignore or :py:class:`typing.Pattern` if it is one
            already
        """
        if value is None:
            return None

        if isinstance(value, re.Pattern):
            return value

        if isinstance(value, list) and all(isinstance(v, str) for v in value):
            return r"|".join(value)

        if isinstance(value, str):
            return value

        msg = "Not a string or list of strings"
        raise TypeError(msg)


class RstcheckConfig(RstcheckConfigFile):
    """Rstcheck config.

    :raises ValueError: If setting has incorrect value or type
    :raises pydantic.ValidationError: If setting is not parsable into correct type
    """

    config_path: t.Optional[pathlib.Path] = None  # noqa: UP007
    recursive: t.Optional[bool] = None  # noqa: UP007
    warn_unknown_settings: t.Optional[bool] = None  # noqa: UP007


class _RstcheckConfigINIFile(pydantic.BaseModel):
    """Type for [rstcheck] section in INI file.

    The types apply to the file's data before the parsing by :py:class:`RstcheckConfig` is done.

    :raises pydantic.ValidationError: If setting is not parsable into correct type
    """

    report_level: t.Union[str, int, None] = None  # noqa: UP007
    ignore_directives: t.Optional[str] = None  # noqa: UP007
    ignore_roles: t.Optional[str] = None  # noqa: UP007
    ignore_substitutions: t.Optional[str] = None  # noqa: UP007
    ignore_languages: t.Optional[str] = None  # noqa: UP007
    ignore_messages: t.Optional[str] = None  # noqa: UP007


def _load_config_from_ini_file(
    ini_file: pathlib.Path,
    *,
    log_missing_section_as_warning: bool = True,
    warn_unknown_settings: bool = False,
) -> RstcheckConfigFile | None:
    """Load, parse and validate rstcheck config from a ini file.

    :param ini_file: INI file to load config from
    :param log_missing_section_as_warning: If a missing [tool.rstcheck] section should be logged at
        WARNING (:py:obj:`True`) or ``INFO`` (:py:obj:`False`) level;
        defaults to :py:obj:`True`
    :param warn_unknown_settings: If a warning should be logged for unknown settings in config file;
        defaults to :py:obj:`False`
    :raises FileNotFoundError: If the file is not found
    :return: instance of :py:class:`RstcheckConfigFile` or :py:class:`None` on missing config
        section
        or ``NONE`` is passed as the config path.
    """
    logger.debug("Try loading config from INI file: '%s'", ini_file)

    if ini_file.name == "NONE":
        logger.info("Config path is set to 'NONE'. No config file is loaded.")
        return None

    resolved_file = ini_file.resolve()

    if not resolved_file.is_file():
        msg = f"{resolved_file}"
        raise FileNotFoundError(msg)

    parser = configparser.ConfigParser()
    parser.read(resolved_file)

    if not parser.has_section("rstcheck"):
        if log_missing_section_as_warning:
            logger.warning(
                "Config file has no [rstcheck] section: '%s'.",
                ini_file,
            )
            return None
        logger.info(
            "Config file has no [rstcheck] section: '%s'.",
            ini_file,
        )
        return None

    config_values_raw = dict(parser.items("rstcheck"))
    if warn_unknown_settings:
        known_settings = _RstcheckConfigINIFile().model_dump().keys()
        unknown = [s for s in config_values_raw if s not in known_settings]
        if unknown:
            logger.warning(
                "Unknown setting(s) %s found in file: '%s'.",
                unknown,
                ini_file,
            )

    config_values_checked = _RstcheckConfigINIFile(**config_values_raw)
    return RstcheckConfigFile(**config_values_checked.model_dump())


class _RstcheckConfigTOMLFile(
    pydantic.BaseModel,
):
    """Type for [tool.rstcheck] section in TOML file.

    The types apply to the file's data before the parsing by :py:class:`RstcheckConfig` is done.

    :raises pydantic.ValidationError: If setting is not parsable into correct type
    """

    report_level: t.Union[str, int, None] = None  # noqa: UP007
    ignore_directives: t.Optional[t.List[str]] = None  # noqa: UP006, UP007
    ignore_roles: t.Optional[t.List[str]] = None  # noqa: UP006, UP007
    ignore_substitutions: t.Optional[t.List[str]] = None  # noqa: UP006, UP007
    ignore_languages: t.Optional[t.List[str]] = None  # noqa: UP006, UP007
    ignore_messages: t.Union[t.List[str], str, None] = None  # noqa: UP006, UP007


def _load_config_from_toml_file(
    toml_file: pathlib.Path,
    *,
    log_missing_section_as_warning: bool = True,
    warn_unknown_settings: bool = False,
) -> RstcheckConfigFile | None:
    """Load, parse and validate rstcheck config from a TOML file.

    .. warning::

        Needs tomli installed for python versions before 3.11!
        Use toml extra.

    :param toml_file: TOML file to load config from
    :param log_missing_section_as_warning: If a missing [tool.rstcheck] section should be logged at
        WARNING (:py:obj:`True`) or ``INFO`` (:py:obj:`False`) level;
        defaults to :py:obj:`True`
    :param warn_unknown_settings: If a warning should be logged for unknown settings in config file;
        defaults to :py:obj:`False`
    :raises ValueError: If the file is not a TOML file
    :raises FileNotFoundError: If the file is not found
    :return: instance of :py:class:`RstcheckConfigFile` or :py:obj:`None` on missing config section
        or ``NONE`` is passed as the config path.
    """
    _extras.install_guard_tomli(tomllib_imported=tomllib_imported)
    logger.debug("Try loading config from TOML file: '%s'.", toml_file)

    if toml_file.name == "NONE":
        logger.info("Config path is set to 'NONE'. No config file is loaded.")
        return None

    resolved_file = toml_file.resolve()

    if not resolved_file.is_file():
        logging.error("Config file is not a file: '%s'.", toml_file)
        msg = f"{resolved_file}"
        raise FileNotFoundError(msg)

    if resolved_file.suffix.casefold() != ".toml":
        logging.error("Config file is not a TOML file: '%s'.", toml_file)
        msg = "File is not a TOML file"
        raise ValueError(msg)

    with pathlib.Path(resolved_file).open("rb") as toml_file_handle:
        toml_dict = tomllib.load(toml_file_handle)

    rstcheck_section: t.Optional[dict[str, t.Any]] = toml_dict.get("tool", {}).get(  # noqa: UP007
        "rstcheck"
    )

    if rstcheck_section is None:
        if log_missing_section_as_warning:
            logger.warning(
                "Config file has no [tool.rstcheck] section: '%s'.",
                toml_file,
            )
            return None
        logger.info(
            "Config file has no [tool.rstcheck] section: '%s'.",
            toml_file,
        )
        return None

    if warn_unknown_settings:
        known_settings = _RstcheckConfigTOMLFile().model_dump().keys()
        unknown = [s for s in rstcheck_section if s not in known_settings]
        if unknown:
            logger.warning(
                "Unknown setting(s) %s found in file: '%s'.",
                unknown,
                toml_file,
            )

    config_values_checked = _RstcheckConfigTOMLFile(**rstcheck_section)
    return RstcheckConfigFile(**config_values_checked.model_dump())


def load_config_file(
    file_path: pathlib.Path,
    *,
    log_missing_section_as_warning: bool = True,
    warn_unknown_settings: bool = False,
) -> RstcheckConfigFile | None:
    """Load, parse and validate rstcheck config from a file.

    .. caution::

        If a TOML file is passed this function need tomli installed for python versions before 3.11!
        Use toml extra or install manually.

    :param file_path: File to load config from
    :param log_missing_section_as_warning: If a missing config section should be logged at
        WARNING (:py:obj:`True`) or ``INFO`` (:py:obj:`False`) level;
        defaults to :py:obj:`True`
    :param warn_unknown_settings: If a warning should be logged for unknown settings in config file;
        defaults to :py:obj:`False`
    :raises FileNotFoundError: If the file is not found
    :return: instance of :py:class:`RstcheckConfigFile` or :py:obj:`None` on missing config section
        or ``NONE`` is passed as the config path.
    """
    logger.debug("Try loading config file.")

    if file_path.name == "NONE":
        logger.info("Config path is set to 'NONE'. No config file is loaded.")
        return None

    if file_path.suffix.casefold() == ".toml":
        return _load_config_from_toml_file(
            file_path,
            log_missing_section_as_warning=log_missing_section_as_warning,
            warn_unknown_settings=warn_unknown_settings,
        )
    return _load_config_from_ini_file(
        file_path,
        log_missing_section_as_warning=log_missing_section_as_warning,
        warn_unknown_settings=warn_unknown_settings,
    )


def load_config_file_from_dir(
    dir_path: pathlib.Path,
    *,
    log_missing_section_as_warning: bool = False,
    warn_unknown_settings: bool = False,
) -> RstcheckConfigFile | None:
    """Search, load, parse and validate rstcheck config from a directory.

    Searches files from :py:data:`CONFIG_FILES` in the directory. If a file is found, try to load
    the config from it. If is has no config, search further.

    :param dir_path: Directory to search
    :param log_missing_section_as_warning: If a missing config section in a config file should be
        logged at WARNING (:py:obj:`True`) or ``INFO`` (:py:obj:`False`) level;
        defaults to :py:obj:`False`
    :param warn_unknown_settings: If a warning should be logged for unknown settings in config file;
        defaults to :py:obj:`False`
    :return: instance of :py:class:`RstcheckConfigFile` or
        :py:obj:`None` if no file is found or no file has a rstcheck section
        or ``NONE`` is passed as the config path.
    """
    logger.debug("Try loading config file from directory: '%s'.", dir_path)

    if dir_path.name == "NONE":
        logger.info("Config path is set to 'NONE'. No config file is loaded.")
        return None

    config = None

    for file_name in CONFIG_FILES:
        file_path = (dir_path / file_name).resolve()
        if file_path.is_file():
            config = load_config_file(
                file_path,
                log_missing_section_as_warning=(
                    log_missing_section_as_warning or (file_name == ".rstcheck.cfg")
                ),
                warn_unknown_settings=warn_unknown_settings,
            )
            if config is not None:
                break

    if config is None:
        logger.info(
            "No config section in supported config files found in directory: '%s'.",
            dir_path,
        )

    return config


def load_config_file_from_dir_tree(
    dir_path: pathlib.Path,
    *,
    log_missing_section_as_warning: bool = False,
    warn_unknown_settings: bool = False,
) -> RstcheckConfigFile | None:
    """Search, load, parse and validate rstcheck config from a directory tree.

    Searches files from :py:data:`CONFIG_FILES` in the directory. If a file is found, try to load
    the config from it. If is has no config, search further. If no config is found in the directory
    search its parents one by one.

    :param dir_path: Directory to search
    :param log_missing_section_as_warning: If a missing config section in a config file should be
        logged at ``WARNING`` (:py:obj:`True`) or ``INFO`` (:py:obj:`False`) level;
        defaults to :py:obj:`False`
    :param warn_unknown_settings: If a warning should be logged for unknown settings in config file;
        defaults to :py:obj:`False`
    :return: instance of :py:class:`RstcheckConfigFile` or
        :py:obj:`None` if no file is found or no file has a rstcheck section
        or ``NONE`` is passed as the config path.
    """
    logger.debug("Try loading config file from directory tree: '%s'.", dir_path)

    if dir_path.name == "NONE":
        logger.info("Config path is set to 'NONE'. No config file is loaded.")
        return None

    config = None

    search_dir = dir_path.resolve()

    while True:
        config = load_config_file_from_dir(
            search_dir,
            log_missing_section_as_warning=log_missing_section_as_warning,
            warn_unknown_settings=warn_unknown_settings,
        )

        if config is not None:
            break

        parent_dir = search_dir.parent.resolve()
        if parent_dir == search_dir:
            break
        search_dir = parent_dir

    if config is None:
        logger.info(
            "No config section in supported config files found in directory tree: '%s'.",
            dir_path,
        )

    return config


def load_config_file_from_path(
    path: pathlib.Path,
    *,
    search_dir_tree: bool = False,
    log_missing_section_as_warning_for_file: bool = True,
    log_missing_section_as_warning_for_dir: bool = False,
    warn_unknown_settings: bool = False,
) -> RstcheckConfigFile | None:
    """Analyse the path and call the correct config file loader.

    :param path: Path to load config file from; can be a file or directory
    :param search_dir_tree: If the directory tree should be searched;
        only applies if ``path`` is a directory;
        defaults to :py:obj:`False`
    :param log_missing_section_as_warning_for_file: If a missing config section in a config file
        should be logged at WARNING (:py:obj:`True`) or ``INFO`` (:py:obj:`False`) level when the
        given path is a file;
        defaults to :py:obj:`True`
    :param log_missing_section_as_warning_for_dir: If a missing config section in a config file
        should be logged at ``WARNING`` (:py:obj:`True`) or ``INFO`` (:py:obj:`False`) level when
        the given file is a direcotry;
        defaults to :py:obj:`False`
    :param warn_unknown_settings: If a warning should be logged for unknown settings in config file;
        defaults to :py:obj:`False`
    :raises FileNotFoundError: When the passed path is not found.
    :return: instance of :py:class:`RstcheckConfigFile` or
        :py:obj:`None` if no file is found or no file has a rstcheck section
        or ``NONE`` is passed as the config path.
    """
    logger.debug("Try loading config file from path: '%s'.", path)

    if path.name == "NONE":
        logger.info("Config path is set to 'NONE'. No config file is loaded.")
        return None

    resolved_path = path.resolve()

    if resolved_path.is_file():
        return load_config_file(
            resolved_path,
            log_missing_section_as_warning=log_missing_section_as_warning_for_file,
            warn_unknown_settings=warn_unknown_settings,
        )

    if resolved_path.is_dir():
        if search_dir_tree:
            return load_config_file_from_dir_tree(
                resolved_path,
                log_missing_section_as_warning=log_missing_section_as_warning_for_dir,
                warn_unknown_settings=warn_unknown_settings,
            )
        return load_config_file_from_dir(
            resolved_path,
            log_missing_section_as_warning=log_missing_section_as_warning_for_dir,
            warn_unknown_settings=warn_unknown_settings,
        )

    raise FileNotFoundError(2, "Passed config path not found.", path)


def merge_configs(
    config_base: RstcheckConfig,
    config_add: RstcheckConfig | RstcheckConfigFile,
    *,
    config_add_is_dominant: bool = True,
) -> RstcheckConfig:
    """Merge two configs into a new one.

    :param config_base: The base config to merge into
    :param config_add: The config that is merged into the ``config_base``
    :param config_add_is_dominant: If the ``config_add`` overwrites values of ``config_base``;
        defaults to :py:obj:`True`
    :return: New merged config
    """
    logger.debug("Merging configs.")
    sub_config: RstcheckConfig | RstcheckConfigFile = config_base
    sub_config_dict = sub_config.model_dump()
    for setting in dict(sub_config_dict):
        if sub_config_dict[setting] is None:
            del sub_config_dict[setting]

    dom_config: RstcheckConfig | RstcheckConfigFile = config_add
    dom_config_dict = dom_config.model_dump()
    for setting in dict(dom_config_dict):
        if dom_config_dict[setting] is None:
            del dom_config_dict[setting]

    if config_add_is_dominant is False:
        sub_config_dict, dom_config_dict = dom_config_dict, sub_config_dict

    merged_config_dict = {**sub_config_dict, **dom_config_dict}

    return RstcheckConfig(**merged_config_dict)
