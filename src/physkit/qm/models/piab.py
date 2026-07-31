# src/physkit/qm/models/piab.py

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from physkit.qm.models.base import QuantumModel
from physkit.qm.models.base import QuantumResult
from physkit.qm.models.base import QuantumSolver


class Piab(
    QuantumModel,
    ABC,
):
    """
    Base physical specification of a particle-in-a-box model.

    This class identifies the physical model family. Dimensional
    geometry and particle parameters are defined by subclasses.
    """

    # Piab1D, Piab2D, and Piab3D inherit from this class.
    pass


class PiabResult(
    QuantumResult,
    ABC,
):
    """
    Base result produced by a particle-in-a-box solver.
    """

    # Dimension-specific PIAB result classes inherit from this class.
    pass


# This placeholder represents the exact PIAB result returned by a
# particular PIAB solver.
PiabResultType = TypeVar(
    "PiabResultType",
    bound=PiabResult,
    covariant=True,
)


class PiabSolver(
    QuantumSolver[PiabResultType],
    Generic[PiabResultType],
    ABC,
):
    """
    Base interface for a particle-in-a-box solver.
    """

    # The solve() method is inherited from QuantumSolver.
    pass
