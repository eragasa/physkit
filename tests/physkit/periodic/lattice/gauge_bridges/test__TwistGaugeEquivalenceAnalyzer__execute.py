"""Tests for represented scalar-operator twist-gauge equivalence analysis."""

from dataclasses import replace

import numpy as np
import pytest
from scipy import sparse

from physkit.periodic.lattice.boundary_phases import BoundaryTwistLift
from physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    LatticeDimension,
    LatticeDisplacement,
)
from physkit.periodic.lattice.gauge_bridges import (
    TwistGaugeBridgeConstructor,
    TwistGaugeEquivalenceAnalyzer,
    TwistGaugeEquivalenceIssueCode,
)
from physkit.periodic.lattice.hopping import ScalarHoppingModel, ScalarHoppingTerm
from physkit.periodic.lattice.operator_construction import (
    TwistedSupercellOperatorConstructor,
)
from physkit.periodic.lattice.represented_operators import (
    ScalarFiniteLatticeOperator,
)
from physkit.units import ComplexSparseMatrixQuantity, PhysicalUnit


def test_compares_equivalent_and_perturbed_matrices_after_the_bridge() -> None:
    unit = PhysicalUnit("electron_volt")
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
        unit,
        "parent_zero",
        "scalar_cell_basis",
    )
    domain = FinitePeriodicDomain(LatticeDimension.ONE, (3,))
    source = TwistedSupercellOperatorConstructor().execute(
        "uniform",
        model,
        domain,
        BoundaryTwistLift(LatticeDimension.ONE, (0.25,)),
    )
    bridge = TwistGaugeBridgeConstructor().execute(domain, source.twist_fiber)
    seam = np.array(
        [[0.0, -1.0, 1.0j], [-1.0, 0.0, -1.0], [-1.0j, -1.0, 0.0]],
        dtype=np.complex128,
    )
    target = ScalarFiniteLatticeOperator(
        "seam",
        ComplexSparseMatrixQuantity.from_csr(sparse.csr_array(seam), unit),
        domain,
        bridge.target_fiber,
        source.basis_identifier,
        source.energy_reference,
        (("route", "hand_derived_seam"),),
    )
    analyzer = TwistGaugeEquivalenceAnalyzer()

    equivalent = analyzer.execute(source, target, bridge, absolute_tolerance=1.0e-14)
    changed = target.matrix.to_csr().toarray()
    changed[0, 0] = 0.01
    perturbed = replace(
        target,
        matrix=ComplexSparseMatrixQuantity.from_csr(sparse.csr_array(changed), unit),
    )
    rejected = analyzer.execute(source, perturbed, bridge, absolute_tolerance=1.0e-14)
    basis_mismatch = analyzer.execute(
        source,
        replace(target, basis_identifier="different_basis"),
        bridge,
        absolute_tolerance=1.0e-14,
    )
    different_domain = FinitePeriodicDomain(LatticeDimension.ONE, (2,))
    domain_mismatch_target = ScalarFiniteLatticeOperator(
        "other_domain",
        ComplexSparseMatrixQuantity.from_csr(
            sparse.identity(2, dtype=np.complex128, format="csr"), unit
        ),
        different_domain,
        bridge.target_fiber,
        source.basis_identifier,
        source.energy_reference,
        (),
    )
    domain_mismatch = analyzer.execute(
        source, domain_mismatch_target, bridge, absolute_tolerance=1.0e-14
    )

    assert equivalent.compatible and equivalent.is_equivalent
    assert equivalent.maximum_absolute_residual is not None
    assert equivalent.maximum_absolute_residual <= 1.0e-15
    assert rejected.maximum_absolute_residual == pytest.approx(0.01)
    assert not rejected.is_equivalent
    assert basis_mismatch.issue_codes == (TwistGaugeEquivalenceIssueCode.BASIS,)
    assert basis_mismatch.maximum_absolute_residual is None
    assert domain_mismatch.issue_codes == (TwistGaugeEquivalenceIssueCode.DOMAIN,)
    assert domain_mismatch.maximum_absolute_residual is None
