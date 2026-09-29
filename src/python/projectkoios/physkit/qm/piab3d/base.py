"""Unit-aware three-dimensional rectangular particle-in-a-box model."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from projectkoios.physkit.qm.models.model3d import BaseQuantumModel3D
from projectkoios.physkit.units import ScalarQuantity, UnitSystem


@dataclass(frozen=True, slots=True, kw_only=True)
class Piab3D(BaseQuantumModel3D):
    """Define a homogeneous-Dirichlet rectangular cuboid.

    The represented domain is
    ``[0, length_x] × [0, length_y] × [0, length_z]``. Construction is
    keyword-only. Length and mass magnitudes use ``unit_system``. All numerical
    parameters accept exactly built-in :class:`float`; booleans and numeric
    strings are rejected.
    """

    length_x: float
    length_y: float
    length_z: float
    mass: float
    unit_system: UnitSystem

    def __post_init__(self) -> None:
        """Check each cuboid box-model argument."""
        self._check_arg_length_x()
        self._check_arg_length_y()
        self._check_arg_length_z()
        self._check_arg_mass()
        self._check_arg_unit_system()

    def _check_arg_length_x(self) -> None:
        """Require a finite positive built-in floating-point x length."""
        if type(self.length_x) is not float:
            raise TypeError("length_x must be a built-in float")
        if not np.isfinite(self.length_x) or self.length_x <= 0.0:
            raise ValueError("length_x must be finite and positive")

    def _check_arg_length_y(self) -> None:
        """Require a finite positive built-in floating-point y length."""
        if type(self.length_y) is not float:
            raise TypeError("length_y must be a built-in float")
        if not np.isfinite(self.length_y) or self.length_y <= 0.0:
            raise ValueError("length_y must be finite and positive")

    def _check_arg_length_z(self) -> None:
        """Require a finite positive built-in floating-point z length."""
        if type(self.length_z) is not float:
            raise TypeError("length_z must be a built-in float")
        if not np.isfinite(self.length_z) or self.length_z <= 0.0:
            raise ValueError("length_z must be finite and positive")

    def _check_arg_mass(self) -> None:
        """Require a finite positive built-in floating-point particle mass."""
        if type(self.mass) is not float:
            raise TypeError("mass must be a built-in float")
        if not np.isfinite(self.mass) or self.mass <= 0.0:
            raise ValueError("mass must be finite and positive")

    def _check_arg_unit_system(self) -> None:
        """Require the coherent unit system used by every model parameter."""
        if type(self.unit_system) is not UnitSystem:
            raise TypeError("unit_system must be UnitSystem")

    @property
    def length_x_quantity(self) -> ScalarQuantity:
        """Return the first box length in the selected numerical scale."""
        return ScalarQuantity(
            magnitude=self.length_x,
            unit=self.unit_system.length_unit,
        )

    @property
    def length_y_quantity(self) -> ScalarQuantity:
        """Return the second box length in the selected numerical scale."""
        return ScalarQuantity(
            magnitude=self.length_y,
            unit=self.unit_system.length_unit,
        )

    @property
    def length_z_quantity(self) -> ScalarQuantity:
        """Return the third box length in the selected numerical scale."""
        return ScalarQuantity(
            magnitude=self.length_z,
            unit=self.unit_system.length_unit,
        )

    @property
    def mass_quantity(self) -> ScalarQuantity:
        """Return the particle mass in the selected numerical scale."""
        return ScalarQuantity(
            magnitude=self.mass,
            unit=self.unit_system.mass_unit,
        )

    @property
    def hbar_quantity(self) -> ScalarQuantity:
        """Return reduced Planck's constant in the selected action unit."""
        return self.unit_system.hbar
