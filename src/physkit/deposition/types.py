from __future__ import annotations
from typing import Union
import numpy as np

ArrayLike = Union[float, np.ndarray]

def asarray_f(x: ArrayLike) -> np.ndarray:
    return np.asarray(x, dtype=float)

