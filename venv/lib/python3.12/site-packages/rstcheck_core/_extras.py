"""Central place for install-checker and guards for 'extras' dependencies.

The ``*_INSTALLED`` constansts reveal wether the dependency is installed with a supported version.
The :py:func:`install_guard` guard function is intended for use inside functions which need specific
extra packages installed.

Example usage:

.. code-block:: python

    from rstcheck_core import _extras

    if _extras.SPHINX_INSTALLED:
        import sphinx


    def print_sphinx_version():
        _extras.install_guard("sphinx")
        print(sphinx.version_info)
"""

from __future__ import annotations

import importlib
import importlib.metadata
import logging
import typing as t

logger = logging.getLogger(__name__)


ExtraDependencies = t.Literal["sphinx", "tomli"]
"""List of all dependencies installable through extras."""


class DependencyInfos(t.TypedDict):
    """Information about a dependency."""

    min_version: tuple[int, ...]
    extra: str


ExtraDependenciesInfos: dict[ExtraDependencies, DependencyInfos] = {
    "sphinx": DependencyInfos(min_version=(5, 0), extra="sphinx"),
    "tomli": DependencyInfos(min_version=(2, 0), extra="toml"),
}
"""Dependency map with their min. supported version and extra by which they can be installed."""


def is_installed_with_supported_version(package: ExtraDependencies) -> bool:
    """Check if the package is installed and has the minimum required version.

    :param package: Name of packge to check
    :return: Bool if package is installed with supported version
    """
    logger.debug(
        "Check if package is installed with supported version: '%s'.",
        package,
    )
    try:
        importlib.import_module(package)
    except ImportError:
        return False

    version: str = importlib.metadata.version(package)
    version_tuple = tuple(int(v) for v in version.split(".")[:3])

    return version_tuple >= ExtraDependenciesInfos[package]["min_version"]


SPHINX_INSTALLED = is_installed_with_supported_version("sphinx")
TOMLI_INSTALLED = is_installed_with_supported_version("tomli")


ExtraDependenciesInstalled: dict[ExtraDependencies, bool] = {
    "sphinx": SPHINX_INSTALLED,
    "tomli": TOMLI_INSTALLED,
}


def install_guard(package: ExtraDependencies) -> None:
    """Guard code that needs the ``package`` installed and throw :py:exc:`ModuleNotFoundError`.

    See example in module docstring.

    :param package: Name of packge to check
    :raises ModuleNotFoundError: When the package is not installed.
    """
    if ExtraDependenciesInstalled[package] is True:
        return

    extra = ExtraDependenciesInfos[package]

    msg = (
        f"No supported version of {package} installed. Install rstcheck with "
        f"{extra} extra (rstcheck[{extra}]) or install a supported version of {package} yourself."
    )
    raise ModuleNotFoundError(msg)


def install_guard_tomli(*, tomllib_imported: bool) -> None:
    """Specific version of :py:func:`install_guard` for ``tomli``.

    :param tomllib_imported: If tomllib is imported
    :raises ModuleNotFoundError: When ``tomli`` is not installed.
    """
    if tomllib_imported or ExtraDependenciesInstalled["tomli"] is True:
        return

    extra = ExtraDependenciesInfos["tomli"]

    msg = (
        f"tomllib could not be imported and no supported version of tomli installed. "
        f"Install rstcheck with {extra} extra (rstcheck[{extra}]) or install a "
        "supported version of tomli yourself."
    )
    raise ModuleNotFoundError(msg)
