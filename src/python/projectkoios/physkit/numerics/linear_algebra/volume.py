"""Scale-invariant numerical volume calculations."""

from __future__ import annotations

import math

import numpy as np

from projectkoios.physkit.numerics.typing.numpy.arrays import RealMatrix


def normalized_column_volume(matrix: RealMatrix) -> float:
    r"""Return the absolute determinant after normalizing matrix columns.

    For a square matrix with nonzero columns :math:`\mathbf a_i`, this
    function computes the dimensionless quantity

    .. math::

        \left|\det\begin{bmatrix}
        \mathbf a_1/\lVert\mathbf a_1\rVert_2 & \cdots &
        \mathbf a_n/\lVert\mathbf a_n\rVert_2
        \end{bmatrix}\right|.

    The calculation pre-scales each column by its largest absolute component
    before taking its Euclidean norm. This is algebraically equivalent to
    direct normalization while avoiding intermediate underflow and overflow.
    A matrix containing a zero column has normalized column volume zero.

    Parameters
    ----------
    matrix:
        Nonempty finite square real matrix.

    Returns
    -------
    float
        Absolute determinant of the column-normalized matrix.

    Raises
    ------
    TypeError
        If ``matrix`` is not a NumPy array with real numeric values.
    ValueError
        If ``matrix`` is not finite, nonempty, and square.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if matrix.dtype.kind not in "iuf":
        raise TypeError("matrix must contain real numeric values")

    values = np.asarray(matrix, dtype=np.float64)
    if values.ndim != 2 or not np.all(np.isfinite(values)):
        raise ValueError("matrix must be finite and two-dimensional")
    rows, columns = values.shape
    if rows == 0 or rows != columns:
        raise ValueError("matrix must be nonempty and square")

    column_scales = np.max(np.abs(values), axis=0)
    if np.any(column_scales == 0.0):
        return 0.0

    scaled_values = values / column_scales
    column_norms = np.sqrt(np.sum(scaled_values * scaled_values, axis=0))
    normalized_columns = scaled_values / column_norms
    return abs(float(np.linalg.det(normalized_columns)))


def columns_are_linearly_independent(
    A: RealMatrix,
    *,
    norm_vol_atol: float,
) -> bool:
    """Return whether square-matrix columns are numerically independent.

    Independence is determined from the dimensionless normalized column
    volume. A volume at or below ``norm_vol_atol`` is treated as numerically
    dependent.

    Parameters
    ----------
    A:
        Nonempty finite square real matrix whose columns are checked.
    norm_vol_atol:
        Nonnegative finite absolute tolerance for normalized column volume.

    Returns
    -------
    bool
        Whether the matrix columns are numerically linearly independent.

    Raises
    ------
    TypeError
        If the tolerance is not exactly a built-in ``float``, or if ``A``
        fails :func:`normalized_column_volume` type validation.
    ValueError
        If the tolerance is negative or nonfinite, or if ``A`` fails
        :func:`normalized_column_volume` value validation.
    """
    if type(norm_vol_atol) is not float:
        raise TypeError("norm_vol_atol must be a built-in float")
    if not math.isfinite(norm_vol_atol) or norm_vol_atol < 0.0:
        raise ValueError("norm_vol_atol must be finite and nonnegative")

    normalized_volume = normalized_column_volume(A)
    return not math.isclose(
        normalized_volume,
        0.0,
        rel_tol=0.0,
        abs_tol=norm_vol_atol,
    )
