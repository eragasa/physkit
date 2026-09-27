"""Tests for sparse centered-uniform-link localized perturbation construction."""

import numpy as np

from physkit.periodic.lattice.boundary_phases import (
    BoundaryTwistLift,
    TwistGaugeRepresentation,
)
from physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    LatticeCoordinate,
    LatticeDimension,
    LatticeDisplacement,
)
from physkit.periodic.lattice.hopping import (
    LocalizedBondTerm,
    LocalizedOnsiteTerm,
    LocalizedPerturbation,
)
from physkit.periodic.lattice.operator_construction import (
    LocalizedPerturbationOperatorConstructor,
)
from physkit.units import PhysicalUnit


def test_matches_hand_derived_two_dimensional_uniform_link_matrix() -> None:
    perturbation = LocalizedPerturbation(
        "directional",
        LatticeDimension.TWO,
        (
            LocalizedOnsiteTerm(
                LatticeCoordinate(LatticeDimension.TWO, (0, 0)), 0.2, 0.0
            ),
            LocalizedBondTerm(
                LatticeCoordinate(LatticeDimension.TWO, (0, 0)),
                LatticeDisplacement(LatticeDimension.TWO, (1, 0)),
                0.04,
                0.0,
            ),
            LocalizedBondTerm(
                LatticeCoordinate(LatticeDimension.TWO, (1, 0)),
                LatticeDisplacement(LatticeDimension.TWO, (-1, 0)),
                0.04,
                0.0,
            ),
        ),
        PhysicalUnit("electron_volt"),
        "parent_zero",
        "scalar_cell_basis",
    )

    represented = LocalizedPerturbationOperatorConstructor().execute(
        "directional_operator",
        perturbation,
        FinitePeriodicDomain(LatticeDimension.TWO, (3, 2)),
        BoundaryTwistLift(LatticeDimension.TWO, (0.75, 0.0)),
    )

    expected = np.zeros((6, 6), dtype=np.complex128)
    expected[0, 0] = 0.2
    expected[0, 2] = 0.04j
    expected[2, 0] = -0.04j
    np.testing.assert_allclose(
        represented.matrix.to_csr().toarray(), expected, rtol=0.0, atol=1.0e-17
    )
    assert (
        represented.twist_fiber.gauge is TwistGaugeRepresentation.CENTERED_UNIFORM_LINK
    )
    assert represented.provenance == (
        ("constructor", "LocalizedPerturbationOperatorConstructor"),
        ("source_perturbation", "directional"),
    )


def test_does_not_invent_reverse_bonds() -> None:
    perturbation = LocalizedPerturbation(
        "directed",
        LatticeDimension.ONE,
        (
            LocalizedBondTerm(
                LatticeCoordinate(LatticeDimension.ONE, (0,)),
                LatticeDisplacement(LatticeDimension.ONE, (1,)),
                1.0,
                0.0,
            ),
        ),
        PhysicalUnit("electron_volt"),
        "parent_zero",
        "scalar_cell_basis",
    )

    represented = LocalizedPerturbationOperatorConstructor().execute(
        "directed_operator",
        perturbation,
        FinitePeriodicDomain(LatticeDimension.ONE, (3,)),
        BoundaryTwistLift(LatticeDimension.ONE, (0.0,)),
    )

    matrix = represented.matrix.to_csr()
    assert represented.matrix.nonzero_count == 1
    assert matrix[0, 1] == 1.0 + 0.0j
    assert matrix[1, 0] == 0.0 + 0.0j
