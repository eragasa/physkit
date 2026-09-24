"""Deprecated quantum-model implementations.

Use :mod:`physkit.qm.piab1d` for the maintained particle-in-a-box model.
"""

from warnings import warn

__deprecated__ = True

warn(
    "physkit.legacy.qm is deprecated; use physkit.qm.piab1d instead",
    DeprecationWarning,
    stacklevel=2,
)

__all__: list[str] = []
