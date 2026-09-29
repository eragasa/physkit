"""Evaluation tests for ``GaussianWavePacket1DInitialState``."""

from inspect import signature

import numpy as np

from projectkoios.physkit.qm.sampled_states import (
    GaussianWavePacket1DInitialState,
    GaussianWavePacket1DInitialStateModel,
    SampledQuantumState1D,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestGaussianWavePacket1DInitialStateEvaluate:
    """Verify the initial Gaussian envelope and phase convention."""

    def test__init_exposes_only_the_initial_state_model(self) -> None:
        assert tuple(signature(GaussianWavePacket1DInitialState).parameters) == (
            "model",
        )

    def test__evaluate_returns_centered_complex_initial_state(self) -> None:
        coordinate_values = np.array([-1.0, 0.0, 1.0], dtype=np.float64)
        center = 0.0
        width = 1.0
        wavenumber = np.pi
        tolerance = 2.0e-16
        coordinates = VectorQuantity(
            magnitude=coordinate_values,
            unit=Unitless(),
        )
        initial_state = GaussianWavePacket1DInitialState(
            model=GaussianWavePacket1DInitialStateModel(
                center=ScalarQuantity(magnitude=center, unit=Unitless()),
                width=ScalarQuantity(magnitude=width, unit=Unitless()),
                wavenumber=ScalarQuantity(magnitude=wavenumber, unit=Unitless()),
            )
        )

        sampled_state = initial_state.evaluate(coordinates=coordinates)

        expected = np.exp(-(coordinate_values**2) / (2.0 * width**2)) * np.exp(
            1.0j * wavenumber * coordinate_values
        )
        assert isinstance(sampled_state, SampledQuantumState1D)
        np.testing.assert_allclose(
            sampled_state.amplitudes.magnitude,
            expected,
            rtol=0.0,
            atol=tolerance,
        )
        assert sampled_state.coordinates is coordinates
        assert isinstance(sampled_state.amplitudes.unit, Unitless)

    def test__evaluate_converts_length_and_inverse_length_units(self) -> None:
        meter = PhysicalUnit(expression="meter")
        centimeter = PhysicalUnit(expression="centimeter")
        inverse_centimeter = PhysicalUnit(expression="centimeter ** -1")
        coordinate_values = np.array([0.0, 1.0], dtype=np.float64)
        center_centimeters = 50.0
        width_centimeters = 50.0
        wavenumber_per_centimeter = 0.01
        center_meters = 0.5
        width_meters = 0.5
        wavenumber_per_meter = 1.0
        tolerance = 2.0e-16
        coordinates = VectorQuantity(magnitude=coordinate_values, unit=meter)
        initial_state = GaussianWavePacket1DInitialState(
            model=GaussianWavePacket1DInitialStateModel(
                center=ScalarQuantity(
                    magnitude=center_centimeters,
                    unit=centimeter,
                ),
                width=ScalarQuantity(
                    magnitude=width_centimeters,
                    unit=centimeter,
                ),
                wavenumber=ScalarQuantity(
                    magnitude=wavenumber_per_centimeter,
                    unit=inverse_centimeter,
                ),
            )
        )

        sampled_state = initial_state.evaluate(coordinates=coordinates)

        displacement = coordinate_values - center_meters
        expected = np.exp(-(displacement**2) / (2.0 * width_meters**2)) * np.exp(
            1.0j * wavenumber_per_meter * coordinate_values
        )
        np.testing.assert_allclose(
            sampled_state.amplitudes.magnitude,
            expected,
            rtol=0.0,
            atol=tolerance,
        )
