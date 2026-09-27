"""Tests for ``LocalizedOnsiteTerm.value``."""

from physkit.solidstate.lattice_models.geometry import (
    LatticeCoordinate,
    LatticeDimension,
)
from physkit.solidstate.lattice_models.lattice_models import LocalizedOnsiteTerm


def test_returns_the_represented_complex_coefficient() -> None:
    term = LocalizedOnsiteTerm(
        LatticeCoordinate(LatticeDimension.ONE, (0,)), 0.2, -0.1
    )

    assert term.value == complex(0.2, -0.1)
