"""Public one-dimensional discretization representations.

The legacy active-set grid and the accepted geometry/state-space-separated
uniform homogeneous-Dirichlet surface coexist without adapters or migration.
"""

from .grid_1d import ActiveSetType1D, Grid1D, UniformGrid1D
from .state_space_1d import HomogeneousDirichletStateSpace1D

__all__ = [
    "ActiveSetType1D",
    "Grid1D",
    "UniformGrid1D",
    "HomogeneousDirichletStateSpace1D",
]
