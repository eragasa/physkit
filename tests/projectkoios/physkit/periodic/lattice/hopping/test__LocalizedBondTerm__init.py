"""Tests for ``LocalizedBondTerm`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from projectkoios.physkit.periodic.lattice.finite_domain import (
    LatticeCoordinate,
    LatticeDimension,
    LatticeDisplacement,
)
from projectkoios.physkit.periodic.lattice.hopping import LocalizedBondTerm


def test_retains_compatible_site_displacement_and_coefficient() -> None:
    start = LatticeCoordinate(LatticeDimension.TWO, (0, 1))
    displacement = LatticeDisplacement(LatticeDimension.TWO, (1, -1))
    term = LocalizedBondTerm(start, displacement, 0.05, 0.02)

    assert term.start is start
    assert term.displacement is displacement
    assert term.value == complex(0.05, 0.02)
    with pytest.raises(FrozenInstanceError):
        term.real = 0.0  # type: ignore[misc]


def test_rejects_zero_dimensionally_incompatible_and_nonfinite_bonds() -> None:
    start = LatticeCoordinate(LatticeDimension.TWO, (0, 0))
    with pytest.raises(ValueError, match="dimensions must agree"):
        LocalizedBondTerm(
            start,
            LatticeDisplacement(LatticeDimension.ONE, (1,)),
            0.1,
            0.0,
        )
    with pytest.raises(ValueError, match="must be nonzero"):
        LocalizedBondTerm(
            start,
            LatticeDisplacement(LatticeDimension.TWO, (0, 0)),
            0.1,
            0.0,
        )
    with pytest.raises(ValueError, match="must be finite"):
        LocalizedBondTerm(
            start,
            LatticeDisplacement(LatticeDimension.TWO, (1, 0)),
            float("inf"),
            0.0,
        )
