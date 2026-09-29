"""Normalization tests for ``SampledQuantumState1D``."""

import numpy as np
import pytest

from projectkoios.physkit.qm.sampled_states import SampledQuantumState1D
from projectkoios.physkit.units import (
    ComplexVectorQuantity,
    PhysicalUnit,
    Unitless,
    VectorQuantity,
)


class TestSampledQuantumState1DNormalize:
    """Verify weighted normalization and explicit amplitude units."""

    @staticmethod
    def _unitless_state(*, amplitudes: np.ndarray) -> SampledQuantumState1D:
        sample_count = amplitudes.size
        return SampledQuantumState1D(
            coordinates=VectorQuantity(
                magnitude=np.arange(sample_count, dtype=np.float64),
                unit=Unitless(),
            ),
            amplitudes=ComplexVectorQuantity(
                magnitude=amplitudes,
                unit=Unitless(),
            ),
        )

    def test__normalize_under_dimensionless_weights(self) -> None:
        first_amplitude = 3.0
        second_amplitude = 4.0j
        normalization_factor = 5.0
        tolerance = 2.0e-16
        amplitude_values = np.array(
            [first_amplitude + 0.0j, second_amplitude],
            dtype=np.complex128,
        )
        state = self._unitless_state(amplitudes=amplitude_values)
        quadrature_weights = VectorQuantity(
            magnitude=np.ones(amplitude_values.size, dtype=np.float64),
            unit=Unitless(),
        )

        normalization = state.normalize(
            quadrature_weights=quadrature_weights,
        )

        expected = amplitude_values / normalization_factor
        np.testing.assert_allclose(
            normalization.normalized_state.amplitudes.magnitude,
            expected,
            rtol=0.0,
            atol=tolerance,
        )
        assert normalization.request.state is state
        assert normalization.request.quadrature_weights is quadrature_weights
        assert normalization.normalization_factor.magnitude == normalization_factor
        assert isinstance(normalization.normalized_state.amplitudes.unit, Unitless)

    def test__normalize_assigns_inverse_square_root_physical_unit(self) -> None:
        sample_count = 2
        spacing = 0.5
        state = self._unitless_state(
            amplitudes=np.ones(sample_count, dtype=np.complex128),
        )
        quadrature_weights = VectorQuantity(
            magnitude=np.full(sample_count, spacing, dtype=np.float64),
            unit=PhysicalUnit(expression="meter"),
        )

        normalization = state.normalize(
            quadrature_weights=quadrature_weights,
        )

        assert normalization.normalized_state.amplitudes.unit == PhysicalUnit(
            expression="(meter) ** -0.5"
        )
        assert normalization.normalization_factor.unit == PhysicalUnit(
            expression="(meter) ** 0.5"
        )

    def test__normalize_rejects_zero_state(self) -> None:
        sample_count = 2
        state = self._unitless_state(
            amplitudes=np.zeros(sample_count, dtype=np.complex128),
        )
        quadrature_weights = VectorQuantity(
            magnitude=np.ones(sample_count, dtype=np.float64),
            unit=Unitless(),
        )

        with pytest.raises(ValueError, match="must not be identically zero"):
            state.normalize(quadrature_weights=quadrature_weights)

    def test__normalize_rejects_nonpositive_weight(self) -> None:
        sample_count = 2
        nonpositive_weight = 0.0
        state = self._unitless_state(
            amplitudes=np.ones(sample_count, dtype=np.complex128),
        )
        quadrature_weights = VectorQuantity(
            magnitude=np.array([1.0, nonpositive_weight], dtype=np.float64),
            unit=Unitless(),
        )

        with pytest.raises(ValueError, match="quadrature_weights must be positive"):
            state.normalize(quadrature_weights=quadrature_weights)
