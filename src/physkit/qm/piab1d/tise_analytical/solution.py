"""Closed-form energy solution for the one-dimensional particle in a box.

The energy formula and mode ordering are adapted from
``ksdft2effmass/analysis/model_systems/particle_in_box/model.py`` at commit
``7bd913151f7e61ed2bdba593df920be36573b502``.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import numpy.typing as npt

from physkit.core.results import ResultsObject
from physkit.units import (
    MODEL_SYSTEM_UNIT_CONVERTER,
    PhysicalUnit,
    Unitless,
    VectorQuantity,
)

from ..base import Piab1D


type IntegerVector = npt.NDArray[np.int64]


@dataclass(frozen=True, slots=True, eq=False)
class Piab1DAnalyticalResults(ResultsObject):
    """Retain one model and its ordered closed-form energy levels."""

    model: Piab1D
    quantum_numbers: IntegerVector
    energies: VectorQuantity

    def __post_init__(self) -> None:
        if not isinstance(self.model, Piab1D):
            raise TypeError("model must be Piab1D")
        if not isinstance(self.quantum_numbers, np.ndarray):
            raise TypeError("quantum_numbers must be a numpy.ndarray")
        values = np.asarray(self.quantum_numbers)
        if values.ndim != 1 or values.dtype.kind not in "iu":
            raise ValueError("quantum_numbers must be an integer vector")
        expected = np.arange(1, values.size + 1, dtype=np.int64)
        if values.size == 0 or not np.array_equal(values, expected):
            raise ValueError(
                "quantum_numbers must be consecutive positive integers"
            )
        if not isinstance(self.energies, VectorQuantity):
            raise TypeError("energies must be VectorQuantity")
        if self.energies.magnitude.shape != values.shape:
            raise ValueError("energies must match quantum_numbers")
        if self.energies.unit != self.model.unit_system.energy_unit:
            raise ValueError("energies must use the model energy unit")
        immutable = np.frombuffer(
            values.astype("<i8").tobytes(),
            dtype="<i8",
        )
        object.__setattr__(self, "quantum_numbers", immutable)


@dataclass(frozen=True, slots=True)
class Piab1DAnalyticalSolution:
    """Evaluate the known continuum energy spectrum of one ``Piab1D``."""

    model: Piab1D

    def __post_init__(self) -> None:
        if not isinstance(self.model, Piab1D):
            raise TypeError("model must be Piab1D")

    def evaluate(self, count: int) -> Piab1DAnalyticalResults:
        """Return the first ``count`` closed-form energy levels."""
        if type(count) is not int:
            raise TypeError("count must be a built-in int")
        if count <= 0:
            raise ValueError("count must be positive")
        quantum_numbers = np.arange(1, count + 1, dtype=np.int64)
        indices = quantum_numbers.astype(np.float64)
        hbar = self.model.hbar_quantity
        mass = self.model.mass_quantity
        length = self.model.length_quantity
        energies = (
            hbar.magnitude**2
            * np.pi**2
            * indices**2
            / (2.0 * mass.magnitude * length.magnitude**2)
        )
        if isinstance(self.model.unit_system.energy_unit, Unitless):
            energy_unit: PhysicalUnit | Unitless = Unitless()
        else:
            if not isinstance(hbar.unit, PhysicalUnit):
                raise TypeError("physical model requires physical action units")
            if not isinstance(mass.unit, PhysicalUnit):
                raise TypeError("physical model requires physical mass units")
            if not isinstance(length.unit, PhysicalUnit):
                raise TypeError("physical model requires physical length units")
            source_unit = PhysicalUnit(
                f"({hbar.unit.expression}) ** 2 / "
                f"({mass.unit.expression}) / "
                f"({length.unit.expression}) ** 2"
            )
            energy_unit = self.model.unit_system.energy_unit
            energies *= MODEL_SYSTEM_UNIT_CONVERTER.conversion_factor(
                source_unit,
                energy_unit,
            )
        return Piab1DAnalyticalResults(
            model=self.model,
            quantum_numbers=quantum_numbers,
            energies=VectorQuantity(energies, energy_unit),
        )
