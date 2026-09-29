r"""Dimensionless periodic two-dimensional Cahn--Hilliard evolution."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from projectkoios.physkit.core.actions import ActionizedDataObject
from projectkoios.physkit.core.data import DataObject
from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.solidstate.phase_field.cahn_hilliard.base import (
    DimensionlessCahnHilliardParameters,
)
from projectkoios.physkit.units import MatrixQuantity, ScalarQuantity, Unitless


@dataclass(frozen=True, slots=True, eq=False, kw_only=True)
class DimensionlessPeriodicCahnHilliard2DState(DataObject):
    """Represent one reduced scalar field on a uniform periodic rectangle."""

    field_values: MatrixQuantity
    domain_length_x: ScalarQuantity
    domain_length_y: ScalarQuantity

    def __post_init__(self) -> None:
        """Check every two-dimensional state argument."""
        self._check_arg_field_values()
        self._check_arg_domain_length_x()
        self._check_arg_domain_length_y()

    def _check_arg_field_values(self) -> None:
        """Require at least four unitless samples along each axis."""
        if not isinstance(self.field_values, MatrixQuantity):
            raise TypeError("field_values must be MatrixQuantity")
        if not isinstance(self.field_values.unit, Unitless):
            raise ValueError("field_values must be unitless")
        if any(size < 4 for size in self.field_values.magnitude.shape):
            raise ValueError("field_values must have at least four samples per axis")

    def _check_arg_domain_length_x(self) -> None:
        """Require a positive unitless reduced x length."""
        self._check_positive_unitless_length(
            quantity=self.domain_length_x,
            argument_name="domain_length_x",
        )

    def _check_arg_domain_length_y(self) -> None:
        """Require a positive unitless reduced y length."""
        self._check_positive_unitless_length(
            quantity=self.domain_length_y,
            argument_name="domain_length_y",
        )

    @staticmethod
    def _check_positive_unitless_length(
        *,
        quantity: ScalarQuantity,
        argument_name: str,
    ) -> None:
        """Apply repeated mechanical reduced-length checks."""
        if not isinstance(quantity, ScalarQuantity):
            raise TypeError(f"{argument_name} must be ScalarQuantity")
        if not isinstance(quantity.unit, Unitless):
            raise ValueError(f"{argument_name} must be unitless")
        if quantity.magnitude <= 0.0:
            raise ValueError(f"{argument_name} must be positive")

    @property
    def mean_field(self) -> ScalarQuantity:
        """Return the discrete periodic mean of the conserved field."""
        return ScalarQuantity(
            magnitude=float(np.mean(self.field_values.magnitude)),
            unit=Unitless(),
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionlessPeriodicCahnHilliard2DSolveRequest(DataObject):
    """Request bounded two-dimensional semi-implicit spectral evolution."""

    model: DimensionlessPeriodicCahnHilliard2DModel
    initial_state: DimensionlessPeriodicCahnHilliard2DState
    step_count: int
    snapshot_stride: int

    def __post_init__(self) -> None:
        """Check every two-dimensional solve request argument."""
        self._check_arg_model()
        self._check_arg_initial_state()
        self._check_arg_step_count()
        self._check_arg_snapshot_stride()

    def _check_arg_model(self) -> None:
        """Require the dimensionless periodic model."""
        if not isinstance(self.model, DimensionlessPeriodicCahnHilliard2DModel):
            raise TypeError("model must be DimensionlessPeriodicCahnHilliard2DModel")

    def _check_arg_initial_state(self) -> None:
        """Require a two-dimensional periodic state."""
        if not isinstance(
            self.initial_state,
            DimensionlessPeriodicCahnHilliard2DState,
        ):
            raise TypeError(
                "initial_state must be DimensionlessPeriodicCahnHilliard2DState"
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
class DimensionlessPeriodicCahnHilliard2DSolution(ResultsObject):
    """Retain one solve request and its ordered matrix snapshots."""

    request: DimensionlessPeriodicCahnHilliard2DSolveRequest
    step_indices: tuple[int, ...]
    snapshots: tuple[DimensionlessPeriodicCahnHilliard2DState, ...]

    def __post_init__(self) -> None:
        """Check every two-dimensional solution argument."""
        self._check_arg_request()
        self._check_arg_step_indices()
        self._check_arg_snapshots()

    def _check_arg_request(self) -> None:
        """Require the complete solve request."""
        if not isinstance(
            self.request,
            DimensionlessPeriodicCahnHilliard2DSolveRequest,
        ):
            raise TypeError(
                "request must be DimensionlessPeriodicCahnHilliard2DSolveRequest"
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
            isinstance(snapshot, DimensionlessPeriodicCahnHilliard2DState)
            for snapshot in self.snapshots
        ):
            raise TypeError(
                "snapshots must be a tuple of DimensionlessPeriodicCahnHilliard2DState"
            )
        if len(self.snapshots) != len(self.step_indices):
            raise ValueError("snapshots must align with step_indices")
        reference = self.request.initial_state
        if any(
            snapshot.field_values.magnitude.shape
            != reference.field_values.magnitude.shape
            or snapshot.domain_length_x != reference.domain_length_x
            or snapshot.domain_length_y != reference.domain_length_y
            for snapshot in self.snapshots
        ):
            raise ValueError("snapshots must remain on the requested periodic grid")

    @property
    def final_state(self) -> DimensionlessPeriodicCahnHilliard2DState:
        """Return the terminal immutable state."""
        return self.snapshots[-1]


@dataclass(frozen=True, slots=True)
class DimensionlessPeriodicCahnHilliard2DSpectralSolver:
    """Advance the reduced periodic equation with a semi-implicit 2D FFT scheme."""

    def action(
        self,
        *,
        request: DimensionlessPeriodicCahnHilliard2DSolveRequest,
    ) -> DimensionlessPeriodicCahnHilliard2DSolution:
        """Advance the nonlinear term explicitly and gradient term implicitly."""
        if not isinstance(
            request,
            DimensionlessPeriodicCahnHilliard2DSolveRequest,
        ):
            raise TypeError(
                "request must be DimensionlessPeriodicCahnHilliard2DSolveRequest"
            )
        parameters = request.model.parameters
        values = np.asarray(
            request.initial_state.field_values.magnitude,
            dtype=np.float64,
        ).copy()
        count_x, count_y = values.shape
        spacing_x = request.initial_state.domain_length_x.magnitude / count_x
        spacing_y = request.initial_state.domain_length_y.magnitude / count_y
        wave_x = 2.0 * np.pi * np.fft.fftfreq(count_x, d=spacing_x)
        wave_y = 2.0 * np.pi * np.fft.fftfreq(count_y, d=spacing_y)
        squared_x, squared_y = np.meshgrid(wave_x**2, wave_y**2, indexing="ij")
        squared_wave_numbers = squared_x + squared_y
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
            nonlinear_transform = np.fft.fft2(values**3 - values)
            transformed = (
                np.fft.fft2(values)
                - parameters.time_step.magnitude
                * parameters.mobility.magnitude
                * squared_wave_numbers
                * nonlinear_transform
            ) / denominator
            values = np.asarray(np.fft.ifft2(transformed).real, dtype=np.float64)
            if (
                step_index % request.snapshot_stride == 0
                or step_index == request.step_count
            ):
                indices.append(step_index)
                snapshots.append(
                    DimensionlessPeriodicCahnHilliard2DState(
                        field_values=MatrixQuantity(
                            magnitude=values,
                            unit=Unitless(),
                        ),
                        domain_length_x=request.initial_state.domain_length_x,
                        domain_length_y=request.initial_state.domain_length_y,
                    )
                )
        return DimensionlessPeriodicCahnHilliard2DSolution(
            request=request,
            step_indices=tuple(indices),
            snapshots=tuple(snapshots),
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionlessPeriodicCahnHilliard2DModel(
    ActionizedDataObject[
        DimensionlessPeriodicCahnHilliard2DSolveRequest,
        DimensionlessPeriodicCahnHilliard2DSolution,
    ]
):
    """Represent reduced constant-mobility periodic Cahn--Hilliard dynamics."""

    parameters: DimensionlessCahnHilliardParameters
    actionizer: DimensionlessPeriodicCahnHilliard2DSpectralSolver = field(
        default_factory=DimensionlessPeriodicCahnHilliard2DSpectralSolver,
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
        initial_state: DimensionlessPeriodicCahnHilliard2DState,
        step_count: int,
        snapshot_stride: int,
    ) -> DimensionlessPeriodicCahnHilliard2DSolution:
        """Evolve one initial periodic field for a bounded number of steps."""
        return self._respond(
            request=DimensionlessPeriodicCahnHilliard2DSolveRequest(
                model=self,
                initial_state=initial_state,
                step_count=step_count,
                snapshot_stride=snapshot_stride,
            )
        )
