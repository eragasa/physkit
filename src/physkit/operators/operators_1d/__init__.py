"""Generic unit-aware one-dimensional matrix operators."""

from .fd import (
    SecondOrderCentralDifferenceLaplacian1D,
    UnitAwareMatrixOperator,
)

__all__ = [
    "SecondOrderCentralDifferenceLaplacian1D",
    "UnitAwareMatrixOperator",
]
