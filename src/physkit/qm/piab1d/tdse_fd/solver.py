"""Spectral time evolution of the finite-difference PIAB1D Hamiltonian."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from physkit.core.results import ResultsObject
from physkit.units import (
    MODEL_SYSTEM_UNIT_CONVERTER,
    ComplexMatrixQuantity,
    ComplexVectorQuantity,
    MatrixQuantity,
    PhysicalUnit,
    Unitless,
    VectorQuantity,
)

from ..base import Piab1D
from ..tise_fd import Piab1dTiseFdResults


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
class Piab1dTdseFdResults(ResultsObject):
    """Retain one unitary evolution of a finite-difference PIAB1D state."""

    tise_results: Piab1dTiseFdResults
    initial_state: ComplexVectorQuantity
    times: VectorQuantity
    states: ComplexMatrixQuantity

    def __post_init__(self) -> None:
        if not isinstance(self.tise_results, Piab1dTiseFdResults):
            raise TypeError("tise_results must be Piab1dTiseFdResults")
        if not isinstance(self.initial_state, ComplexVectorQuantity):
            raise TypeError("initial_state must be ComplexVectorQuantity")
        if not isinstance(self.times, VectorQuantity):
            raise TypeError("times must be VectorQuantity")
        if not isinstance(self.states, ComplexMatrixQuantity):
            raise TypeError("states must be ComplexMatrixQuantity")
        if not isinstance(self.initial_state.unit, Unitless):
            raise ValueError("initial_state must contain unitless amplitudes")
        if not isinstance(self.states.unit, Unitless):
            raise ValueError("states must contain unitless amplitudes")
        if self.times.unit != self.model.unit_system.time_unit:
            raise ValueError("times must use the model time unit")
        if self.times.magnitude.size == 0:
            raise ValueError("times must be nonempty")
        if self.times.magnitude[0] != 0.0:
            raise ValueError("times must begin at zero")
        if np.any(self.times.magnitude[1:] < self.times.magnitude[:-1]):
            raise ValueError("times must be nondecreasing")
        points = self.tise_results.interior_points
        if self.initial_state.magnitude.shape != (points,):
            raise ValueError("initial_state must match the interior grid")
        if self.states.magnitude.shape != (
            points,
            self.times.magnitude.size,
        ):
            raise ValueError("states must match interior points and times")
        tolerance = 128.0 * np.finfo(np.float64).eps
        norm = np.vdot(
            self.initial_state.magnitude,
            self.initial_state.magnitude,
        ).real
        if not np.isclose(norm, 1.0, rtol=tolerance, atol=tolerance):
            raise ValueError("initial_state must be normalized")
        if not np.allclose(
            self.states.magnitude[:, 0],
            self.initial_state.magnitude,
            rtol=tolerance,
            atol=tolerance,
        ):
            raise ValueError("states at time zero must equal the initial state")

    @property
    def model(self) -> Piab1D:
        """Return the represented physical model."""
        return self.tise_results.model

    @property
    def probabilities(self) -> MatrixQuantity:
        """Return coordinate-basis probabilities at every represented time."""
        return MatrixQuantity(np.abs(self.states.magnitude) ** 2, Unitless())

    @property
    def norms(self) -> VectorQuantity:
        """Return the state norm at every represented time."""
        values = np.sum(np.abs(self.states.magnitude) ** 2, axis=0)
        return VectorQuantity(values, Unitless())

    @property
    def energy_expectations(self) -> VectorQuantity:
        """Return the energy expectation at every represented time."""
        hamiltonian = self.tise_results.hamiltonian.to_csr()
        values = np.empty(self.times.magnitude.size, dtype=np.float64)
        for index, state in enumerate(self.states.magnitude.T):
            values[index] = float(np.vdot(state, hamiltonian @ state).real)
        return VectorQuantity(values, self.model.unit_system.energy_unit)

    @property
    def sampled_wavefunctions(self) -> ComplexMatrixQuantity:
        """Return grid samples normalized with the physical spacing measure."""
        spacing = self.tise_results.grid_spacing
        values = self.states.magnitude / np.sqrt(spacing.magnitude)
        if isinstance(spacing.unit, Unitless):
            wavefunction_unit: PhysicalUnit | Unitless = Unitless()
        else:
            if not isinstance(spacing.unit, PhysicalUnit):
                raise TypeError("physical model requires a physical length unit")
            wavefunction_unit = PhysicalUnit(
                f"({spacing.unit.expression}) ** -0.5"
            )
        return ComplexMatrixQuantity(values, wavefunction_unit)


class Piab1dTdseFdSolver:
    """Propagate the complete finite-difference eigensystem exactly in time."""

    def solve(
        self,
        tise_results: Piab1dTiseFdResults,
        initial_state: ComplexVectorQuantity,
        times: VectorQuantity,
    ) -> Piab1dTdseFdResults:
        """Return unitary spectral evolution in the interior coordinate basis."""
        if not isinstance(tise_results, Piab1dTiseFdResults):
            raise TypeError("tise_results must be Piab1dTiseFdResults")
        if not isinstance(initial_state, ComplexVectorQuantity):
            raise TypeError("initial_state must be ComplexVectorQuantity")
        if not isinstance(initial_state.unit, Unitless):
            raise ValueError("initial_state must contain unitless amplitudes")
        points = tise_results.interior_points
        if initial_state.magnitude.shape != (points,):
            raise ValueError("initial_state must match the interior grid")
        tolerance = 128.0 * np.finfo(np.float64).eps
        norm = np.vdot(
            initial_state.magnitude,
            initial_state.magnitude,
        ).real
        if not np.isclose(norm, 1.0, rtol=tolerance, atol=tolerance):
            raise ValueError("initial_state must be normalized")
        selected_times = _selected_times(tise_results.model, times)
        eigenvectors = tise_results.eigenvectors.magnitude
        spectral_coefficients = eigenvectors.T.conj() @ initial_state.magnitude
        phases = np.exp(
            -1.0j
            * np.outer(
                tise_results.energies.magnitude,
                selected_times.magnitude,
            )
            / tise_results.model.hbar_quantity.magnitude
        )
        states = eigenvectors @ (
            spectral_coefficients[:, np.newaxis] * phases
        )
        return Piab1dTdseFdResults(
            tise_results=tise_results,
            initial_state=initial_state,
            times=selected_times,
            states=ComplexMatrixQuantity(states, Unitless()),
        )
