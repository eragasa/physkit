"""Finite Fourier-series evaluators extracted from computational notebooks.

The initial evaluator represents the conventional odd square wave through a
finite sum of odd sine harmonics. Angles are dimensionless and expressed in
radians. This module owns reusable numerical evaluation; plotting and lesson
narrative remain with the corresponding notebook.
"""

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


@dataclass(frozen=True, slots=True)
class OddSquareWaveFourierSeriesEvaluator:
    r"""Evaluate a finite odd-harmonic approximation to a square wave.

    The represented approximation with ``term_count`` terms is

    .. math::

        S_M(x) = \frac{4}{\pi}\sum_{j=0}^{M-1}
        \frac{\sin((2j+1)x)}{2j+1}.

    Parameters
    ----------
    term_count
        Positive built-in integer number of odd harmonics. Boolean and NumPy
        integer values are rejected.

    Notes
    -----
    :meth:`execute` accepts only finite ``numpy.float64`` arrays. Values are
    dimensionless angles in radians. The output has the same shape and does not
    alias or mutate the input.
    """

    term_count: int

    def __post_init__(self) -> None:
        """Validate the finite-series truncation."""
        if type(self.term_count) is not int:
            raise TypeError("term_count must be a built-in integer")
        if self.term_count <= 0:
            raise ValueError("term_count must be positive")

    def execute(self, angles: NDArray[np.float64]) -> NDArray[np.float64]:
        """Return the finite square-wave series at ``angles``.

        Parameters
        ----------
        angles
            Exact NumPy ``float64`` array of finite dimensionless angles in
            radians. Arrays of any shape, including empty arrays, are accepted.

        Returns
        -------
        numpy.ndarray
            Newly allocated ``float64`` values with the same shape as
            ``angles``.

        Raises
        ------
        TypeError
            If ``angles`` is not an exact NumPy array with ``float64`` dtype.
        ValueError
            If any angle is NaN or infinite.
        """
        if type(angles) is not np.ndarray:
            raise TypeError("angles must be a NumPy array")
        if angles.dtype != np.dtype(np.float64):
            raise TypeError("angles must have float64 dtype")
        if not np.all(np.isfinite(angles)):
            raise ValueError("angles must contain only finite values")

        values = np.zeros_like(angles)
        for harmonic in range(1, 2 * self.term_count, 2):
            values += (4.0 / (np.pi * harmonic)) * np.sin(harmonic * angles)
        return values
