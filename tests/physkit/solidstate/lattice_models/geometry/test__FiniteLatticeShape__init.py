"""Tests for ``FiniteLatticeShape`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from physkit.solidstate.lattice_models.geometry import (
    FiniteLatticeShape,
    LatticeDimension,
    LatticeSiteOrdering,
)


def test_retains_positive_integer_extents_and_ordering() -> None:
    shape = FiniteLatticeShape(LatticeDimension.THREE, (2, 3, 4))

    assert shape.dimension is LatticeDimension.THREE
    assert shape.extents == (2, 3, 4)
    assert shape.ordering is LatticeSiteOrdering.LAST_AXIS_FASTEST
    with pytest.raises(FrozenInstanceError):
        shape.extents = (1, 1, 1)  # type: ignore[misc]


def test_rejects_noncanonical_or_invalid_extents() -> None:
    with pytest.raises(ValueError, match="count must match dimension"):
        FiniteLatticeShape(LatticeDimension.TWO, (2,))
    with pytest.raises(TypeError, match="built-in integers"):
        FiniteLatticeShape(LatticeDimension.ONE, (True,))
    with pytest.raises(ValueError, match="extents must be positive"):
        FiniteLatticeShape(LatticeDimension.TWO, (2, 0))
    with pytest.raises(TypeError, match="ordering must be LatticeSiteOrdering"):
        FiniteLatticeShape(
            LatticeDimension.ONE,
            (2,),
            "last_axis_fastest",  # type: ignore[arg-type]
        )
