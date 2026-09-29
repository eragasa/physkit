"""Flux tests for ``PlanarHertzKnudsen3DNetFluxModel``."""

import math

import numpy as np
import pytest

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.transport.phase_change.hertz_knudsen3d import (
    PlanarHertzKnudsen3DNetFluxModel,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestPlanarHertzKnudsen3DNetFluxModelEvaluate:
    """Verify separate and signed Hertz--Knudsen flux contributions."""

    @staticmethod
    def _model() -> PlanarHertzKnudsen3DNetFluxModel:
        return PlanarHertzKnudsen3DNetFluxModel(
            particle_mass=ScalarQuantity(
                magnitude=4.65e-26,
                unit=PhysicalUnit(expression="kilogram"),
            ),
            evaporation_coefficient=ScalarQuantity(
                magnitude=0.8,
                unit=Unitless(),
            ),
            condensation_coefficient=ScalarQuantity(
                magnitude=0.5,
                unit=Unitless(),
            ),
        )

    def test__evaluate_matches_separate_signed_formula(self) -> None:
        model = self._model()
        temperatures_kelvin = np.array([300.0, 600.0], dtype=np.float64)
        equilibrium_pressure_pascal = np.array([2.0, 4.0], dtype=np.float64)
        ambient_pressure_pascal = np.array([1.0, 8.0], dtype=np.float64)

        evaluation = model.evaluate(
            temperatures=VectorQuantity(
                magnitude=temperatures_kelvin,
                unit=PhysicalUnit(expression="kelvin"),
            ),
            equilibrium_pressures=VectorQuantity(
                magnitude=equilibrium_pressure_pascal,
                unit=PhysicalUnit(expression="pascal"),
            ),
            ambient_pressures=VectorQuantity(
                magnitude=ambient_pressure_pascal,
                unit=PhysicalUnit(expression="pascal"),
            ),
            number_flux_unit=PhysicalUnit(expression="meter ** -2 / second"),
            mass_flux_unit=PhysicalUnit(expression="kilogram / meter ** 2 / second"),
        )

        denominator = np.sqrt(
            2.0 * math.pi * model.particle_mass.magnitude * SI.k_B * temperatures_kelvin
        )
        expected_evaporation = 0.8 * equilibrium_pressure_pascal / denominator
        expected_condensation = 0.5 * ambient_pressure_pascal / denominator
        expected_net = expected_evaporation - expected_condensation
        np.testing.assert_allclose(
            evaluation.evaporation_number_flux.magnitude,
            expected_evaporation,
            rtol=2.0e-16,
            atol=0.0,
        )
        np.testing.assert_allclose(
            evaluation.condensation_number_flux.magnitude,
            expected_condensation,
            rtol=2.0e-16,
            atol=0.0,
        )
        np.testing.assert_allclose(
            evaluation.net_number_flux.magnitude,
            expected_net,
            rtol=2.0e-16,
            atol=0.0,
        )
        np.testing.assert_allclose(
            evaluation.net_mass_flux.magnitude,
            model.particle_mass.magnitude * expected_net,
            rtol=2.0e-16,
            atol=0.0,
        )
        assert evaluation.net_number_flux.magnitude[0] > 0.0
        assert evaluation.net_number_flux.magnitude[1] < 0.0

    def test__evaluate_does_not_clamp_condensation_dominated_flux(self) -> None:
        evaluation = self._model().evaluate(
            temperatures=VectorQuantity(
                magnitude=np.array([300.0], dtype=np.float64),
                unit=PhysicalUnit(expression="kelvin"),
            ),
            equilibrium_pressures=VectorQuantity(
                magnitude=np.array([0.0], dtype=np.float64),
                unit=PhysicalUnit(expression="pascal"),
            ),
            ambient_pressures=VectorQuantity(
                magnitude=np.array([1.0], dtype=np.float64),
                unit=PhysicalUnit(expression="pascal"),
            ),
            number_flux_unit=PhysicalUnit(expression="centimeter ** -2 / second"),
            mass_flux_unit=PhysicalUnit(expression="gram / meter ** 2 / second"),
        )

        assert evaluation.net_number_flux.magnitude[0] < 0.0
        assert evaluation.net_mass_flux.magnitude[0] < 0.0

    def test__init_rejects_coefficient_above_one(self) -> None:
        with pytest.raises(ValueError, match="closed interval"):
            PlanarHertzKnudsen3DNetFluxModel(
                particle_mass=ScalarQuantity(
                    magnitude=4.65e-26,
                    unit=PhysicalUnit(expression="kilogram"),
                ),
                evaporation_coefficient=ScalarQuantity(
                    magnitude=1.01,
                    unit=Unitless(),
                ),
                condensation_coefficient=ScalarQuantity(
                    magnitude=0.5,
                    unit=Unitless(),
                ),
            )
