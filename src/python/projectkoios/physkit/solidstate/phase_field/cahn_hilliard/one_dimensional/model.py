r"""Dimensionless periodic one-dimensional Cahn--Hilliard evolution."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from projectkoios.physkit.core.actions import ActionizedDataObject
from projectkoios.physkit.core.data import DataObject
from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.solidstate.phase_field.cahn_hilliard.base import (
    DimensionlessCahnHilliardParameters,
)
from projectkoios.physkit.units import ScalarQuantity, Unitless, VectorQuantity


@dataclass(frozen=True, slots=True, eq=False, kw_only=True)
class DimensionlessPeriodicCahnHilliard1DState(DataObject):
    """Represent one reduced scalar field on a uniform periodic line."""

    field_values: VectorQuantity
    domain_length: ScalarQuantity

    def __post_init__(self) -> None:
        """Check every one-dimensional state argument."""
        self._check_arg_field_values()
        self._check_arg_domain_length()

    def _check_arg_field_values(self) -> None:
        """Require at least four unitless periodic samples."""
        if not isinstance(self.field_values, VectorQuantity):
            raise TypeError("field_values must be VectorQuantity")
        if not isinstance(self.field_values.unit, Unitless):
            raise ValueError("field_values must be unitless")
        if self.field_values.magnitude.size < 4:
            raise ValueError("field_values must contain at least four samples")

    def _check_arg_domain_length(self) -> None:
        """Require a positive unitless reduced domain length."""
        if not isinstance(self.domain_length, ScalarQuantity):
            raise TypeError("domain_length must be ScalarQuantity")
        if not isinstance(self.domain_length.unit, Unitless):
            raise ValueError("domain_length must be unitless")
        if self.domain_length.magnitude <= 0.0:
            raise ValueError("domain_length must be positive")

    @property
    def mean_field(self) -> ScalarQuantity:
        """Return the discrete periodic mean of the conserved field."""
        return ScalarQuantity(
            magnitude=float(np.mean(self.field_values.magnitude)),
            unit=Unitless(),
        )

    @property
    def grid_points(self) -> VectorQuantity:
        """Return uniform endpoint-excluded reduced coordinates."""
        return VectorQuantity(
            magnitude=np.linspace(
                0.0,
                self.domain_length.magnitude,
                self.field_values.magnitude.size,
                endpoint=False,
                dtype=np.float64,
            ),
            unit=Unitless(),
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionlessPeriodicCahnHilliard1DSolveRequest(DataObject):
    """Request bounded semi-implicit spectral evolution."""

    model: DimensionlessPeriodicCahnHilliard1DModel
    initial_state: DimensionlessPeriodicCahnHilliard1DState
    step_count: int
    snapshot_stride: int

    def __post_init__(self) -> None:
        """Check every one-dimensional solve request argument."""
        self._check_arg_model()
        self._check_arg_initial_state()
        self._check_arg_step_count()
        self._check_arg_snapshot_stride()

    def _check_arg_model(self) -> None:
        """Require the dimensionless periodic model."""
        if not isinstance(self.model, DimensionlessPeriodicCahnHilliard1DModel):
            raise TypeError("model must be DimensionlessPeriodicCahnHilliard1DModel")

    def _check_arg_initial_state(self) -> None:
        """Require a one-dimensional periodic state."""
        if not isinstance(
            self.initial_state,
            DimensionlessPeriodicCahnHilliard1DState,
        ):
            raise TypeError(
                "initial_state must be DimensionlessPeriodicCahnHilliard1DState"
            )

    def _check_arg_step_count(self) -> None:
        """Require a positive built-in integer step count."""
        if type(self.step_count) is not int:
            raise TypeError("step_count must be a built-in int")
        if self.step_count <= 0:
            raise ValueError("step_count must be positive")

    def _check_arg_snapshot_stride(self) -> None:
        """Require a positive built-in integer snapshot stride."""
        if type(self.snapshot_stride) is not int:
            raise TypeError("snapshot_stride must be a built-in int")
        if self.snapshot_stride <= 0:
            raise ValueError("snapshot_stride must be positive")


@dataclass(frozen=True, slots=True, eq=False, kw_only=True)
class DimensionlessPeriodicCahnHilliard1DSolution(ResultsObject):
    """Retain one solve request and its ordered state snapshots."""

    request: DimensionlessPeriodicCahnHilliard1DSolveRequest
    step_indices: tuple[int, ...]
    snapshots: tuple[DimensionlessPeriodicCahnHilliard1DState, ...]

    def __post_init__(self) -> None:
        """Check every one-dimensional solution argument."""
        self._check_arg_request()
        self._check_arg_step_indices()
        self._check_arg_snapshots()

    def _check_arg_request(self) -> None:
        """Require the complete solve request."""
        if not isinstance(
            self.request,
            DimensionlessPeriodicCahnHilliard1DSolveRequest,
        ):
            raise TypeError(
                "request must be DimensionlessPeriodicCahnHilliard1DSolveRequest"
            )

    def _check_arg_step_indices(self) -> None:
        """Require increasing integer indices spanning initial and final states."""
        if not isinstance(self.step_indices, tuple) or not all(
            type(index) is int for index in self.step_indices
        ):
            raise TypeError("step_indices must be a tuple of built-in integers")
        if not self.step_indices:
            raise ValueError("step_indices must be nonempty")
        if self.step_indices[0] != 0:
            raise ValueError("step_indices must begin at zero")
        if self.step_indices[-1] != self.request.step_count:
            raise ValueError("step_indices must end at step_count")
        if any(
            right <= left
            for left, right in zip(
                self.step_indices[:-1],
                self.step_indices[1:],
                strict=True,
            )
        ):
            raise ValueError("step_indices must increase strictly")

    def _check_arg_snapshots(self) -> None:
        """Require one compatible immutable state per index."""
        if not isinstance(self.snapshots, tuple) or not all(
            isinstance(snapshot, DimensionlessPeriodicCahnHilliard1DState)
            for snapshot in self.snapshots
        ):
            raise TypeError(
                "snapshots must be a tuple of DimensionlessPeriodicCahnHilliard1DState"
            )
        if len(self.snapshots) != len(self.step_indices):
            raise ValueError("snapshots must align with step_indices")
        reference = self.request.initial_state
        if any(
            snapshot.field_values.magnitude.shape
            != reference.field_values.magnitude.shape
            or snapshot.domain_length != reference.domain_length
            for snapshot in self.snapshots
        ):
            raise ValueError("snapshots must remain on the requested periodic grid")

    @property
    def final_state(self) -> DimensionlessPeriodicCahnHilliard1DState:
        """Return the terminal immutable state."""
        return self.snapshots[-1]

    @property
    def dimensionless_times(self) -> VectorQuantity:
        """Return reduced times corresponding to the snapshot indices."""
        return VectorQuantity(
            magnitude=np.asarray(
                self.step_indices,
                dtype=np.float64,
            )
            * self.request.model.parameters.time_step.magnitude,
            unit=Unitless(),
        )


@dataclass(frozen=True, slots=True)
class DimensionlessPeriodicCahnHilliard1DSpectralSolver:
    """Advance the reduced periodic equation with a semi-implicit FFT scheme."""

    def action(
        self,
        *,
        request: DimensionlessPeriodicCahnHilliard1DSolveRequest,
    ) -> DimensionlessPeriodicCahnHilliard1DSolution:
        """Advance the nonlinear term explicitly and gradient term implicitly."""
        if not isinstance(
            request,
            DimensionlessPeriodicCahnHilliard1DSolveRequest,
        ):
            raise TypeError(
                "request must be DimensionlessPeriodicCahnHilliard1DSolveRequest"
            )
        parameters = request.model.parameters
        values = np.asarray(
            request.initial_state.field_values.magnitude,
            dtype=np.float64,
        ).copy()
        sample_count = values.size
        spacing = request.initial_state.domain_length.magnitude / sample_count
        wave_numbers = 2.0 * np.pi * np.fft.fftfreq(sample_count, d=spacing)
        squared_wave_numbers = wave_numbers**2
        fourth_power_wave_numbers = squared_wave_numbers**2
        denominator = (
            1.0
            + parameters.time_step.magnitude
            * parameters.mobility.magnitude
            * parameters.gradient_penalty.magnitude
            * fourth_power_wave_numbers
        )
        indices = [0]
        snapshots = [request.initial_state]
        for step_index in range(1, request.step_count + 1):
            nonlinear_transform = np.fft.fft(values**3 - values)
            transformed = (
                np.fft.fft(values)
                - parameters.time_step.magnitude
                * parameters.mobility.magnitude
                * squared_wave_numbers
                * nonlinear_transform
            ) / denominator
            values = np.asarray(np.fft.ifft(transformed).real, dtype=np.float64)
            if (
                step_index % request.snapshot_stride == 0
                or step_index == request.step_count
            ):
                indices.append(step_index)
                snapshots.append(
                    DimensionlessPeriodicCahnHilliard1DState(
                        field_values=VectorQuantity(
                            magnitude=values,
                            unit=Unitless(),
                        ),
                        domain_length=request.initial_state.domain_length,
                    )
                )
        return DimensionlessPeriodicCahnHilliard1DSolution(
            request=request,
            step_indices=tuple(indices),
            snapshots=tuple(snapshots),
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionlessPeriodicCahnHilliard1DModel(
    ActionizedDataObject[
        DimensionlessPeriodicCahnHilliard1DSolveRequest,
        DimensionlessPeriodicCahnHilliard1DSolution,
    ]
):
    """Represent reduced constant-mobility periodic Cahn--Hilliard dynamics."""

    parameters: DimensionlessCahnHilliardParameters
    actionizer: DimensionlessPeriodicCahnHilliard1DSpectralSolver = field(
        default_factory=DimensionlessPeriodicCahnHilliard1DSpectralSolver,
        init=False,
        repr=False,
        compare=False,
    )

    def __post_init__(self) -> None:
        """Check the complete parameter record."""
        self._check_arg_parameters()

    def _check_arg_parameters(self) -> None:
        """Require dimensionless Cahn--Hilliard parameters."""
        if not isinstance(self.parameters, DimensionlessCahnHilliardParameters):
            raise TypeError("parameters must be DimensionlessCahnHilliardParameters")

    def solve(
        self,
        *,
        initial_state: DimensionlessPeriodicCahnHilliard1DState,
        step_count: int,
        snapshot_stride: int,
    ) -> DimensionlessPeriodicCahnHilliard1DSolution:
        """Evolve one initial periodic field for a bounded number of steps."""
        return self._respond(
            request=DimensionlessPeriodicCahnHilliard1DSolveRequest(
                model=self,
                initial_state=initial_state,
                step_count=step_count,
                snapshot_stride=snapshot_stride,
            )
        )
