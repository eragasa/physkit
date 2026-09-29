r"""Equivalent-stress evaluators for symmetric continuum stress states.

The evaluators accept numerical stress tensors whose entries use one consistent,
caller-owned stress unit. They return von Mises equivalent stress in that same
unit. Small or large off-diagonal asymmetries are handled by the explicitly
preserved notebook convention of averaging each transposed pair before
calculation.
"""

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


@dataclass(frozen=True, slots=True)
class PlaneStressVonMisesEvaluator:
    r"""Evaluate von Mises equivalent stress under a plane-stress assumption.

    For in-plane normal stresses $\sigma_{xx}$ and $\sigma_{yy}$ and averaged
    shear stress $\tau_{xy}$, the represented formula is

    .. math::

        \sigma_{\mathrm{vM}} = \sqrt{
        \sigma_{xx}^2 - \sigma_{xx}\sigma_{yy} + \sigma_{yy}^2
        + 3\tau_{xy}^2}.

    The out-of-plane normal and shear stresses are assumed to be zero. Input and
    output use the same caller-owned stress unit.
    """

    def execute(self, stress_tensor: NDArray[np.float64]) -> float:
        """Return plane-stress von Mises equivalent stress.

        Parameters
        ----------
        stress_tensor
            Exact NumPy ``float64`` array with shape ``(2, 2)`` and finite
            entries. The off-diagonal entries are averaged before evaluation.

        Returns
        -------
        float
            Equivalent stress in the same unit as the tensor entries.

        Raises
        ------
        TypeError
            If the input is not an exact NumPy array with ``float64`` dtype.
        ValueError
            If the shape is not ``(2, 2)`` or any entry is nonfinite.

        Notes
        -----
        Arithmetic uses NumPy binary64 operations. Sufficiently large finite
        magnitudes can overflow or produce a nonfinite result with a NumPy warning.
        """
        if type(stress_tensor) is not np.ndarray:
            raise TypeError("stress_tensor must be a NumPy array")
        if stress_tensor.dtype != np.dtype(np.float64):
            raise TypeError("stress_tensor must have float64 dtype")
        if stress_tensor.shape != (2, 2):
            raise ValueError("stress_tensor must have shape (2, 2)")
        if not np.all(np.isfinite(stress_tensor)):
            raise ValueError("stress_tensor must contain only finite values")

        sigma_xx = stress_tensor[0, 0]
        sigma_yy = stress_tensor[1, 1]
        tau_xy = 0.5 * (stress_tensor[0, 1] + stress_tensor[1, 0])
        equivalent_stress = np.sqrt(
            sigma_xx**2 - sigma_xx * sigma_yy + sigma_yy**2 + 3.0 * tau_xy**2
        )
        return float(equivalent_stress)


@dataclass(frozen=True, slots=True)
class ThreeDimensionalVonMisesStressEvaluator:
    r"""Evaluate von Mises equivalent stress for a three-dimensional tensor.

    Each off-diagonal pair is averaged before the standard symmetric Cauchy
    stress formula is evaluated. Input and output use the same caller-owned
    stress unit.
    """

    def execute(self, stress_tensor: NDArray[np.float64]) -> float:
        """Return three-dimensional von Mises equivalent stress.

        Parameters
        ----------
        stress_tensor
            Exact NumPy ``float64`` array with shape ``(3, 3)`` and finite
            entries. Each off-diagonal pair is averaged before evaluation.

        Returns
        -------
        float
            Equivalent stress in the same unit as the tensor entries.

        Raises
        ------
        TypeError
            If the input is not an exact NumPy array with ``float64`` dtype.
        ValueError
            If the shape is not ``(3, 3)`` or any entry is nonfinite.

        Notes
        -----
        Arithmetic uses NumPy binary64 operations. Sufficiently large finite
        magnitudes can overflow or produce a nonfinite result with a NumPy warning.
        """
        if type(stress_tensor) is not np.ndarray:
            raise TypeError("stress_tensor must be a NumPy array")
        if stress_tensor.dtype != np.dtype(np.float64):
            raise TypeError("stress_tensor must have float64 dtype")
        if stress_tensor.shape != (3, 3):
            raise ValueError("stress_tensor must have shape (3, 3)")
        if not np.all(np.isfinite(stress_tensor)):
            raise ValueError("stress_tensor must contain only finite values")

        sigma_xx = stress_tensor[0, 0]
        sigma_yy = stress_tensor[1, 1]
        sigma_zz = stress_tensor[2, 2]
        tau_xy = 0.5 * (stress_tensor[0, 1] + stress_tensor[1, 0])
        tau_xz = 0.5 * (stress_tensor[0, 2] + stress_tensor[2, 0])
        tau_yz = 0.5 * (stress_tensor[1, 2] + stress_tensor[2, 1])
        equivalent_stress = np.sqrt(
            0.5
            * (
                (sigma_xx - sigma_yy) ** 2
                + (sigma_yy - sigma_zz) ** 2
                + (sigma_zz - sigma_xx) ** 2
            )
            + 3.0 * (tau_xy**2 + tau_yz**2 + tau_xz**2)
        )
        return float(equivalent_stress)
