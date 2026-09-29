"""Tests for represented twist-gauge equivalence results."""

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
from projectkoios.physkit.periodic.lattice.gauge_bridges import (
    TwistGaugeBridgeConstructor,
    TwistGaugeEquivalenceAnalyzer,
)
from projectkoios.physkit.periodic.lattice.represented_operators import (
    ScalarFiniteLatticeOperator,
)
from projectkoios.physkit.units import ComplexSparseMatrixQuantity, Unitless


def test__init__requires_residual_presence_to_agree_with_compatibility() -> None:
    domain = FinitePeriodicDomain(LatticeDimension.ONE, (1,))
    reduction = BoundaryTwistReducer().execute(
        BoundaryTwistLift(LatticeDimension.ONE, (0.0,))
    )
    source_fiber = TwistFiber(reduction, TwistGaugeRepresentation.CENTERED_UNIFORM_LINK)
    bridge = TwistGaugeBridgeConstructor().execute(domain, source_fiber)
    matrix = ComplexSparseMatrixQuantity.from_csr(
        sparse.csr_array(np.array([[2.0 + 0.0j]])), Unitless()
    )
    source = ScalarFiniteLatticeOperator(
        "source", matrix, domain, source_fiber, "basis", "zero", ()
    )
    target = ScalarFiniteLatticeOperator(
        "target", matrix, domain, bridge.target_fiber, "basis", "zero", ()
    )

    result = TwistGaugeEquivalenceAnalyzer().execute(
        source, target, bridge, absolute_tolerance=0.0
    )

    assert result.compatible and result.is_equivalent
    assert result.maximum_absolute_residual == 0.0
    with pytest.raises(ValueError, match="residual presence"):
        replace(result, maximum_absolute_residual=None)
