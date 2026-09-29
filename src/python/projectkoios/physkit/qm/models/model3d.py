"""Nominal base for three-dimensional quantum models."""

from abc import ABC
from typing import ClassVar, Literal

from projectkoios.physkit.qm.models.base import BaseQuantumModel


class BaseQuantumModel3D(BaseQuantumModel, ABC):
    """Base physical specification over three spatial coordinates.

    Attributes
    ----------
    dimension
        Fixed spatial dimensionality, equal to ``3``.
    """

    dimension: ClassVar[Literal[3]] = 3
