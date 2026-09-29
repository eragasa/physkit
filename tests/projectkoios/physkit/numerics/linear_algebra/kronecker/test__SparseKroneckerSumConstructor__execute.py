"""Tests for sparse separable Kronecker-sum assembly."""

import numpy as np
import pytest
from scipy import sparse

from projectkoios.physkit.numerics.linear_algebra.kronecker import (
    SparseKroneckerSumConstructor,
)


def test__SparseKroneckerSumConstructor__execute__uses_last_axis_fastest() -> None:
    first = sparse.diags((10.0, 20.0), format="csr")
    second = sparse.diags((1.0, 2.0, 3.0), format="csr")

    represented = SparseKroneckerSumConstructor().execute((first, second))

    np.testing.assert_allclose(
        represented.toarray(),
        np.diag((11.0, 12.0, 13.0, 21.0, 22.0, 23.0)),
    )
    assert isinstance(represented, sparse.csr_array)
    assert represented.has_canonical_format


def test__SparseKroneckerSumConstructor__execute__adds_real_axis_spectra() -> None:
    first = sparse.csr_array(np.array([[2.0, -1.0], [-1.0, 2.0]]))
    second = sparse.csr_array(
        np.array(
            [
                [2.0, -1.0, 0.0],
                [-1.0, 2.0, -1.0],
                [0.0, -1.0, 2.0],
            ]
        )
    )

    represented = SparseKroneckerSumConstructor().execute((first, second))
    expected = np.sort(
        (
            np.linalg.eigvalsh(first.toarray())[:, None]
            + np.linalg.eigvalsh(second.toarray())[None, :]
        ).ravel()
    )

    np.testing.assert_allclose(np.linalg.eigvalsh(represented.toarray()), expected)
    assert represented.dtype == np.dtype(np.float64)


def test__SparseKroneckerSumConstructor__execute__supports_complex_three_axis() -> None:
    first = sparse.csr_array(np.array([[2.0, -1.0j], [1.0j, 2.0]], dtype=np.complex128))
    second = sparse.csr_array(np.array([[1.0, 0.25], [0.25, 1.0]], dtype=np.complex128))
    third = sparse.diags(
        np.array([3.0, 4.0], dtype=np.complex128),
        format="csr",
    )

    represented = SparseKroneckerSumConstructor().execute((first, second, third))
    expected = np.sort(
        (
            np.linalg.eigvalsh(first.toarray())[:, None, None]
            + np.linalg.eigvalsh(second.toarray())[None, :, None]
            + np.linalg.eigvalsh(third.toarray())[None, None, :]
        ).ravel()
    )

    np.testing.assert_allclose(np.linalg.eigvalsh(represented.toarray()), expected)
    assert represented.shape == (8, 8)
    assert represented.dtype == np.dtype(np.complex128)


@pytest.mark.parametrize("operators", [(), (sparse.eye(2),), (sparse.eye(2),) * 4])
def test__SparseKroneckerSumConstructor__execute__requires_two_or_three_axes(
    operators: tuple[sparse.spmatrix, ...],
) -> None:
    with pytest.raises(ValueError, match="two or three"):
        SparseKroneckerSumConstructor().execute(operators)


def test__SparseKroneckerSumConstructor__execute__requires_tuple() -> None:
    with pytest.raises(TypeError, match="must be a tuple"):
        SparseKroneckerSumConstructor().execute(  # type: ignore[arg-type]
            [sparse.eye(2), sparse.eye(2)]
        )


@pytest.mark.parametrize(
    "operator",
    [
        np.eye(2),
        sparse.csr_array((0, 0)),
        sparse.csr_array((2, 3)),
    ],
)
def test__SparseKroneckerSumConstructor__execute__rejects_invalid_operator(
    operator: object,
) -> None:
    expected_error = TypeError if isinstance(operator, np.ndarray) else ValueError
    with pytest.raises(expected_error):
        SparseKroneckerSumConstructor().execute(  # type: ignore[arg-type]
            (operator, sparse.eye(2))
        )


@pytest.mark.parametrize(
    "values",
    [
        np.array([[np.iinfo(np.int64).min]], dtype=np.int64),
        np.array([[np.iinfo(np.int64).max]], dtype=np.int64),
        np.array([[np.iinfo(np.uint64).min]], dtype=np.uint64),
        np.array([[np.iinfo(np.uint64).max]], dtype=np.uint64),
        np.array([[True]], dtype=np.bool_),
    ],
)
def test__SparseKroneckerSumConstructor__execute__rejects_exact_dtypes(
    values: np.ndarray,
) -> None:
    exact_operator = sparse.csr_array(values)

    with pytest.raises(TypeError, match="floating-point or complex-floating"):
        SparseKroneckerSumConstructor().execute((exact_operator, sparse.eye(1)))


def test__SparseKroneckerSumConstructor__execute__rejects_nonfinite_values() -> None:
    invalid = sparse.csr_array(np.array([[np.nan, 0.0], [0.0, 1.0]]))

    with pytest.raises(ValueError, match="finite values"):
        SparseKroneckerSumConstructor().execute((invalid, sparse.eye(2)))


def test__SparseKroneckerSumConstructor__execute__rejects_overflowed_result() -> None:
    huge = sparse.csr_array([[np.finfo(np.float64).max]])

    with (
        np.errstate(over="ignore"),
        pytest.raises(
            ValueError,
            match="must remain finite",
        ),
    ):
        SparseKroneckerSumConstructor().execute((huge, huge))
