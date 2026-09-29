"""Nominal base for two-dimensional quantum models."""

from abc import ABC
from typing import ClassVar, Literal

from projectkoios.physkit.qm.models.base import BaseQuantumModel


class BaseQuantumModel2D(BaseQuantumModel, ABC):
    """Base physical specification over two spatial coordinates.

    Attributes
    ----------
    dimension
        Fixed spatial dimensionality, equal to ``2``.
    """

    dimension: ClassVar[Literal[2]] = 2
