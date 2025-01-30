"""Helper types."""

from __future__ import annotations

import pathlib
import typing as t

SourceFileOrString = t.Union[pathlib.Path, t.Literal["<string>", "<stdin>"]]  # noqa: UP007
"""Path to source file or if it is a string then '<string>' or '<stdin>'."""


class LintError(t.TypedDict):
    """Dict with information about an linting error."""

    source_origin: SourceFileOrString
    line_number: int
    message: str


YieldedLintError = t.Generator[LintError, None, None]
"""Yielded version of type :py:class:`LintError`."""


class IgnoreDict(t.TypedDict):
    """Dict with ignore information."""

    messages: t.Pattern[str] | None
    languages: list[str]
    directives: list[str]
    roles: list[str]
    substitutions: list[str]


def construct_ignore_dict(
    messages: t.Pattern[str] | None = None,
    languages: list[str] | None = None,
    directives: list[str] | None = None,
    roles: list[str] | None = None,
    substitutions: list[str] | None = None,
) -> IgnoreDict:
    """Create an :py:class:`IgnoreDict` with passed values or defaults.

    :param messages: Value for :py:attr:`IgnoreDict.messages`;
        :py:obj:`None` results in an empty list; defaults to :py:obj:`None`
    :param directives: Value for :py:attr:`IgnoreDict.directives`;
        :py:obj:`None` results in an empty list; defaults to :py:obj:`None`
    :param roles: Value for :py:attr:`IgnoreDict.roles`;
        :py:obj:`None` results in an empty list; defaults to :py:obj:`None`
    :param substitutions: Value for :py:attr:`IgnoreDict.substitutions`;
        :py:obj:`None` results in an empty list; defaults to :py:obj:`None`
    :return: :py:class:`IgnoreDict` with passed values or defaults
    """
    return IgnoreDict(
        messages=messages,
        languages=languages if languages is not None else [],
        directives=directives if directives is not None else [],
        roles=roles if roles is not None else [],
        substitutions=substitutions if substitutions is not None else [],
    )


CheckerRunFunction = t.Callable[..., YieldedLintError]
"""Function to run checks.

Returned by :py:meth:`rstcheck_core.checker.CodeBlockChecker.create_checker`.
"""


class InlineConfig(t.TypedDict):
    """Dict with a config key and config value comming from a inline config comment."""

    key: str
    value: str


class InlineFlowControl(t.TypedDict):
    """Dict with a flow control value and line number comming from a inline config comment."""

    value: str
    line_number: int
