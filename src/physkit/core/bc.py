# physkit/core/bc.py
# Eugene Joseph M. Ragasa
from __future__ import annotations

from enum import Enum
import numpy as np


class BCType(Enum):
    """
    Boundary condition type for structured finite-difference grids.
    """

    DIRICHLET = "dirichlet"
    NEUMANN = "neumann"
    ROBIN = "robin"
    PERIODIC = "periodic"
    BLOCH = "bloch"


class BoundaryCondition:
    """
    Base class for boundary condition objects.
    """

    def __init__(self) -> None:
        self.type: BCType | None = None


class DirichletBC(BoundaryCondition):
    """
    Dirichlet boundary condition.

    Specifies the value of the field at a boundary:

        u = value
    """

    def __init__(self, value: float = 0.0) -> None:
        super().__init__()

        self.value: float = value
        self.type: BCType = BCType.DIRICHLET

        self.check_args()

    def check_args(self) -> None:
        if not np.isfinite(self.value):
            raise ValueError("DirichletBC value must be finite.")

    def __repr__(self) -> str:
        return f"DirichletBC(value={self.value})"


class NeumannBC(BoundaryCondition):
    """
    Neumann boundary condition.

    Specifies the normal derivative of the field at a boundary:

        du/dn = value
    """

    def __init__(self, value: float = 0.0) -> None:
        super().__init__()

        self.value: float = value
        self.type: BCType = BCType.NEUMANN

        self.check_args()

    def check_args(self) -> None:
        if not np.isfinite(self.value):
            raise ValueError("NeumannBC value must be finite.")

    def __repr__(self) -> str:
        return f"NeumannBC(value={self.value})"

class RobinBC(BoundaryCondition):
    """
    Robin boundary condition.

    Specifies a linear relation between the field and its normal derivative:

        alpha * u + beta * du/dn = value
    """

    def __init__(
        self,
        alpha: complex,
        beta: complex,
        value: complex = 0.0,
    ) -> None:
        super().__init__()

        self.alpha: complex = alpha
        self.beta: complex = beta
        self.value: complex = value
        self.type: BCType = BCType.ROBIN

        self.check_args()

    def check_args(self) -> None:
        if not np.isfinite(self.alpha):
            raise ValueError("alpha must be finite.")

        if not np.isfinite(self.beta):
            raise ValueError("beta must be finite.")

        if not np.isfinite(self.value):
            raise ValueError("value must be finite.")

        if self.alpha == 0 and self.beta == 0:
            raise ValueError("alpha and beta cannot both be zero.")

    def __repr__(self) -> str:
        return (
            "RobinBC("
            f"alpha={self.alpha}, "
            f"beta={self.beta}, "
            f"value={self.value})"
        )

class PeriodicBC(BoundaryCondition):
    """
    Periodic boundary condition.

    Identifies opposite boundaries:

        u(x + L) = u(x)

    This is a paired boundary condition. It connects the minimum and maximum
    sides of a coordinate direction.
    """

    def __init__(self) -> None:
        super().__init__()

        self.type: BCType = BCType.PERIODIC

    def __repr__(self) -> str:
        return "PeriodicBC()"


class BlochBC(BoundaryCondition):
    """
    Bloch boundary condition.

    Identifies opposite boundaries up to a phase:

        u(x + L) = exp(i k L) u(x)

    This is a paired boundary condition. It connects the minimum and maximum
    sides of a coordinate direction.
    """

    def __init__(self, k: float) -> None:
        super().__init__()

        self.k: float = k
        self.type: BCType = BCType.BLOCH

        self.check_args()

    def check_args(self) -> None:
        if not np.isfinite(self.k):
            raise ValueError("k must be finite.")

    def __repr__(self) -> str:
        return f"BlochBC(k={self.k})"
