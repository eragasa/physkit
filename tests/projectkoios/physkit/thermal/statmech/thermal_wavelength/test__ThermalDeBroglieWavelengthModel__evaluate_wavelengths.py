"""Wavelength tests for ``ThermalDeBroglieWavelengthModel``."""

import math

import numpy as np
import pytest

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.statmech.thermal_wavelength import (
    ThermalDeBroglieWavelengthModel,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, VectorQuantity


class TestThermalDeBroglieWavelengthModelEvaluateWavelengths:
    """Verify canonical unit-aware thermal wavelengths."""

    @staticmethod
    def _electron_model() -> ThermalDeBroglieWavelengthModel:
        return ThermalDeBroglieWavelengthModel(
            particle_mass=ScalarQuantity(
                magnitude=float(SI.me0),
                unit=PhysicalUnit(expression="kilogram"),
            )
        )

    def test__evaluate_wavelengths_matches_canonical_closed_form(self) -> None:
        temperatures_kelvin = np.array([300.0, 1200.0], dtype=np.float64)

        evaluation = self._electron_model().evaluate_wavelengths(
            temperatures=VectorQuantity(
                magnitude=temperatures_kelvin,
                unit=PhysicalUnit(expression="kelvin"),
            ),
            wavelength_unit=PhysicalUnit(expression="nanometer"),
        )

        expected_metres = SI.h / np.sqrt(
            2.0 * math.pi * SI.me0 * SI.k_B * temperatures_kelvin
        )
        np.testing.assert_allclose(
            evaluation.wavelengths.magnitude,
            expected_metres * 1.0e9,
            rtol=2.0e-16,
            atol=0.0,
        )
        assert evaluation.wavelengths.magnitude[0] == pytest.approx(4.303475436666189)
        assert evaluation.wavelengths.unit == PhysicalUnit(expression="nanometer")

    def test__evaluate_wavelengths_obeys_inverse_square_root_scaling(self) -> None:
        evaluation = self._electron_model().evaluate_wavelengths(
            temperatures=VectorQuantity(
                magnitude=np.array([300.0, 1200.0], dtype=np.float64),
                unit=PhysicalUnit(expression="kelvin"),
            ),
            wavelength_unit=PhysicalUnit(expression="meter"),
        )

        ratio = (
            evaluation.wavelengths.magnitude[0] / evaluation.wavelengths.magnitude[1]
        )
        assert ratio == pytest.approx(2.0)

    def test__evaluate_wavelengths_rejects_absolute_zero(self) -> None:
        with pytest.raises(ValueError, match="above absolute zero"):
            self._electron_model().evaluate_wavelengths(
                temperatures=VectorQuantity(
                    magnitude=np.array([0.0], dtype=np.float64),
                    unit=PhysicalUnit(expression="kelvin"),
                ),
                wavelength_unit=PhysicalUnit(expression="meter"),
            )
