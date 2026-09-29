"""Tests for ``LatticeDisplacement.is_zero``."""

from projectkoios.physkit.periodic.lattice.finite_domain import (
    LatticeDimension,
    LatticeDisplacement,
)


def test_identifies_only_the_zero_displacement() -> None:
    assert LatticeDisplacement(LatticeDimension.THREE, (0, 0, 0)).is_zero
    assert not LatticeDisplacement(LatticeDimension.THREE, (0, -1, 0)).is_zero
