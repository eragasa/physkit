
from __future__ import annotations
import numpy as np

from ..types import ArrayLike, asarray_f

class PlanePointGeometry:
  @staticmethod
  def r(h_m: float, ell_m: ArrayLake) -> np.ndarray:
    ell = np.asarray(ell_m, dtype=float)
    return np.sqrt(h_m*h_m + ell*ell)

  @staticmethod
  def cos_theta(h_m: float,
                ell_m: ArrayLake
                ) -> np.ndarray:
    return h_m/PlanePointGeometry.r(h_m, ell_m)

