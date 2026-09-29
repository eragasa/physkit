"""Unit-aware one-dimensional particle-in-a-box model.

The represented ``[0, L]`` model and parameter invariants are adapted from
``ksdft2effmass/analysis/model_systems/particle_in_box/model.py`` at commit
``7bd913151f7e61ed2bdba593df920be36573b502``.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from projectkoios.physkit.qm.models.model1d import BaseQuantumModel1D
from projectkoios.physkit.units import ScalarQuantity, UnitSystem


@dataclass(frozen=True, slots=True, kw_only=True)
class Piab1D(BaseQuantumModel1D):
    """Define a homogeneous-Dirichlet box on ``[0, length]``.

    Construction is keyword-only. ``length`` and ``mass`` are numerical values
    in ``unit_system``. The
    selected unit system supplies their units, the represented energy unit,
    and reduced Planck's constant.
    """

    length: float
    mass: float
    unit_system: UnitSystem

    def __post_init__(self) -> None:
        """Check each one-dimensional box-model argument."""
        self._check_arg_length()
        self._check_arg_mass()
        self._check_arg_unit_system()

    def _check_arg_length(self) -> None:
        """Require a finite positive built-in floating-point box length."""
        if type(self.length) is not float:
            raise TypeError("length must be a built-in float")
        if not np.isfinite(self.length) or self.length <= 0.0:
            raise ValueError("length must be finite and positive")

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
    def length_quantity(self) -> ScalarQuantity:
        """Return the box length in the selected numerical scale."""
        return ScalarQuantity(
            magnitude=self.length,
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
