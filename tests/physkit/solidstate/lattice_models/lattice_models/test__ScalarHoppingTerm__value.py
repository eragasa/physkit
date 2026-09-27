"""Tests for ``ScalarHoppingTerm.value``."""

from physkit.solidstate.lattice_models.geometry import (
    LatticeDimension,
    LatticeDisplacement,
)
from physkit.solidstate.lattice_models.lattice_models import ScalarHoppingTerm


def test_returns_the_represented_complex_coefficient() -> None:
    term = ScalarHoppingTerm(
        LatticeDisplacement(LatticeDimension.ONE, (1,)), -1.5, 0.25
    )

    assert term.value == complex(-1.5, 0.25)
    assert type(term.value) is complex
