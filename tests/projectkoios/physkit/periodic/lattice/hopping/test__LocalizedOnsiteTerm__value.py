"""Tests for ``LocalizedOnsiteTerm.value``."""

from projectkoios.physkit.periodic.lattice.finite_domain import (
    LatticeCoordinate,
    LatticeDimension,
)
from projectkoios.physkit.periodic.lattice.hopping import LocalizedOnsiteTerm


def test_returns_the_represented_complex_coefficient() -> None:
    term = LocalizedOnsiteTerm(LatticeCoordinate(LatticeDimension.ONE, (0,)), 0.2, -0.1)

    assert term.value == complex(0.2, -0.1)
