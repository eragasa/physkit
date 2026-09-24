"""Verification of unit-free real-symmetric eigenpair results."""

import numpy as np
import pytest

from physkit.numerics.eigenproblems.real_symmetric import (
    RealSymmetricEigenpairResult,
)


def test_owns_correlated_immutable_arrays() -> None:
    eigenvalues = np.array([1.0, 2.0])
    eigenvectors = np.eye(2)
    result = RealSymmetricEigenpairResult(eigenvalues, eigenvectors)
    eigenvalues[:] = 0.0
    eigenvectors[:] = 0.0

    np.testing.assert_array_equal(result.eigenvalues, [1.0, 2.0])
    np.testing.assert_array_equal(result.eigenvectors, np.eye(2))
    assert not result.eigenvalues.flags.writeable
    assert not result.eigenvectors.flags.writeable


def test_rejects_uncorrelated_dimensions() -> None:
    with pytest.raises(ValueError, match="match selected eigenvalues"):
        RealSymmetricEigenpairResult(
            np.array([1.0, 2.0]),
            np.ones((2, 1)),
        )
