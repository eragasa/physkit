"""Analytical spectral time evolution for the one-dimensional particle in a box."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from physkit.core.results import ResultsObject
from physkit.units import (
    MODEL_SYSTEM_UNIT_CONVERTER,
    ComplexMatrixQuantity,
    ComplexVectorQuantity,
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)

from ..base import Piab1D
from ..tise_analytical import Piab1DAnalyticalResults


def _selected_times(model: Piab1D, times: VectorQuantity) -> VectorQuantity:
    if not isinstance(times, VectorQuantity):
        raise TypeError("times must be VectorQuantity")
    selected = MODEL_SYSTEM_UNIT_CONVERTER.convert_vector(
        times,
        model.unit_system.time_unit,
    )
    values = selected.magnitude
    if values.size == 0:
        raise ValueError("times must be nonempty")
    if values[0] != 0.0:
        raise ValueError("times must begin at zero")
    if np.any(values[1:] < values[:-1]):
        raise ValueError("times must be nondecreasing")
    return selected


@dataclass(frozen=True, slots=True, eq=False)
class Piab1dTdseAnalyticalResults(ResultsObject):
    """Retain one analytical PIAB1D spectral time evolution."""

    tise_results: Piab1DAnalyticalResults
    initial_coefficients: ComplexVectorQuantity
    times: VectorQuantity
    coefficients: ComplexMatrixQuantity

    def __post_init__(self) -> None:
        if not isinstance(self.tise_results, Piab1DAnalyticalResults):
            raise TypeError("tise_results must be Piab1DAnalyticalResults")
        if not isinstance(self.initial_coefficients, ComplexVectorQuantity):
            raise TypeError(
                "initial_coefficients must be ComplexVectorQuantity"
            )
        if not isinstance(self.times, VectorQuantity):
            raise TypeError("times must be VectorQuantity")
        if not isinstance(self.coefficients, ComplexMatrixQuantity):
            raise TypeError("coefficients must be ComplexMatrixQuantity")
        if not isinstance(self.initial_coefficients.unit, Unitless):
            raise ValueError("initial_coefficients must be unitless")
        if not isinstance(self.coefficients.unit, Unitless):
            raise ValueError("coefficients must be unitless")
        model = self.tise_results.model
        if self.times.unit != model.unit_system.time_unit:
            raise ValueError("times must use the model time unit")
        if self.times.magnitude.size == 0:
            raise ValueError("times must be nonempty")
        if self.times.magnitude[0] != 0.0:
            raise ValueError("times must begin at zero")
        if np.any(self.times.magnitude[1:] < self.times.magnitude[:-1]):
            raise ValueError("times must be nondecreasing")
        mode_count = self.tise_results.quantum_numbers.size
        if self.initial_coefficients.magnitude.shape != (mode_count,):
            raise ValueError("initial_coefficients must match the TISE modes")
        if self.coefficients.magnitude.shape != (
            mode_count,
            self.times.magnitude.size,
        ):
            raise ValueError("coefficients must match modes and times")
        tolerance = 64.0 * np.finfo(np.float64).eps
        if not np.isclose(
            np.vdot(
                self.initial_coefficients.magnitude,
                self.initial_coefficients.magnitude,
            ).real,
            1.0,
            rtol=tolerance,
            atol=tolerance,
        ):
            raise ValueError("initial_coefficients must be normalized")
        if not np.allclose(
            self.coefficients.magnitude[:, 0],
            self.initial_coefficients.magnitude,
            rtol=tolerance,
            atol=tolerance,
        ):
            raise ValueError("coefficients at time zero must equal the initial state")

    @property
    def model(self) -> Piab1D:
        """Return the represented physical model."""
        return self.tise_results.model

    @property
    def norms(self) -> VectorQuantity:
        """Return the spectral norm at every represented time."""
        values = np.sum(np.abs(self.coefficients.magnitude) ** 2, axis=0)
        return VectorQuantity(values, Unitless())

    @property
    def energy_expectation(self) -> ScalarQuantity:
        """Return the conserved energy expectation value."""
        weights = np.abs(self.initial_coefficients.magnitude) ** 2
        value = float(weights @ self.tise_results.energies.magnitude)
        return ScalarQuantity(value, self.model.unit_system.energy_unit)

    def wavefunctions(
        self,
        coordinates: VectorQuantity,
    ) -> ComplexMatrixQuantity:
        """Evaluate continuum wavefunctions at coordinates and represented times."""
        if not isinstance(coordinates, VectorQuantity):
            raise TypeError("coordinates must be VectorQuantity")
        selected = MODEL_SYSTEM_UNIT_CONVERTER.convert_vector(
            coordinates,
            self.model.unit_system.length_unit,
        )
        length = self.model.length_quantity.magnitude
        if np.any(selected.magnitude < 0.0) or np.any(
            selected.magnitude > length
        ):
            raise ValueError("coordinates must lie in the closed box interval")
        quantum_numbers = self.tise_results.quantum_numbers.astype(np.float64)
        basis = np.sqrt(2.0 / length) * np.sin(
            np.pi
            * np.outer(selected.magnitude / length, quantum_numbers)
        )
        values = basis @ self.coefficients.magnitude
        length_unit = self.model.unit_system.length_unit
        if isinstance(length_unit, Unitless):
            wavefunction_unit: PhysicalUnit | Unitless = Unitless()
        else:
            if not isinstance(length_unit, PhysicalUnit):
                raise TypeError("physical model requires a physical length unit")
            wavefunction_unit = PhysicalUnit(
                f"({length_unit.expression}) ** -0.5"
            )
        return ComplexMatrixQuantity(values, wavefunction_unit)


class Piab1dTdseAnalyticalSolver:
    """Propagate a finite analytical PIAB1D eigenbasis exactly in time."""

    def solve(
        self,
        tise_results: Piab1DAnalyticalResults,
        initial_coefficients: ComplexVectorQuantity,
        times: VectorQuantity,
    ) -> Piab1dTdseAnalyticalResults:
        """Return exact phase evolution in the represented continuum basis."""
        if not isinstance(tise_results, Piab1DAnalyticalResults):
            raise TypeError("tise_results must be Piab1DAnalyticalResults")
        if not isinstance(initial_coefficients, ComplexVectorQuantity):
            raise TypeError(
                "initial_coefficients must be ComplexVectorQuantity"
            )
        if not isinstance(initial_coefficients.unit, Unitless):
            raise ValueError("initial_coefficients must be unitless")
        mode_count = tise_results.quantum_numbers.size
        if initial_coefficients.magnitude.shape != (mode_count,):
            raise ValueError("initial_coefficients must match the TISE modes")
        tolerance = 64.0 * np.finfo(np.float64).eps
        norm = np.vdot(
            initial_coefficients.magnitude,
            initial_coefficients.magnitude,
        ).real
        if not np.isclose(norm, 1.0, rtol=tolerance, atol=tolerance):
            raise ValueError("initial_coefficients must be normalized")
        selected_times = _selected_times(tise_results.model, times)
        phases = np.exp(
            -1.0j
            * np.outer(
                tise_results.energies.magnitude,
                selected_times.magnitude,
            )
            / tise_results.model.hbar_quantity.magnitude
        )
        coefficients = initial_coefficients.magnitude[:, np.newaxis] * phases
        return Piab1dTdseAnalyticalResults(
            tise_results=tise_results,
            initial_coefficients=initial_coefficients,
            times=selected_times,
            coefficients=ComplexMatrixQuantity(coefficients, Unitless()),
        )
