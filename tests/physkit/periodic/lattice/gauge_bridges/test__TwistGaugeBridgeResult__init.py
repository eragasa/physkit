"""Tests for correlated site-diagonal twist-gauge bridge results."""

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
from physkit.periodic.lattice.gauge_bridges import TwistGaugeBridgeConstructor
from physkit.units import ComplexSparseMatrixQuantity, Unitless


def test_requires_ordered_fibers_with_one_common_reduction() -> None:
    reduction = BoundaryTwistReducer().execute(
        BoundaryTwistLift(LatticeDimension.TWO, (1.25, -0.25))
    )
    source = TwistFiber(reduction, TwistGaugeRepresentation.CENTERED_UNIFORM_LINK)
    result = TwistGaugeBridgeConstructor().execute(
        FinitePeriodicDomain(LatticeDimension.TWO, (2, 3)), source
    )

    assert result.source_fiber.reduction == result.target_fiber.reduction
    assert result.transformation.shape == (6, 6)
    with pytest.raises(ValueError, match="target fiber"):
        replace(result, target_fiber=source)


def test_requires_one_unit_magnitude_diagonal_phase_per_site() -> None:
    domain = FinitePeriodicDomain(LatticeDimension.ONE, (1,))
    reduction = BoundaryTwistReducer().execute(
        BoundaryTwistLift(LatticeDimension.ONE, (0.0,))
    )
    source = TwistFiber(reduction, TwistGaugeRepresentation.CENTERED_UNIFORM_LINK)
    result = TwistGaugeBridgeConstructor().execute(domain, source)
    scaling = ComplexSparseMatrixQuantity.from_csr(
        sparse.csr_array(np.array([[2.0 + 0.0j]])), Unitless()
    )

    with pytest.raises(ValueError, match="unit magnitude"):
        replace(result, transformation=scaling)
