"""Tests for sparse represented scalar-operator addition."""

from dataclasses import replace

import numpy as np
import pytest
from scipy import sparse

from projectkoios.physkit.periodic.lattice.boundary_phases import (
    BoundaryTwistLift,
    BoundaryTwistReducer,
    TwistFiber,
    TwistGaugeRepresentation,
)
from projectkoios.physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    LatticeDimension,
)
from projectkoios.physkit.periodic.lattice.operator_composition import (
    ScalarFiniteLatticeOperatorAdder,
    ScalarFiniteLatticeOperatorCompatibilityAnalyzer,
)
from projectkoios.physkit.periodic.lattice.represented_operators import (
    ScalarFiniteLatticeOperator,
)
from projectkoios.physkit.units import ComplexSparseMatrixQuantity, Unitless


def test_adds_compatible_sparse_operators_and_records_sources() -> None:
    domain = FinitePeriodicDomain(LatticeDimension.ONE, (2,))
    fiber = TwistFiber(
        BoundaryTwistReducer().execute(
            BoundaryTwistLift(LatticeDimension.ONE, (0.25,))
        ),
        TwistGaugeRepresentation.CENTERED_UNIFORM_LINK,
    )
    left = ScalarFiniteLatticeOperator(
        "left",
        ComplexSparseMatrixQuantity.from_csr(
            sparse.csr_array(np.array([[1.0, 0.0], [0.0, 2.0]])), Unitless()
        ),
        domain,
        fiber,
        "basis",
        "zero",
        (),
    )
    right = ScalarFiniteLatticeOperator(
        "right",
        ComplexSparseMatrixQuantity.from_csr(
            sparse.csr_array(np.array([[0.0, 3.0], [4.0, 0.0]])), Unitless()
        ),
        domain,
        fiber,
        "basis",
        "zero",
        (),
    )
    compatibility = ScalarFiniteLatticeOperatorCompatibilityAnalyzer().execute(
        left, right
    )

    result = ScalarFiniteLatticeOperatorAdder().execute(
        "sum", left, right, compatibility
    )

    np.testing.assert_array_equal(
        result.matrix.to_dense().magnitude, np.array([[1.0, 3.0], [4.0, 2.0]])
    )
    assert result.domain is domain
    assert result.twist_fiber is fiber
    assert result.provenance == (
        ("composer", "ScalarFiniteLatticeOperatorAdder"),
        ("left_operator", "left"),
        ("right_operator", "right"),
    )


def test_rejects_compatibility_for_different_operand_objects() -> None:
    domain = FinitePeriodicDomain(LatticeDimension.ONE, (1,))
    fiber = TwistFiber(
        BoundaryTwistReducer().execute(BoundaryTwistLift(LatticeDimension.ONE, (0.0,))),
        TwistGaugeRepresentation.QUOTIENT_SEAM,
    )
    matrix = ComplexSparseMatrixQuantity.from_csr(
        sparse.identity(1, dtype=np.complex128, format="csr"), Unitless()
    )
    left = ScalarFiniteLatticeOperator(
        "left", matrix, domain, fiber, "basis", "zero", ()
    )
    right = replace(left, identifier="right")
    different_right = replace(left, identifier="different")
    compatibility = ScalarFiniteLatticeOperatorCompatibilityAnalyzer().execute(
        left, right
    )

    with pytest.raises(ValueError, match="correlate the exact operands"):
        ScalarFiniteLatticeOperatorAdder().execute(
            "sum", left, different_right, compatibility
        )
