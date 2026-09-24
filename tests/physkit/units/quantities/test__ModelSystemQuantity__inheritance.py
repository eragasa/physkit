"""Verification of nominal model-system quantity ownership."""

import pytest

from physkit.units.quantities import (
    ComplexMatrixQuantity,
    ComplexSparseMatrixQuantity,
    ComplexVectorQuantity,
    MatrixQuantity,
    ModelSystemQuantity,
    ScalarQuantity,
    SparseMatrixQuantity,
    VectorQuantity,
)


@pytest.mark.parametrize(
    "quantity_type",
    [
        ScalarQuantity,
        VectorQuantity,
        ComplexVectorQuantity,
        MatrixQuantity,
        ComplexMatrixQuantity,
        SparseMatrixQuantity,
        ComplexSparseMatrixQuantity,
    ],
)
def test_concrete_quantities_inherit_model_system_quantity(
    quantity_type: type,
) -> None:
    assert quantity_type.__bases__ == (ModelSystemQuantity,)
