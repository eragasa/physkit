from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from .piab import Piab
from .piab import PiabResult
from .piab import PiabSolver


class Piab2D(Piab):
    """
    Physical specification of a two-dimensional particle in a box.
    """

    pass


class Piab2DResult(PiabResult):
    """
    Base result for a two-dimensional particle-in-a-box model.
    """

    pass


Piab2DResultT = TypeVar(
    "Piab2DResultT",
    bound=Piab2DResult,
)


class Piab2DSolver(
    PiabSolver[Piab2DResultT],
    Generic[Piab2DResultT],
    ABC,
):
    """
    Base solver for a two-dimensional particle-in-a-box model.
    """

    pass


class Piab2DAnalyticalResult(Piab2DResult):
    pass


class Piab2DAnalyticalSolver(
    Piab2DSolver[Piab2DAnalyticalResult],
):
    @property
    def result(self) -> Piab2DAnalyticalResult:
        raise NotImplementedError


class Piab2DNumericalResult(Piab2DResult):
    pass


class Piab2DNumericalSolver(
    Piab2DSolver[Piab2DNumericalResult],
):
    @property
    def result(self) -> Piab2DNumericalResult:
        raise NotImplementedError
