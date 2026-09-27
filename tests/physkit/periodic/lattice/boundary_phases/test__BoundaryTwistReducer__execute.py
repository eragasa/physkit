"""Tests for boundary-twist reduction."""

from physkit.periodic.lattice.boundary_phases import (
    BoundaryTwistLift,
    BoundaryTwistReducer,
)
from physkit.periodic.lattice.finite_domain import LatticeDimension


def test_separates_representative_and_integer_quotient() -> None:
    lift = BoundaryTwistLift(LatticeDimension.TWO, (0.25, -0.25))
    result = BoundaryTwistReducer().execute(lift)

    assert result.lift is lift
    assert result.representative.turns == (0.25, 0.75)
    assert result.quotient.components == (0, -1)
