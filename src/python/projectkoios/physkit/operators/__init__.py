"""Public immutable operator hierarchy for the accepted 1D foundation.

The namespace exposes the minimal semantic operator interface, its discrete
CSR specialization, and the centered homogeneous-Dirichlet Laplacian.  It
introduces no composition, physical operator, or symbolic infrastructure.
"""

from .base import LinearOperator
from .discrete_1d import DiscreteLinearOperator1D
from .finite_difference_1d import FiniteDifferenceLaplacian1D

__all__ = [
    "LinearOperator",
    "DiscreteLinearOperator1D",
    "FiniteDifferenceLaplacian1D",
]
