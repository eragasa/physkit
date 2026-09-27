"""Tests for site-diagonal twist-gauge bridge construction."""

import math

import numpy as np

from physkit.periodic.lattice.boundary_phases import (
    BoundaryTwistLift,
    TwistGaugeRepresentation,
)
from physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    LatticeDimension,
    LatticeDisplacement,
)
from physkit.periodic.lattice.gauge_bridges import (
    TwistGaugeBridgeConstructor,
    TwistGaugeBridgeConvention,
)
from physkit.periodic.lattice.hopping import ScalarHoppingModel, ScalarHoppingTerm
from physkit.periodic.lattice.operator_construction import (
    TwistedSupercellOperatorConstructor,
)
from physkit.units import PhysicalUnit


def test_matches_diagonal_phases_and_declared_seam_relation() -> None:
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
    domain = FinitePeriodicDomain(LatticeDimension.ONE, (3,))
    uniform = TwistedSupercellOperatorConstructor().execute(
        "uniform",
        model,
        domain,
        BoundaryTwistLift(LatticeDimension.ONE, (0.25,)),
    )

    bridge = TwistGaugeBridgeConstructor().execute(domain, uniform.twist_fiber)

    expected_diagonal = np.array(
        [
            1.0 + 0.0j,
            complex(math.sqrt(3.0) / 2.0, 0.5),
            complex(0.5, math.sqrt(3.0) / 2.0),
        ]
    )
    np.testing.assert_allclose(
        bridge.transformation.data,
        expected_diagonal,
        rtol=0.0,
        atol=1.0e-15,
    )
    unitary = bridge.transformation.to_csr()
    transformed = unitary @ uniform.matrix.to_csr() @ unitary.conjugate().transpose()
    expected_seam = np.array(
        [[0.0, -1.0, 1.0j], [-1.0, 0.0, -1.0], [-1.0j, -1.0, 0.0]],
        dtype=np.complex128,
    )
    np.testing.assert_allclose(
        transformed.toarray(), expected_seam, rtol=0.0, atol=1.0e-15
    )
    assert bridge.source_fiber.gauge is TwistGaugeRepresentation.CENTERED_UNIFORM_LINK
    assert bridge.target_fiber.gauge is TwistGaugeRepresentation.QUOTIENT_SEAM
    assert (
        bridge.convention is TwistGaugeBridgeConvention.TARGET_EQUALS_U_SOURCE_U_DAGGER
    )
