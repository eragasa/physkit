"""Evaluation tests for ``BlackbodyWavelengthSpectrumModel``."""

import numpy as np
import pytest

from projectkoios.physkit.thermal.statmech.radiation.blackbody import (
    BlackbodyWavelengthSpectrumModel,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, VectorQuantity


class TestBlackbodyWavelengthSpectrumModelEvaluate:
    """Verify unit-aware Planck and limiting wavelength spectra."""

    @staticmethod
    def _model() -> BlackbodyWavelengthSpectrumModel:
        return BlackbodyWavelengthSpectrumModel()

    def test__evaluate_returns_correlated_nonnegative_spectra(self) -> None:
        wavelengths = VectorQuantity(
            magnitude=np.array([0.5, 1.0, 2.0], dtype=np.float64),
            unit=PhysicalUnit(expression="micrometer"),
        )
        temperature = ScalarQuantity(
            magnitude=5000.0,
            unit=PhysicalUnit(expression="kelvin"),
        )
        density_unit = PhysicalUnit(expression="joule / meter ** 4")

        evaluation = self._model().evaluate(
            wavelengths=wavelengths,
            temperature=temperature,
            spectral_energy_density_unit=density_unit,
        )

        assert evaluation.request.wavelengths is wavelengths
        assert evaluation.request.temperature is temperature
        for density in (
            evaluation.planck_spectral_energy_density,
            evaluation.wien_spectral_energy_density,
            evaluation.rayleigh_jeans_spectral_energy_density,
        ):
            assert density.unit == density_unit
            assert density.magnitude.shape == wavelengths.magnitude.shape
            assert np.all(np.isfinite(density.magnitude))
            assert np.all(density.magnitude >= 0.0)

    def test__evaluate_wien_limit_agrees_at_short_wavelength(self) -> None:
        evaluation = self._model().evaluate(
            wavelengths=VectorQuantity(
                magnitude=np.array([1.0], dtype=np.float64),
                unit=PhysicalUnit(expression="micrometer"),
            ),
            temperature=ScalarQuantity(
                magnitude=100.0,
                unit=PhysicalUnit(expression="kelvin"),
            ),
            spectral_energy_density_unit=PhysicalUnit(expression="joule / meter ** 4"),
        )

        np.testing.assert_allclose(
            evaluation.wien_spectral_energy_density.magnitude,
            evaluation.planck_spectral_energy_density.magnitude,
            rtol=3.0e-16,
            atol=0.0,
        )

    def test__evaluate_rayleigh_jeans_limit_agrees_at_long_wavelength(self) -> None:
        evaluation = self._model().evaluate(
            wavelengths=VectorQuantity(
                magnitude=np.array([1.0], dtype=np.float64),
                unit=PhysicalUnit(expression="meter"),
            ),
            temperature=ScalarQuantity(
                magnitude=300.0,
                unit=PhysicalUnit(expression="kelvin"),
            ),
            spectral_energy_density_unit=PhysicalUnit(expression="joule / meter ** 4"),
        )

        np.testing.assert_allclose(
            evaluation.rayleigh_jeans_spectral_energy_density.magnitude,
            evaluation.planck_spectral_energy_density.magnitude,
            rtol=3.0e-5,
            atol=0.0,
        )

    def test__evaluate_rejects_zero_wavelength(self) -> None:
        with pytest.raises(ValueError, match="wavelengths must be positive"):
            self._model().evaluate(
                wavelengths=VectorQuantity(
                    magnitude=np.array([0.0], dtype=np.float64),
                    unit=PhysicalUnit(expression="meter"),
                ),
                temperature=ScalarQuantity(
                    magnitude=300.0,
                    unit=PhysicalUnit(expression="kelvin"),
                ),
                spectral_energy_density_unit=PhysicalUnit(
                    expression="joule / meter ** 4"
                ),
            )
