"""Cartesian effective-mass tensors for periodic two-dimensional models."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from projectkoios.physkit.core.data import DataObject
from projectkoios.physkit.units import MatrixQuantity, UnitSystem


@dataclass(frozen=True, slots=True, eq=False, kw_only=True)
class CartesianEffectiveMassTensor2D(DataObject):
    """Represent a symmetric positive-definite Cartesian mass tensor."""

    tensor: MatrixQuantity
    unit_system: UnitSystem

    def __post_init__(self) -> None:
        """Check every effective-mass argument."""
        self._check_arg_tensor()
        self._check_arg_unit_system()

    def _check_arg_tensor(self) -> None:
        """Require a symmetric positive-definite two-dimensional mass matrix."""
        if not isinstance(self.tensor, MatrixQuantity):
            raise TypeError("tensor must be MatrixQuantity")
        if self.tensor.magnitude.shape != (2, 2):
            raise ValueError("tensor must have shape (2, 2)")
        if not np.array_equal(self.tensor.magnitude, self.tensor.magnitude.T):
            raise ValueError("tensor must be exactly symmetric")
        if np.any(np.linalg.eigvalsh(self.tensor.magnitude) <= 0.0):
            raise ValueError("tensor must be positive definite")

    def _check_arg_unit_system(self) -> None:
        """Require a physical coherent unit system matching the mass unit."""
        if type(self.unit_system) is not UnitSystem:
            raise TypeError("unit_system must be UnitSystem")
        if self.unit_system is UnitSystem.NONDIMENSIONAL:
            raise ValueError("unit_system must be physical")
        if self.tensor.unit != self.unit_system.mass_unit:
            raise ValueError("tensor must use the selected unit-system mass unit")
