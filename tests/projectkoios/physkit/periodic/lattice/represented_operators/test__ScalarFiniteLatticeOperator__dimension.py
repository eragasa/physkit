"""Tests for ``ScalarFiniteLatticeOperator.dimension``."""

import numpy as np
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
from projectkoios.physkit.periodic.lattice.represented_operators import (
    ScalarFiniteLatticeOperator,
)
from projectkoios.physkit.units import ComplexSparseMatrixQuantity, Unitless


def test_returns_the_finite_periodic_domain_dimension() -> None:
    domain = FinitePeriodicDomain(LatticeDimension.THREE, (1, 1, 2))
    represented = ScalarFiniteLatticeOperator(
        "operator",
        ComplexSparseMatrixQuantity.from_csr(
            sparse.identity(2, dtype=np.complex128, format="csr"), Unitless()
        ),
        domain,
        TwistFiber(
            BoundaryTwistReducer().execute(
                BoundaryTwistLift(LatticeDimension.THREE, (0.0, 0.0, 0.0))
            ),
            TwistGaugeRepresentation.QUOTIENT_SEAM,
        ),
        "basis",
        "zero",
        (),
    )

    assert represented.dimension is LatticeDimension.THREE
