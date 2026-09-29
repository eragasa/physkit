"""Sparse Kronecker sums for separable two- and three-axis representations."""

from __future__ import annotations

import math

import numpy as np
from scipy import sparse

from projectkoios.physkit.numerics.typing.scipy.sparse import SparseMatrix


class SparseKroneckerSumConstructor:
    r"""Construct a canonical sparse Kronecker sum in C-order convention.

    For square axis operators ``A_0, ..., A_{d-1}``, with ``d`` equal to two
    or three, the represented operator is

    .. math::

        A_0\otimes I\otimes\cdots
        + I\otimes A_1\otimes\cdots
        + \cdots
        + I\otimes\cdots\otimes A_{d-1}.

    Array states use shape ``(n_0, ..., n_{d-1})`` and C-order flattening, so
    the last axis varies fastest. This constructor owns numerical assembly only:
    callers retain boundary conditions, units, state-space meaning, and physical
    interpretation.
    """

    __slots__ = ()

    def execute(self, axis_operators: tuple[SparseMatrix, ...]) -> sparse.csr_array:
        """Return the canonical CSR Kronecker sum of two or three operators.

        Parameters
        ----------
        axis_operators:
            Ordered tuple of finite numeric square SciPy sparse matrices or
            arrays. Tuple order is array-axis order.

        Returns
        -------
        scipy.sparse.csr_array
            Owned canonical sparse representation of the Kronecker sum.

        Raises
        ------
        TypeError
            If the container or any operator has an unsupported type or dtype.
        ValueError
            If the operator count, shape, or stored values are invalid.
        """
        if type(axis_operators) is not tuple:
            raise TypeError("axis_operators must be a tuple")
        if len(axis_operators) not in (2, 3):
            raise ValueError("axis_operators must contain two or three operators")

        canonical_operators: list[sparse.csr_array] = []
        for operator in axis_operators:
            if not isinstance(operator, sparse.spmatrix | sparse.sparray):
                raise TypeError("each axis operator must be a SciPy sparse matrix")
            if operator.dtype.kind not in "iufc":
                raise TypeError(
                    "axis operators must contain numeric values excluding booleans"
                )
            rows, columns = operator.shape
            if rows != columns or rows < 1:
                raise ValueError("each axis operator must be nonempty and square")
            canonical = sparse.csr_array(operator, copy=True)
            canonical.sum_duplicates()
            canonical.eliminate_zeros()
            canonical.sort_indices()
            if not np.all(np.isfinite(canonical.data)):
                raise ValueError("axis operators must contain finite values")
            canonical_operators.append(canonical)

        result_dtype = np.dtype(
            np.result_type(*(operator.dtype for operator in canonical_operators))
        )
        axis_sizes = tuple(int(operator.shape[0]) for operator in canonical_operators)
        state_size = math.prod(axis_sizes)
        result = sparse.csr_array(
            (state_size, state_size),
            dtype=result_dtype,
        )

        for active_axis, active_operator in enumerate(canonical_operators):
            term = sparse.csr_array([[1]], dtype=result_dtype)
            for axis, axis_size in enumerate(axis_sizes):
                factor = (
                    active_operator.astype(result_dtype, copy=False)
                    if axis == active_axis
                    else sparse.identity(
                        axis_size,
                        dtype=result_dtype,
                        format="csr",
                    )
                )
                term = sparse.kron(term, factor, format="csr")
            result = result + term

        result.sum_duplicates()
        result.eliminate_zeros()
        result.sort_indices()
        if not np.all(np.isfinite(result.data)):
            raise ValueError("Kronecker sum must remain finite")
        return sparse.csr_array(result, dtype=result_dtype, copy=True)
