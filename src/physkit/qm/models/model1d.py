# src/physkit/qm/models/model1d.py

from __future__ import annotations

from abc import ABC
from typing import ClassVar, Literal

from physkit.qm.models.base import QuantumModel


class QuantumModel1D(
    QuantumModel,
    ABC,
):
    """
    Base physical specification of a one-dimensional quantum system.

    A one-dimensional quantum model defines a continuous state space
    over one spatial coordinate. It does not define a numerical grid,
    discrete operator, or solution algorithm.
    """

    # Every model in this family has exactly one spatial dimension.
    dimension: ClassVar[Literal[1]] = 1
