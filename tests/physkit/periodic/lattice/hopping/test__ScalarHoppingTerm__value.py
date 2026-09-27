"""Tests for ``ScalarHoppingTerm.value``."""

from physkit.periodic.lattice.finite_domain import (
    LatticeDimension,
    LatticeDisplacement,
)
from physkit.periodic.lattice.hopping import ScalarHoppingTerm


def test_returns_the_represented_complex_coefficient() -> None:
    term = ScalarHoppingTerm(
        LatticeDisplacement(LatticeDimension.ONE, (1,)), -1.5, 0.25
    )

    assert term.value == complex(-1.5, 0.25)
    assert type(term.value) is complex
