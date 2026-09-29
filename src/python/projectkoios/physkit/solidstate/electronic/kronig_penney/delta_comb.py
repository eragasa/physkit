r"""Dimensionless one-dimensional Kronig--Penney delta-comb dispersion."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from projectkoios.physkit.core.actions import ActionizedDataObject
from projectkoios.physkit.core.data import DataObject
from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.units import ScalarQuantity, Unitless, VectorQuantity


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionlessDeltaCombBandSamplingRequest(DataObject):
    """Request allowed states at explicit positive free-propagation phases."""

    model: DimensionlessKronigPenneyDeltaComb
    phase_parameters: VectorQuantity

    def __post_init__(self) -> None:
        """Check every band-sampling request argument."""
        self._check_arg_model()
        self._check_arg_phase_parameters()

    def _check_arg_model(self) -> None:
        """Require the dimensionless delta-comb model."""
        if not isinstance(self.model, DimensionlessKronigPenneyDeltaComb):
            raise TypeError("model must be DimensionlessKronigPenneyDeltaComb")

    def _check_arg_phase_parameters(self) -> None:
        """Require a nonempty increasing positive unitless phase vector."""
        if not isinstance(self.phase_parameters, VectorQuantity):
            raise TypeError("phase_parameters must be VectorQuantity")
        if not isinstance(self.phase_parameters.unit, Unitless):
            raise ValueError("phase_parameters must be unitless")
        values = self.phase_parameters.magnitude
        if values.size == 0:
            raise ValueError("phase_parameters must be nonempty")
        if np.any(values <= 0.0):
            raise ValueError("phase_parameters must be positive")
        if np.any(values[1:] <= values[:-1]):
            raise ValueError("phase_parameters must increase strictly")


@dataclass(frozen=True, slots=True, eq=False, kw_only=True)
class DimensionlessDeltaCombBandSampling(ResultsObject):
    """Retain sampled allowed states on the nonnegative Bloch-phase branch."""

    request: DimensionlessDeltaCombBandSamplingRequest
    allowed_phase_parameters: VectorQuantity
    bloch_phases: VectorQuantity
    reduced_energies: VectorQuantity

    def __post_init__(self) -> None:
        """Check every band-sampling response argument."""
        self._check_arg_request()
        self._check_arg_allowed_phase_parameters()
        self._check_arg_bloch_phases()
        self._check_arg_reduced_energies()

    def _check_arg_request(self) -> None:
        """Require the complete sampling request."""
        if not isinstance(self.request, DimensionlessDeltaCombBandSamplingRequest):
            raise TypeError("request must be DimensionlessDeltaCombBandSamplingRequest")

    def _check_arg_allowed_phase_parameters(self) -> None:
        """Require allowed unitless phase parameters from the request grid."""
        self._check_result_vector(
            vector=self.allowed_phase_parameters,
            argument_name="allowed_phase_parameters",
        )
        requested = self.request.phase_parameters.magnitude
        if not np.all(np.isin(self.allowed_phase_parameters.magnitude, requested)):
            raise ValueError(
                "allowed_phase_parameters must be selected from the request"
            )

    def _check_arg_bloch_phases(self) -> None:
        """Require nonnegative first-zone Bloch phases."""
        self._check_result_vector(
            vector=self.bloch_phases,
            argument_name="bloch_phases",
        )
        if np.any(self.bloch_phases.magnitude < 0.0) or np.any(
            self.bloch_phases.magnitude > np.pi
        ):
            raise ValueError("bloch_phases must lie in the closed interval [0, pi]")

    def _check_arg_reduced_energies(self) -> None:
        """Require nonnegative reduced energies matching the phase parameters."""
        self._check_result_vector(
            vector=self.reduced_energies,
            argument_name="reduced_energies",
        )
        expected = self.allowed_phase_parameters.magnitude**2
        if not np.array_equal(self.reduced_energies.magnitude, expected):
            raise ValueError("reduced_energies must equal phase parameter squared")

    def _check_result_vector(
        self,
        *,
        vector: VectorQuantity,
        argument_name: str,
    ) -> None:
        """Apply repeated mechanical result-vector checks."""
        if not isinstance(vector, VectorQuantity):
            raise TypeError(f"{argument_name} must be VectorQuantity")
        if not isinstance(vector.unit, Unitless):
            raise ValueError(f"{argument_name} must be unitless")
        expected_shape = self.allowed_phase_parameters.magnitude.shape
        if argument_name == "allowed_phase_parameters":
            expected_shape = vector.magnitude.shape
        if vector.magnitude.shape != expected_shape:
            raise ValueError(f"{argument_name} must match allowed_phase_parameters")


@dataclass(frozen=True, slots=True)
class DimensionlessDeltaCombBandSampler:
    """Evaluate the delta-comb dispersion and retain allowed samples."""

    def action(
        self,
        *,
        request: DimensionlessDeltaCombBandSamplingRequest,
    ) -> DimensionlessDeltaCombBandSampling:
        """Return samples satisfying the real first-zone Bloch condition."""
        if not isinstance(request, DimensionlessDeltaCombBandSamplingRequest):
            raise TypeError("request must be DimensionlessDeltaCombBandSamplingRequest")
        phase_parameters = request.phase_parameters.magnitude
        dispersion_values = np.cos(
            phase_parameters
        ) + request.model.barrier_strength.magnitude * np.sinc(phase_parameters / np.pi)
        allowed = np.abs(dispersion_values) <= 1.0
        allowed_phase_parameters = phase_parameters[allowed]
        allowed_dispersion_values = dispersion_values[allowed]
        return DimensionlessDeltaCombBandSampling(
            request=request,
            allowed_phase_parameters=VectorQuantity(
                magnitude=allowed_phase_parameters,
                unit=Unitless(),
            ),
            bloch_phases=VectorQuantity(
                magnitude=np.arccos(np.clip(allowed_dispersion_values, -1.0, 1.0)),
                unit=Unitless(),
            ),
            reduced_energies=VectorQuantity(
                magnitude=allowed_phase_parameters**2,
                unit=Unitless(),
            ),
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionlessKronigPenneyDeltaComb(
    ActionizedDataObject[
        DimensionlessDeltaCombBandSamplingRequest,
        DimensionlessDeltaCombBandSampling,
    ]
):
    r"""Represent $\cos(ka)=\cos z+P\sin(z)/z$ for $P\geq0$."""

    barrier_strength: ScalarQuantity
    actionizer: DimensionlessDeltaCombBandSampler = field(
        default_factory=DimensionlessDeltaCombBandSampler,
        init=False,
        repr=False,
        compare=False,
    )

    def __post_init__(self) -> None:
        """Check the dimensionless barrier-strength argument."""
        self._check_arg_barrier_strength()

    def _check_arg_barrier_strength(self) -> None:
        """Require a nonnegative unitless delta-comb strength."""
        if not isinstance(self.barrier_strength, ScalarQuantity):
            raise TypeError("barrier_strength must be ScalarQuantity")
        if not isinstance(self.barrier_strength.unit, Unitless):
            raise ValueError("barrier_strength must be unitless")
        if self.barrier_strength.magnitude < 0.0:
            raise ValueError("barrier_strength must be nonnegative")

    def dispersion_values(
        self,
        *,
        phase_parameters: VectorQuantity,
    ) -> VectorQuantity:
        r"""Return $\cos z+P\sin(z)/z$ on an explicit positive grid."""
        request = DimensionlessDeltaCombBandSamplingRequest(
            model=self,
            phase_parameters=phase_parameters,
        )
        values = request.phase_parameters.magnitude
        return VectorQuantity(
            magnitude=(
                np.cos(values)
                + self.barrier_strength.magnitude * np.sinc(values / np.pi)
            ),
            unit=Unitless(),
        )

    def sample_allowed_bands(
        self,
        *,
        phase_parameters: VectorQuantity,
    ) -> DimensionlessDeltaCombBandSampling:
        """Sample the nonnegative first-zone branch at allowed energies."""
        return self._respond(
            request=DimensionlessDeltaCombBandSamplingRequest(
                model=self,
                phase_parameters=phase_parameters,
            )
        )
