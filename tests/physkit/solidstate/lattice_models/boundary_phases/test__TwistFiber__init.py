"""Tests for gauge-qualified ``TwistFiber`` identity."""

from physkit.solidstate.lattice_models.boundary_phases import (
    BoundaryTwistLift,
    BoundaryTwistReducer,
    TwistFiber,
    TwistGaugeRepresentation,
)
from physkit.solidstate.lattice_models.geometry import LatticeDimension


def test_retains_lift_representative_quotient_and_gauge() -> None:
    reduction = BoundaryTwistReducer().execute(
        BoundaryTwistLift(LatticeDimension.TWO, (1.25, -0.25))
    )

    fiber = TwistFiber(reduction, TwistGaugeRepresentation.CENTERED_UNIFORM_LINK)

    assert fiber.dimension is LatticeDimension.TWO
    assert fiber.lift.turns == (1.25, -0.25)
    assert fiber.representative.turns == (0.25, 0.75)
    assert fiber.reduction.quotient.components == (1, -1)
    assert fiber.gauge is TwistGaugeRepresentation.CENTERED_UNIFORM_LINK
