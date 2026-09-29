"""Occupation-evaluation tests for ``FermiDiracState``."""

import numpy as np
import pytest

from projectkoios.physkit.thermal.statmech.qm import FermiDiracState
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestFermiDiracStateEvaluateOccupations:
    """Verify stable finite-level Fermi--Dirac occupations."""

    @staticmethod
    def _state(
        *,
        thermal_energy: float,
        chemical_potential: float,
        unit: PhysicalUnit,
    ) -> FermiDiracState:
        return FermiDiracState(
            thermal_energy=ScalarQuantity(
                magnitude=thermal_energy,
                unit=unit,
            ),
            chemical_potential=ScalarQuantity(
                magnitude=chemical_potential,
                unit=unit,
            ),
        )

    def test__evaluate_occupations_matches_particle_hole_symmetry(self) -> None:
        unit = PhysicalUnit(expression="electron_volt")
        state = self._state(
            thermal_energy=0.1,
            chemical_potential=1.0,
            unit=unit,
        )
        energies = VectorQuantity(
            magnitude=np.array([0.9, 1.0, 1.1], dtype=np.float64),
            unit=unit,
        )

        evaluation = state.evaluate_occupations(energies=energies)

        assert evaluation.request.state is state
        assert evaluation.request.energies is energies
        assert isinstance(evaluation.occupations.unit, Unitless)
        assert evaluation.occupations.magnitude[1] == 0.5
        assert np.isclose(
            evaluation.occupations.magnitude[0] + evaluation.occupations.magnitude[2],
            1.0,
            rtol=0.0,
            atol=2e-16,
        )

    def test__evaluate_occupations_remains_finite_for_extreme_arguments(self) -> None:
        unit = PhysicalUnit(expression="joule")
        state = self._state(
            thermal_energy=1.0,
            chemical_potential=0.0,
            unit=unit,
        )

        evaluation = state.evaluate_occupations(
            energies=VectorQuantity(
                magnitude=np.array([-1000.0, 1000.0], dtype=np.float64),
                unit=unit,
            )
        )

        np.testing.assert_array_equal(
            evaluation.occupations.magnitude,
            np.array([1.0, 0.0], dtype=np.float64),
        )

    def test__evaluate_occupations_rejects_a_different_energy_unit(self) -> None:
        state = self._state(
            thermal_energy=1.0,
            chemical_potential=0.0,
            unit=PhysicalUnit(expression="joule"),
        )

        with pytest.raises(ValueError, match="must use the Fermi-Dirac energy unit"):
            state.evaluate_occupations(
                energies=VectorQuantity(
                    magnitude=np.array([1.0], dtype=np.float64),
                    unit=PhysicalUnit(expression="electron_volt"),
                )
            )
