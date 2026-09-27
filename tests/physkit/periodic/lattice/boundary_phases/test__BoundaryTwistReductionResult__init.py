"""Tests for ``BoundaryTwistReductionResult`` construction."""

import pytest

from physkit.core.results import ResultsObject
from physkit.periodic.lattice.boundary_phases import (
    BoundaryTwistLift,
    BoundaryTwistReductionResult,
    BoundaryTwistRepresentative,
)
from physkit.periodic.lattice.finite_domain import (
    LatticeDimension,
    LatticeDisplacement,
)


def test_retains_correlated_reduction_members() -> None:
    lift = BoundaryTwistLift(LatticeDimension.TWO, (0.25, -0.25))
    representative = BoundaryTwistRepresentative(
        LatticeDimension.TWO, (0.25, 0.75)
    )
    quotient = LatticeDisplacement(LatticeDimension.TWO, (0, -1))
    result = BoundaryTwistReductionResult(lift, representative, quotient)

    assert isinstance(result, ResultsObject)
    assert result.lift is lift
    assert result.representative is representative
    assert result.quotient is quotient


def test_rejects_dimensionally_inconsistent_members() -> None:
    with pytest.raises(ValueError, match="dimensions must agree"):
        BoundaryTwistReductionResult(
            BoundaryTwistLift(LatticeDimension.ONE, (0.25,)),
            BoundaryTwistRepresentative(LatticeDimension.ONE, (0.25,)),
            LatticeDisplacement(LatticeDimension.TWO, (0, 0)),
        )
