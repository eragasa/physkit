"""Mixing tests for ``SymmetricRegularSolutionModel``."""

import math

import numpy as np
import pytest

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.thermo.mixtures.regular_solution import (
    SymmetricRegularSolutionModel,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestSymmetricRegularSolutionModelEvaluateMixing:
    """Verify unit-aware symmetric regular-solution mixing quantities."""

    @staticmethod
    def _model() -> SymmetricRegularSolutionModel:
        return SymmetricRegularSolutionModel(
            interaction_parameter=ScalarQuantity(
                magnitude=10.0,
                unit=PhysicalUnit(expression="kilojoule / mole"),
            )
        )

    def test__evaluate_mixing_matches_endpoints_and_equimolar_formula(self) -> None:
        mole_fractions = VectorQuantity(
            magnitude=np.array([0.0, 0.5, 1.0], dtype=np.float64),
            unit=Unitless(),
        )
        temperature_kelvin = 400.0

        evaluation = self._model().evaluate_mixing(
            component_b_mole_fractions=mole_fractions,
            temperature=ScalarQuantity(
                magnitude=temperature_kelvin,
                unit=PhysicalUnit(expression="kelvin"),
            ),
            molar_energy_unit=PhysicalUnit(expression="kilojoule / mole"),
        )

        expected_enthalpy_kilojoule_per_mole = 2.5
        expected_entropy_joule_per_mole_kelvin = SI.R_g * math.log(2.0)
        expected_gibbs_kilojoule_per_mole = (
            expected_enthalpy_kilojoule_per_mole
            - temperature_kelvin * expected_entropy_joule_per_mole_kelvin / 1000.0
        )
        np.testing.assert_allclose(
            evaluation.molar_enthalpy_of_mixing.magnitude,
            np.array(
                [0.0, expected_enthalpy_kilojoule_per_mole, 0.0],
                dtype=np.float64,
            ),
            rtol=0.0,
            atol=0.0,
        )
        assert evaluation.molar_entropy_of_mixing.magnitude[1] == pytest.approx(
            expected_entropy_joule_per_mole_kelvin / 1000.0
        )
        assert evaluation.molar_gibbs_free_energy_of_mixing.magnitude[1] == (
            pytest.approx(expected_gibbs_kilojoule_per_mole)
        )
        assert np.array_equal(
            evaluation.molar_gibbs_free_energy_of_mixing.magnitude[[0, 2]],
            np.zeros(2, dtype=np.float64),
        )

    def test__evaluate_mixing_is_symmetric_under_component_exchange(self) -> None:
        evaluation = self._model().evaluate_mixing(
            component_b_mole_fractions=VectorQuantity(
                magnitude=np.array([0.2, 0.8], dtype=np.float64),
                unit=Unitless(),
            ),
            temperature=ScalarQuantity(
                magnitude=26.85,
                unit=PhysicalUnit(expression="degree_Celsius"),
            ),
            molar_energy_unit=PhysicalUnit(expression="joule / mole"),
        )

        for quantity in (
            evaluation.molar_enthalpy_of_mixing,
            evaluation.molar_entropy_of_mixing,
            evaluation.molar_gibbs_free_energy_of_mixing,
        ):
            assert quantity.magnitude[0] == pytest.approx(quantity.magnitude[1])

    def test__evaluate_mixing_rejects_out_of_range_fraction(self) -> None:
        with pytest.raises(ValueError, match="closed interval"):
            self._model().evaluate_mixing(
                component_b_mole_fractions=VectorQuantity(
                    magnitude=np.array([1.01], dtype=np.float64),
                    unit=Unitless(),
                ),
                temperature=ScalarQuantity(
                    magnitude=400.0,
                    unit=PhysicalUnit(expression="kelvin"),
                ),
                molar_energy_unit=PhysicalUnit(expression="joule / mole"),
            )
