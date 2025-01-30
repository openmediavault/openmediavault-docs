"""Docutils helper functions."""

from __future__ import annotations

import importlib
import logging
import typing as t

import docutils.nodes
import docutils.parsers.rst.directives
import docutils.parsers.rst.roles
import docutils.writers

from . import _extras

logger = logging.getLogger(__name__)


class IgnoredDirective(docutils.parsers.rst.Directive):  # pragma: no cover
    """Stub for unknown directives."""

    has_content = True

    def run(self) -> list:  # type: ignore[type-arg]
        """Do nothing."""
        return []


def ignore_role(  # noqa: PLR0913
    name: str,  # noqa: ARG001
    rawtext: str,  # noqa: ARG001
    text: str,  # noqa: ARG001
    lineno: int,  # noqa: ARG001
    inliner: docutils.parsers.rst.states.Inliner,  # noqa: ARG001
    options: t.Mapping[str, t.Any] | None = None,  # noqa: ARG001
    content: t.Sequence[str] | None = None,  # noqa: ARG001
) -> tuple[
    t.Sequence[docutils.nodes.reference], t.Sequence[docutils.nodes.reference]
]:  # pragma: no cover
    """Stub for unknown roles."""
    return ([], [])


def clean_docutils_directives_and_roles_cache() -> None:  # pragma: no cover
    """Clean docutils' directives and roles cache by reloading their modules.

    Reloads:
    - :py:mod:`docutils.parsers.rst.directives`
    - :py:mod:`docutils.parsers.rst.roles`
    """
    logger.info("Reload module docutils.parsers.rst.directives/roles")
    importlib.reload(docutils.parsers.rst.directives)
    importlib.reload(docutils.parsers.rst.roles)


def ignore_directives_and_roles(directives: list[str], roles: list[str]) -> None:
    """Ignore directives and roles in docutils.

    :param directives: Directives to ignore
    :param roles: Roles to ignore
    """
    for directive in directives:
        docutils.parsers.rst.directives.register_directive(directive, IgnoredDirective)

    for role in roles:
        docutils.parsers.rst.roles.register_local_role(role, ignore_role)


class CodeBlockDirective(docutils.parsers.rst.Directive):
    """Code block directive."""

    has_content = True
    optional_arguments = 1

    def run(self) -> list[docutils.nodes.literal_block]:
        """Run directive.

        :return: Literal block
        """
        try:
            language = self.arguments[0]
        except IndexError:
            language = ""
        code = "\n".join(self.content)
        literal = docutils.nodes.literal_block(code, code)
        literal["classes"].append("code-block")
        literal["language"] = language
        return [literal]


def register_code_directive(
    *,
    ignore_code_directive: bool = False,
    ignore_codeblock_directive: bool = False,
    ignore_sourcecode_directive: bool = False,
) -> None:
    """Optionally register code directives.

    :param ignore_code_directive: If "code" directive should be ignored,
        so that the code block will not be checked; defaults to :py:obj:`False`
    :param ignore_codeblock_directive: If "code-block" directive should be ignored,
        so that the code block will not be checked; defaults to :py:obj:`False`
    :param ignore_sourcecode_directive: If "sourcecode" directive should be ignored,
        so that the code block will not be checked; defaults to :py:obj:`False`
    """
    if not _extras.SPHINX_INSTALLED:
        if ignore_code_directive is False:
            logger.debug("Register custom directive for 'code'.")
            docutils.parsers.rst.directives.register_directive("code", CodeBlockDirective)
        # NOTE: docutils maps `code-block` and `sourcecode` to `code`
        if ignore_codeblock_directive is False:
            logger.debug("Register custom directive for 'code-block'.")
            docutils.parsers.rst.directives.register_directive("code-block", CodeBlockDirective)
        if ignore_sourcecode_directive is False:
            logger.debug("Register custom directive for 'sourcecode'.")
            docutils.parsers.rst.directives.register_directive("sourcecode", CodeBlockDirective)
