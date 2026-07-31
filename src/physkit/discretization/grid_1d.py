# ./src/physkit/grid_1d.py

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto

import numpy as np


class ActiveSetType1D(Enum):
    """Active index sets on a full closed reference grid."""

    ALL = auto()
    INTERIOR = auto()
    LEFT_CLOSED = auto()
    RIGHT_CLOSED = auto()
    LEFT_BOUNDARY = auto()
    RIGHT_BOUNDARY = auto()
    BOUNDARY = auto()


@dataclass(frozen=True)
class Grid1D:
    """Uniform 1D reference grid on the closed interval [a,b].

    The full coordinate grid always includes both endpoints:

        x = np.linspace(a, b, N)

    The active set selects which grid points are used as degrees of freedom.
    """

    a: float
    b: float
    N: int
    active_type: ActiveSetType1D = ActiveSetType1D.ALL

    def __post_init__(self) -> None:
        if self.b <= self.a:
            raise ValueError("Require b > a.")

        if self.N < 2:
            raise ValueError("Require N >= 2.")

    @property
    def L(self) -> float:
        return self.b - self.a

    @property
    def dx(self) -> float:
        return self.L / (self.N - 1)

    @property
    def x(self) -> np.ndarray:
        return np.linspace(self.a, self.b, self.N)

    @property
    def active_indices(self) -> np.ndarray:
        if self.active_type is ActiveSetType1D.ALL:
            return np.arange(0, self.N)

        if self.active_type is ActiveSetType1D.INTERIOR:
            return np.arange(1, self.N - 1)

        if self.active_type is ActiveSetType1D.LEFT_CLOSED:
            return np.arange(0, self.N - 1)

        if self.active_type is ActiveSetType1D.RIGHT_CLOSED:
            return np.arange(1, self.N)

        if self.active_type is ActiveSetType1D.LEFT_BOUNDARY:
            return np.array([0])

        if self.active_type is ActiveSetType1D.RIGHT_BOUNDARY:
            return np.array([self.N - 1])

        if self.active_type is ActiveSetType1D.BOUNDARY:
            return np.array([0, self.N - 1])

        raise ValueError(f"Unknown active_type: {self.active_type}")

    @property
    def x_active(self) -> np.ndarray:
        return self.x[self.active_indices]
