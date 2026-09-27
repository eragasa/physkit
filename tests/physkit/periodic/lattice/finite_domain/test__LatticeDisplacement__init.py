"""Tests for ``LatticeDisplacement`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from physkit.periodic.lattice.finite_domain import (
    LatticeDimension,
    LatticeDisplacement,
)


def test_retains_signed_integer_components() -> None:
    displacement = LatticeDisplacement(LatticeDimension.TWO, (-3, 5))

    assert displacement.dimension is LatticeDimension.TWO
    assert displacement.components == (-3, 5)
    with pytest.raises(FrozenInstanceError):
        displacement.components = (0, 0)  # type: ignore[misc]


def test_rejects_noncanonical_or_dimensionally_inconsistent_inputs() -> None:
    with pytest.raises(TypeError, match="dimension must be LatticeDimension"):
        LatticeDisplacement(2, (1, 2))  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="components must be a tuple"):
        LatticeDisplacement(LatticeDimension.TWO, [1, 2])  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="count must match dimension"):
        LatticeDisplacement(LatticeDimension.THREE, (1, 2))
    with pytest.raises(TypeError, match="built-in integers"):
        LatticeDisplacement(LatticeDimension.ONE, (False,))
