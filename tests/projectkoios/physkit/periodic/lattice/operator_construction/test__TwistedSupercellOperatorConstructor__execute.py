"""Tests for sparse centered-uniform-link parent construction."""

import math

import numpy as np
import pytest

from projectkoios.physkit.periodic.lattice.boundary_phases import (
    BoundaryTwistLift,
    TwistGaugeRepresentation,
)
from projectkoios.physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    LatticeDimension,
    LatticeDisplacement,
)
from projectkoios.physkit.periodic.lattice.hopping import (
    ScalarHoppingModel,
    ScalarHoppingTerm,
)
from projectkoios.physkit.periodic.lattice.operator_construction import (
    TwistedSupercellOperatorConstructor,
)
from projectkoios.physkit.units import PhysicalUnit


def test_matches_hand_derived_one_dimensional_uniform_link_matrix() -> None:
    model = ScalarHoppingModel(
        "nearest_neighbor",
        LatticeDimension.ONE,
        (
            ScalarHoppingTerm(
                LatticeDisplacement(LatticeDimension.ONE, (-1,)), -1.0, 0.0
            ),
            ScalarHoppingTerm(
                LatticeDisplacement(LatticeDimension.ONE, (1,)), -1.0, 0.0
            ),
        ),
        PhysicalUnit("electron_volt"),
        "parent_zero",
        "scalar_cell_basis",
    )

    represented = TwistedSupercellOperatorConstructor().execute(
        "three_site_ring",
        model,
        FinitePeriodicDomain(LatticeDimension.ONE, (3,)),
        BoundaryTwistLift(LatticeDimension.ONE, (0.25,)),
    )

    phase = complex(math.sqrt(3.0) / 2.0, 0.5)
    expected = np.array(
        [
            [0.0, -phase, -phase.conjugate()],
            [-phase.conjugate(), 0.0, -phase],
            [-phase, -phase.conjugate(), 0.0],
        ],
        dtype=np.complex128,
    )
    np.testing.assert_allclose(
        represented.matrix.to_csr().toarray(), expected, rtol=0.0, atol=1.0e-15
    )
    assert represented.twist_fiber.lift.turns == (0.25,)
    assert (
        represented.twist_fiber.gauge is TwistGaugeRepresentation.CENTERED_UNIFORM_LINK
    )
    assert represented.provenance == (
        ("constructor", "TwistedSupercellOperatorConstructor"),
        ("source_model", "nearest_neighbor"),
    )


def test_constructs_closed_two_and_three_dimensional_domains() -> None:
    constructor = TwistedSupercellOperatorConstructor()
    two_model = ScalarHoppingModel(
        "onsite_2d",
        LatticeDimension.TWO,
        (
            ScalarHoppingTerm(
                LatticeDisplacement(LatticeDimension.TWO, (0, 0)), 2.0, 0.0
            ),
        ),
        PhysicalUnit("electron_volt"),
        "parent_zero",
        "scalar_cell_basis",
    )
    three_model = ScalarHoppingModel(
        "onsite_3d",
        LatticeDimension.THREE,
        (
            ScalarHoppingTerm(
                LatticeDisplacement(LatticeDimension.THREE, (0, 0, 0)),
                2.0,
                0.0,
            ),
        ),
        PhysicalUnit("electron_volt"),
        "parent_zero",
        "scalar_cell_basis",
    )

    two = constructor.execute(
        "two",
        two_model,
        FinitePeriodicDomain(LatticeDimension.TWO, (2, 3)),
        BoundaryTwistLift(LatticeDimension.TWO, (1.25, -0.25)),
    )
    three = constructor.execute(
        "three",
        three_model,
        FinitePeriodicDomain(LatticeDimension.THREE, (2, 1, 2)),
        BoundaryTwistLift(LatticeDimension.THREE, (0.1, 0.2, 0.3)),
    )

    np.testing.assert_array_equal(two.matrix.to_csr().toarray(), 2.0 * np.eye(6))
    np.testing.assert_array_equal(three.matrix.to_csr().toarray(), 2.0 * np.eye(4))
    assert two.twist_fiber.representative.turns == (0.25, 0.75)
    assert two.twist_fiber.reduction.quotient.components == (1, -1)


def test_rejects_cross_dimension_inputs() -> None:
    model = ScalarHoppingModel(
        "onsite",
        LatticeDimension.ONE,
        (ScalarHoppingTerm(LatticeDisplacement(LatticeDimension.ONE, (0,)), 1.0, 0.0),),
        PhysicalUnit("electron_volt"),
        "parent_zero",
        "scalar_cell_basis",
    )

    with pytest.raises(ValueError, match="model and finite-lattice"):
        TwistedSupercellOperatorConstructor().execute(
            "mismatch",
            model,
            FinitePeriodicDomain(LatticeDimension.TWO, (2, 2)),
            BoundaryTwistLift(LatticeDimension.TWO, (0.0, 0.0)),
        )
