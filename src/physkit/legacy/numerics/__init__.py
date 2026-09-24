"""Deprecated numerical implementations.

Use the maintained :mod:`physkit.numerics` and :mod:`physkit.operators`
packages for new code.
"""

from warnings import warn

__deprecated__ = True

warn(
    "physkit.legacy.numerics is deprecated; use physkit.numerics or "
    "physkit.operators instead",
    DeprecationWarning,
    stacklevel=2,
)

__all__: list[str] = []
