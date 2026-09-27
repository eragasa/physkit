"""Tests for ``LocalizedBondTerm.value``."""

from physkit.solidstate.lattice_models.geometry import (
    LatticeCoordinate,
    LatticeDimension,
    LatticeDisplacement,
)
from physkit.solidstate.lattice_models.lattice_models import LocalizedBondTerm


def test_returns_the_represented_complex_coefficient() -> None:
    term = LocalizedBondTerm(
        LatticeCoordinate(LatticeDimension.ONE, (0,)),
        LatticeDisplacement(LatticeDimension.ONE, (1,)),
        0.05,
        -0.02,
    )

    assert term.value == complex(0.05, -0.02)
