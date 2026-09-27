"""Tests for ``ScalarFiniteLatticeOperator.dimension``."""

import numpy as np
from scipy import sparse

from physkit.solidstate.lattice_models.boundary_phases import (
    BoundaryTwistLift,
    BoundaryTwistReducer,
    TwistFiber,
    TwistGaugeRepresentation,
)
from physkit.solidstate.lattice_models.geometry import (
    FiniteLatticeShape,
    LatticeDimension,
)
from physkit.solidstate.lattice_models.represented_operators import (
    ScalarFiniteLatticeOperator,
)
from physkit.units import ComplexSparseMatrixQuantity, Unitless


def test_returns_the_finite_shape_dimension() -> None:
    shape = FiniteLatticeShape(LatticeDimension.THREE, (1, 1, 2))
    represented = ScalarFiniteLatticeOperator(
        "operator",
        ComplexSparseMatrixQuantity.from_csr(
            sparse.identity(2, dtype=np.complex128, format="csr"), Unitless()
        ),
        shape,
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
