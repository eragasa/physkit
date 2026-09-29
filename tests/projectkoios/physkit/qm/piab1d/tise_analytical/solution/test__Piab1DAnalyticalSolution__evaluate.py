"""Verification of ``Piab1DAnalyticalSolution.evaluate``."""

import numpy as np
import pytest

from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.qm.piab1d.base import Piab1D
from projectkoios.physkit.qm.piab1d.tise_analytical import (
    Piab1DAnalyticalResults,
    Piab1DAnalyticalSolution,
)
from projectkoios.physkit.units import PhysicalUnit, Unitless, UnitSystem


class TestPiab1DAnalyticalSolutionEvaluate:
    """Verify closed-form energies, units, and input validation."""

    UNIT_LENGTH = 1.0
    UNIT_MASS = 1.0
    GROUND_MODE_COUNT = 1

    @classmethod
    def model(
        cls,
        *,
        length: float = UNIT_LENGTH,
        mass: float = UNIT_MASS,
        unit_system: UnitSystem = UnitSystem.NONDIMENSIONAL,
    ) -> Piab1D:
        """Return a PIAB1D model with explicit parameters."""
        return Piab1D(
            length=length,
            mass=mass,
            unit_system=unit_system,
        )

    def test__evaluate__returns_nondimensional_closed_form_results(self) -> None:
        represented_mode_count = 3
        solution = Piab1DAnalyticalSolution(model=self.model())

        results = solution.evaluate(count=represented_mode_count)

        expected_quantum_numbers = np.arange(
            self.GROUND_MODE_COUNT,
            represented_mode_count + self.GROUND_MODE_COUNT,
            dtype=np.int64,
        )
        expected_energy_coefficients = (
            expected_quantum_numbers.astype(np.float64) ** 2 / 2.0
        )
        assert isinstance(results, ResultsObject)
        assert isinstance(results, Piab1DAnalyticalResults)
        np.testing.assert_array_equal(
            results.quantum_numbers,
            expected_quantum_numbers,
        )
        np.testing.assert_array_equal(
            results.energies.magnitude,
            np.pi**2 * expected_energy_coefficients,
        )
        assert isinstance(results.energies.unit, Unitless)

    def test__evaluate__returns_well_scaled_metal_energies(self) -> None:
        box_length_angstrom = 10.0
        electron_mass_dalton = 5.485_799_090_65e-4
        represented_mode_count = 2
        solution = Piab1DAnalyticalSolution(
            model=self.model(
                length=box_length_angstrom,
                mass=electron_mass_dalton,
                unit_system=UnitSystem.METAL,
            )
        )

        results = solution.evaluate(count=represented_mode_count)

        expected_energies_electron_volt = np.array(
            [0.376_030_162_3, 1.504_120_649_2],
            dtype=np.float64,
        )
        assert results.energies.unit == PhysicalUnit(expression="electron_volt")
        np.testing.assert_allclose(
            results.energies.magnitude,
            expected_energies_electron_volt,
            rtol=2.0e-9,
            atol=0.0,
        )

    def test__evaluate__validates_model_and_count(self) -> None:
        with pytest.raises(TypeError, match="Piab1D"):
            Piab1DAnalyticalSolution(
                model=object(),  # type: ignore[arg-type]
            )

        solution = Piab1DAnalyticalSolution(model=self.model())
        invalid_boolean_count = True
        nonpositive_count = 0
        with pytest.raises(TypeError, match="built-in int"):
            solution.evaluate(count=invalid_boolean_count)
        with pytest.raises(ValueError, match="positive"):
            solution.evaluate(count=nonpositive_count)
