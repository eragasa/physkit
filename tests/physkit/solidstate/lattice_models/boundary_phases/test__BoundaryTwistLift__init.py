"""Tests for ``BoundaryTwistLift`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from physkit.solidstate.lattice_models.boundary_phases import BoundaryTwistLift
from physkit.solidstate.lattice_models.geometry import LatticeDimension


def test_retains_finite_unreduced_turns() -> None:
    lift = BoundaryTwistLift(LatticeDimension.TWO, (1.25, -0.25))

    assert lift.turns == (1.25, -0.25)
    with pytest.raises(FrozenInstanceError):
        lift.turns = (0.25, 0.75)  # type: ignore[misc]


def test_rejects_invalid_components() -> None:
    with pytest.raises(ValueError, match="count must match dimension"):
        BoundaryTwistLift(LatticeDimension.TWO, (0.25,))
    with pytest.raises(TypeError, match="built-in floats"):
        BoundaryTwistLift(LatticeDimension.ONE, (1,))  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="must be finite"):
        BoundaryTwistLift(LatticeDimension.ONE, (float("nan"),))
