"""Tests for ``LatticeCoordinate`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from physkit.solidstate.lattice_models.geometry import (
    LatticeCoordinate,
    LatticeDimension,
)


def test_retains_exact_integer_components() -> None:
    coordinate = LatticeCoordinate(LatticeDimension.THREE, (-2, 0, 4))

    assert coordinate.dimension is LatticeDimension.THREE
    assert coordinate.components == (-2, 0, 4)
    with pytest.raises(FrozenInstanceError):
        coordinate.components = (0, 0, 0)  # type: ignore[misc]


def test_rejects_noncanonical_or_dimensionally_inconsistent_inputs() -> None:
    with pytest.raises(TypeError, match="dimension must be LatticeDimension"):
        LatticeCoordinate(2, (1, 2))  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="components must be a tuple"):
        LatticeCoordinate(LatticeDimension.TWO, [1, 2])  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="count must match dimension"):
        LatticeCoordinate(LatticeDimension.TWO, (1,))
    with pytest.raises(TypeError, match="built-in integers"):
        LatticeCoordinate(LatticeDimension.ONE, (True,))
