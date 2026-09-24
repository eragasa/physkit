"""Verification of complex sparse matrix quantities."""

import numpy as np
from scipy import sparse

from physkit.units.quantities import (
    ComplexSparseMatrixQuantity,
    PhysicalUnit,
)


def test_preserves_immutable_finite_complex_values() -> None:
    values = np.array([[1.0 + 2.0j, 0.0], [0.0, -3.0j]])
    quantity = ComplexSparseMatrixQuantity.from_csr(
        sparse.csr_matrix(values),
        PhysicalUnit("joule"),
    )

    np.testing.assert_array_equal(quantity.to_dense().magnitude, values)
    assert not quantity.data.flags.writeable
