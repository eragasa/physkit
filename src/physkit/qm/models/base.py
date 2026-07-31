# src/physkit/qm/models/base.py

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar


class QuantumModel(ABC):
    """
    Base physical specification of a quantum-mechanical system.

    A model defines the physical system. It does not define its
    mathematical representation or solution method.
    """

    # Every physical quantum model inherits from this class.
    pass


class QuantumResult(ABC):
    """
    Base result produced by a quantum-mechanical solver.
    """

    # Specific result families inherit from this class.
    pass


# This placeholder represents the exact result type returned by a
# particular solver.
QuantumResultType = TypeVar(
    "QuantumResultType",
    bound=QuantumResult,
    covariant=True,
)


class QuantumSolver(
    ABC,
    Generic[QuantumResultType],
):
    """
    Base interface for a quantum-mechanical solver.
    """

    @abstractmethod
    def solve(self) -> QuantumResultType:
        """
        Solve the physical model and return the result.
        """

        # Each concrete solver supplies its own mathematics.
        raise NotImplementedError
