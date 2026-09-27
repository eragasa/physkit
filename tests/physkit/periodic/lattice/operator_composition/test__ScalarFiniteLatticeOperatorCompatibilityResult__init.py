"""Tests for represented scalar-operator compatibility results."""

from dataclasses import replace

import numpy as np
import pytest
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
)
from physkit.periodic.lattice.represented_operators import (
    ScalarFiniteLatticeOperator,
)
from physkit.units import ComplexSparseMatrixQuantity, Unitless


def test_requires_issue_codes_to_exactly_describe_operands() -> None:
    matrix = ComplexSparseMatrixQuantity.from_csr(
        sparse.identity(1, dtype=np.complex128, format="csr"), Unitless()
    )
    fiber = TwistFiber(
        BoundaryTwistReducer().execute(BoundaryTwistLift(LatticeDimension.ONE, (0.0,))),
        TwistGaugeRepresentation.CENTERED_UNIFORM_LINK,
    )
    left = ScalarFiniteLatticeOperator(
        "left",
        matrix,
        FinitePeriodicDomain(LatticeDimension.ONE, (1,)),
        fiber,
        "basis",
        "zero",
        (),
    )
    right = replace(left, identifier="right", basis_identifier="other_basis")
    result = ScalarFiniteLatticeOperatorCompatibilityAnalyzer().execute(left, right)

    assert not result.compatible
    with pytest.raises(ValueError, match="exactly describe"):
        replace(result, issue_codes=())
