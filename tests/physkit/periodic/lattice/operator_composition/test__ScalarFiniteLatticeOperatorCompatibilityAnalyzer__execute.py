"""Tests for represented scalar-operator compatibility analysis."""

from dataclasses import replace

import numpy as np
from scipy import sparse

from physkit.periodic.lattice.boundary_phases import (
    BoundaryTwistLift,
    BoundaryTwistReducer,
    TwistFiber,
    TwistGaugeRepresentation,
)
from physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    LatticeDimension,
)
from physkit.periodic.lattice.operator_composition import (
    ScalarFiniteLatticeOperatorCompatibilityAnalyzer,
    ScalarFiniteLatticeOperatorCompatibilityIssueCode,
)
from physkit.periodic.lattice.represented_operators import (
    ScalarFiniteLatticeOperator,
)
from physkit.units import ComplexSparseMatrixQuantity, PhysicalUnit, Unitless


def test_reports_every_represented_metadata_mismatch() -> None:
    reduction = BoundaryTwistReducer().execute(
        BoundaryTwistLift(LatticeDimension.ONE, (0.0,))
    )
    left = ScalarFiniteLatticeOperator(
        "left",
        ComplexSparseMatrixQuantity.from_csr(
            sparse.identity(1, dtype=np.complex128, format="csr"), Unitless()
        ),
        FinitePeriodicDomain(LatticeDimension.ONE, (1,)),
        TwistFiber(reduction, TwistGaugeRepresentation.CENTERED_UNIFORM_LINK),
        "basis",
        "zero",
        (),
    )
    right = ScalarFiniteLatticeOperator(
        "right",
        ComplexSparseMatrixQuantity.from_csr(
            sparse.identity(2, dtype=np.complex128, format="csr"),
            PhysicalUnit("electron_volt"),
        ),
        FinitePeriodicDomain(LatticeDimension.ONE, (2,)),
        TwistFiber(reduction, TwistGaugeRepresentation.QUOTIENT_SEAM),
        "other_basis",
        "other_zero",
        (),
    )
    analyzer = ScalarFiniteLatticeOperatorCompatibilityAnalyzer()

    passing = analyzer.execute(left, replace(left, identifier="same"))
    failing = analyzer.execute(left, right)

    assert passing.compatible
    assert failing.issue_codes == (
        ScalarFiniteLatticeOperatorCompatibilityIssueCode.BASIS,
        ScalarFiniteLatticeOperatorCompatibilityIssueCode.ENERGY_REFERENCE,
        ScalarFiniteLatticeOperatorCompatibilityIssueCode.SHAPE,
        ScalarFiniteLatticeOperatorCompatibilityIssueCode.TWIST_FIBER,
        ScalarFiniteLatticeOperatorCompatibilityIssueCode.UNIT,
    )
    assert not failing.compatible
