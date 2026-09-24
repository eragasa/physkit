"""Verification of partial unit-free real-symmetric eigensolution."""

import numpy as np
import pytest
from scipy import sparse

from physkit.numerics.eigenproblems.real_symmetric import (
    RealSymmetricEigenpairSolver,
)


def test_returns_lowest_ordered_sparse_states() -> None:
    operator = sparse.diags(
        [4.0, 1.0, 3.0, 2.0],
        offsets=0,
        format="csr",
    )

    result = RealSymmetricEigenpairSolver().execute_lowest(operator, 2)

    np.testing.assert_allclose(result.eigenvalues, [1.0, 2.0])
    assert result.eigenvectors.shape == (4, 2)
    for column in range(result.eigenvectors.shape[1]):
        vector = result.eigenvectors[:, column]
        pivot = int(np.argmax(np.abs(vector)))
        assert vector[pivot] >= 0.0


def test_validates_requested_count() -> None:
    operator = np.diag([1.0, 2.0])
    solver = RealSymmetricEigenpairSolver()

    with pytest.raises(TypeError, match="built-in int"):
        solver.execute_lowest(operator, True)
    with pytest.raises(ValueError, match="between one and all"):
        solver.execute_lowest(operator, 0)
    with pytest.raises(ValueError, match="between one and all"):
        solver.execute_lowest(operator, 3)
