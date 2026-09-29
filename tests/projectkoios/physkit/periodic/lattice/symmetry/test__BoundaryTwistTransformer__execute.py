"""Tests for signed-axis-permutation transformation of twist lifts."""

import pytest

from projectkoios.physkit.periodic.lattice.boundary_phases import BoundaryTwistLift
from projectkoios.physkit.periodic.lattice.finite_domain import LatticeDimension
from projectkoios.physkit.periodic.lattice.symmetry import (
    BoundaryTwistTransformer,
    IntegralLatticeOperation,
)


def test_transforms_signed_axis_permutations_and_rejects_shears() -> None:
    cycle = IntegralLatticeOperation(
        "cycle",
        LatticeDimension.THREE,
        ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
    )
    shear = IntegralLatticeOperation("shear", LatticeDimension.TWO, ((1, 1), (0, 1)))

    result = BoundaryTwistTransformer().execute(
        cycle, BoundaryTwistLift(LatticeDimension.THREE, (0.1, 0.2, 0.3))
    )

    assert result.turns == (0.2, 0.3, 0.1)
    with pytest.raises(ValueError, match="signed axis permutation"):
        BoundaryTwistTransformer().execute(
            shear, BoundaryTwistLift(LatticeDimension.TWO, (0.1, 0.2))
        )
