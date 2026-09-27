"""Tests for ``ScalarFiniteLatticeOperator`` construction."""

from dataclasses import FrozenInstanceError

import numpy as np
import pytest
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
from physkit.units import ComplexSparseMatrixQuantity, PhysicalUnit


def test_retains_complete_scalar_representation_with_immutable_storage() -> None:
    matrix = ComplexSparseMatrixQuantity.from_csr(
        sparse.identity(6, dtype=np.complex128, format="csr"),
        PhysicalUnit("electron_volt"),
    )
    shape = FiniteLatticeShape(LatticeDimension.TWO, (2, 3))
    twist_fiber = TwistFiber(
        BoundaryTwistReducer().execute(
            BoundaryTwistLift(LatticeDimension.TWO, (0.25, 0.5))
        ),
        TwistGaugeRepresentation.CENTERED_UNIFORM_LINK,
    )

    represented = ScalarFiniteLatticeOperator(
        "twisted_parent",
        matrix,
        shape,
        twist_fiber,
        "scalar_cell_basis",
        "parent_zero",
        (("model", "parent"), ("route", "uniform_link")),
    )

    assert represented.matrix is matrix
    assert represented.shape is shape
    assert represented.twist_fiber is twist_fiber
    assert represented.matrix.unit == PhysicalUnit("electron_volt")
    assert represented.provenance == (
        ("model", "parent"),
        ("route", "uniform_link"),
    )
    with pytest.raises(FrozenInstanceError):
        represented.identifier = "other"  # type: ignore[misc]
    with pytest.raises(ValueError):
        represented.matrix.data[0] = 2.0 + 0.0j

    exported = represented.matrix.to_csr()
    exported.data[0] = 3.0 + 0.0j
    assert represented.matrix.to_csr()[0, 0] == 1.0 + 0.0j


def test_rejects_matrix_shape_and_twist_dimension_drift() -> None:
    wrong_size = ComplexSparseMatrixQuantity.from_csr(
        sparse.identity(4, dtype=np.complex128, format="csr"),
        PhysicalUnit("electron_volt"),
    )
    valid_size = ComplexSparseMatrixQuantity.from_csr(
        sparse.identity(6, dtype=np.complex128, format="csr"),
        PhysicalUnit("electron_volt"),
    )
    shape = FiniteLatticeShape(LatticeDimension.TWO, (2, 3))
    two_dimensional_twist = TwistFiber(
        BoundaryTwistReducer().execute(
            BoundaryTwistLift(LatticeDimension.TWO, (0.0, 0.0))
        ),
        TwistGaugeRepresentation.QUOTIENT_SEAM,
    )

    with pytest.raises(ValueError, match="matrix shape"):
        ScalarFiniteLatticeOperator(
            "operator",
            wrong_size,
            shape,
            two_dimensional_twist,
            "basis",
            "zero",
            (),
        )

    one_dimensional_twist = TwistFiber(
        BoundaryTwistReducer().execute(
            BoundaryTwistLift(LatticeDimension.ONE, (0.0,))
        ),
        TwistGaugeRepresentation.QUOTIENT_SEAM,
    )
    with pytest.raises(ValueError, match="dimensions must agree"):
        ScalarFiniteLatticeOperator(
            "operator",
            valid_size,
            shape,
            one_dimensional_twist,
            "basis",
            "zero",
            (),
        )


def test_rejects_invalid_source_metadata() -> None:
    matrix = ComplexSparseMatrixQuantity.from_csr(
        sparse.identity(2, dtype=np.complex128, format="csr"),
        PhysicalUnit("electron_volt"),
    )
    shape = FiniteLatticeShape(LatticeDimension.ONE, (2,))
    twist = TwistFiber(
        BoundaryTwistReducer().execute(
            BoundaryTwistLift(LatticeDimension.ONE, (0.0,))
        ),
        TwistGaugeRepresentation.QUOTIENT_SEAM,
    )

    with pytest.raises(ValueError, match="sorted and unique"):
        ScalarFiniteLatticeOperator(
            "operator",
            matrix,
            shape,
            twist,
            "basis",
            "zero",
            (("route", "seam"), ("model", "parent")),
        )
    with pytest.raises(ValueError, match="sorted and unique"):
        ScalarFiniteLatticeOperator(
            "operator",
            matrix,
            shape,
            twist,
            "basis",
            "zero",
            (("model", "parent"), ("model", "other")),
        )
    with pytest.raises(ValueError, match="provenance value must be nonempty"):
        ScalarFiniteLatticeOperator(
            "operator",
            matrix,
            shape,
            twist,
            "basis",
            "zero",
            (("model", ""),),
        )
