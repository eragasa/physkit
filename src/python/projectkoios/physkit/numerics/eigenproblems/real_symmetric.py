"""Deterministic unit-free eigenanalysis for real-symmetric matrices.

Migrated from ``ksdft2effmass/operators/eigenpairs.py`` at donor commit
``7bd913151f7e61ed2bdba593df920be36573b502``.

This numerical boundary accepts and returns plain arrays. Model layers own units
and attach them only before and after numerical execution.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import numpy.typing as npt
from scipy import linalg, sparse
from scipy.sparse import linalg as sparse_linalg


type RealVector = npt.NDArray[np.float64]
type RealMatrix = npt.NDArray[np.float64]
type RealSymmetricOperator = RealMatrix | sparse.spmatrix | sparse.sparray


@dataclass(frozen=True, slots=True, eq=False)
class RealSymmetricEigenpairResult:
    """Retain immutable ordered unit-free eigenvalues and eigenvectors."""

    eigenvalues: RealVector
    eigenvectors: RealMatrix

    def __post_init__(self) -> None:
        if not isinstance(self.eigenvalues, np.ndarray):
            raise TypeError("eigenvalues must be a numpy.ndarray")
        if not isinstance(self.eigenvectors, np.ndarray):
            raise TypeError("eigenvectors must be a numpy.ndarray")
        if self.eigenvalues.dtype.kind not in "iuf":
            raise TypeError("eigenvalues must contain real numeric values")
        if self.eigenvectors.dtype.kind not in "iuf":
            raise TypeError("eigenvectors must contain real numeric values")
        eigenvalues = np.asarray(self.eigenvalues, dtype=np.float64)
        eigenvectors = np.asarray(self.eigenvectors, dtype=np.float64)
        if eigenvalues.ndim != 1 or not np.all(np.isfinite(eigenvalues)):
            raise ValueError("eigenvalues must be a finite vector")
        if eigenvectors.ndim != 2 or not np.all(np.isfinite(eigenvectors)):
            raise ValueError("eigenvectors must be a finite matrix")
        selected = eigenvalues.size
        if selected <= 0 or eigenvectors.shape[1] != selected:
            raise ValueError("eigenvectors must match selected eigenvalues")
        if eigenvectors.shape[0] < selected:
            raise ValueError("selected states must not exceed the dimension")
        immutable_values = np.frombuffer(
            eigenvalues.astype("<f8").tobytes(),
            dtype="<f8",
        )
        immutable_vectors = np.frombuffer(
            eigenvectors.astype("<f8").tobytes(),
            dtype="<f8",
        ).reshape(eigenvectors.shape)
        object.__setattr__(self, "eigenvalues", immutable_values)
        object.__setattr__(self, "eigenvectors", immutable_vectors)


class RealSymmetricEigenpairSolver:
    """Solve dense or sparse unit-free real-symmetric matrices.

    Complete sparse eigensystems are supported for tridiagonal matrices through
    :func:`scipy.linalg.eigh_tridiagonal`. Partial sparse eigensystems use
    :func:`scipy.sparse.linalg.eigsh`. Complete non-tridiagonal sparse matrices
    are rejected rather than silently materialized as dense.
    """

    __slots__ = ()

    def execute(
        self,
        operator: RealSymmetricOperator,
    ) -> RealSymmetricEigenpairResult:
        """Return the complete ascending eigensystem without densification."""
        dimension = self.validate(operator)
        if isinstance(operator, np.ndarray):
            matrix = np.asarray(operator, dtype=np.float64)
            eigenvalues, eigenvectors = np.linalg.eigh(matrix)
        else:
            matrix = self._as_csr(operator)
            diagonal = np.asarray(matrix.diagonal(), dtype=np.float64)
            off_diagonal = np.asarray(matrix.diagonal(1), dtype=np.float64)
            reconstructed = sparse.diags(
                (off_diagonal, diagonal, off_diagonal),
                offsets=(-1, 0, 1),
                shape=(dimension, dimension),
                format="csr",
                dtype=np.float64,
            )
            difference = matrix - reconstructed
            difference.eliminate_zeros()
            if difference.nnz != 0:
                raise ValueError(
                    "complete sparse eigensystems require a tridiagonal operator"
                )
            eigenvalues, eigenvectors = linalg.eigh_tridiagonal(
                diagonal,
                off_diagonal,
                check_finite=False,
                lapack_driver="auto",
            )
        return RealSymmetricEigenpairResult(
            eigenvalues=eigenvalues,
            eigenvectors=self.canonicalize_signs(eigenvectors),
        )

    def execute_lowest(
        self,
        operator: RealSymmetricOperator,
        count: int,
    ) -> RealSymmetricEigenpairResult:
        """Return the lowest ``count`` eigenpairs without densifying input."""
        dimension = self.validate(operator)
        if type(count) is not int:
            raise TypeError("count must be a built-in int")
        if count <= 0 or count > dimension:
            raise ValueError("count must select between one and all states")
        if count == dimension:
            return self.execute(operator)
        if isinstance(operator, np.ndarray):
            eigenvalues, eigenvectors = np.linalg.eigh(
                np.asarray(operator, dtype=np.float64)
            )
            selected_values = eigenvalues[:count]
            selected_vectors = eigenvectors[:, :count]
        else:
            selected_values, selected_vectors = sparse_linalg.eigsh(
                self._as_csr(operator),
                k=count,
                which="SA",
                v0=np.ones(dimension, dtype=np.float64),
            )
            order = np.argsort(selected_values)
            selected_values = selected_values[order]
            selected_vectors = selected_vectors[:, order]
        return RealSymmetricEigenpairResult(
            eigenvalues=selected_values,
            eigenvectors=self.canonicalize_signs(selected_vectors),
        )

    @classmethod
    def validate(cls, operator: RealSymmetricOperator) -> int:
        """Validate one unit-free real-symmetric matrix and return its dimension."""
        if isinstance(operator, np.ndarray):
            if operator.dtype.kind not in "iuf":
                raise TypeError("operator must contain real numeric values")
            matrix = np.asarray(operator, dtype=np.float64)
            if matrix.ndim != 2 or not np.all(np.isfinite(matrix)):
                raise ValueError("operator must be a finite matrix")
            rows, columns = matrix.shape
            if rows != columns:
                raise ValueError("operator must be square")
            if not np.array_equal(matrix, matrix.T):
                raise ValueError("operator must be exactly real symmetric")
            return rows
        if not sparse.issparse(operator):
            raise TypeError("operator must be a NumPy or SciPy sparse matrix")
        matrix = cls._as_csr(operator)
        rows, columns = matrix.shape
        if rows != columns:
            raise ValueError("operator must be square")
        difference = matrix - matrix.transpose()
        difference.eliminate_zeros()
        if difference.nnz != 0:
            raise ValueError("operator must be exactly real symmetric")
        return int(rows)

    @staticmethod
    def _as_csr(
        operator: sparse.spmatrix | sparse.sparray,
    ) -> sparse.csr_array:
        if operator.dtype.kind not in "iuf":
            raise TypeError("operator must contain real numeric values")
        matrix = sparse.csr_array(operator, dtype=np.float64)
        matrix.sum_duplicates()
        matrix.eliminate_zeros()
        matrix.sort_indices()
        if not np.all(np.isfinite(matrix.data)):
            raise ValueError("operator must contain finite values")
        return matrix

    @staticmethod
    def canonicalize_signs(eigenvectors: RealMatrix) -> RealMatrix:
        """Choose deterministic signs using each vector's largest entry."""
        canonical = np.asarray(eigenvectors, dtype=np.float64).copy()
        for column in range(canonical.shape[1]):
            vector = canonical[:, column]
            pivot = int(np.argmax(np.abs(vector)))
            if vector[pivot] < 0.0:
                canonical[:, column] *= -1.0
        return canonical
