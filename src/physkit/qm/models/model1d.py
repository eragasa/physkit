"""Nominal base for one-dimensional quantum models."""

from abc import ABC
from typing import ClassVar, Literal

from physkit.qm.models.base import BaseQuantumModel


class BaseQuantumModel1D(BaseQuantumModel, ABC):
    """Base physical specification over one spatial coordinate."""

    dimension: ClassVar[Literal[1]] = 1
