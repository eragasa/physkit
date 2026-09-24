"""Verification of ``SparseMatrixQuantity.from_csr``."""

import numpy as np
from scipy import sparse

from physkit.units.quantities import SparseMatrixQuantity, Unitless


def test_canonicalizes_and_returns_defensive_csr() -> None:
    source = sparse.coo_matrix(
        (
            np.array([1.0, 2.0, -1.0, 4.0]),
            (np.array([0, 0, 0, 1]), np.array([0, 0, 1, 1])),
        ),
        shape=(2, 2),
    )
    quantity = SparseMatrixQuantity.from_csr(source, Unitless())
    expected = np.array([[3.0, -1.0], [0.0, 4.0]])

    assert quantity.nonzero_count == 3
    np.testing.assert_array_equal(quantity.to_dense().magnitude, expected)
    first = quantity.to_csr()
    second = quantity.to_csr()
    assert not np.shares_memory(first.data, second.data)
    first.data[:] = 0.0
    np.testing.assert_array_equal(quantity.to_dense().magnitude, expected)
