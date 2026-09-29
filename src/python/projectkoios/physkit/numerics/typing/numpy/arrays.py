"""Precise NumPy array type aliases."""

from __future__ import annotations

import numpy as np
import numpy.typing as npt

type RealArray = npt.NDArray[np.float64]
type ComplexArray = npt.NDArray[np.complex128]
type IntegerArray = npt.NDArray[np.int64]
type RealVector = npt.NDArray[np.float64]
type RealMatrix = npt.NDArray[np.float64]
type ComplexVector = npt.NDArray[np.complex128]
type ComplexMatrix = npt.NDArray[np.complex128]
type IntegerVector = npt.NDArray[np.int64]
type IntegerMatrix = npt.NDArray[np.int64]
