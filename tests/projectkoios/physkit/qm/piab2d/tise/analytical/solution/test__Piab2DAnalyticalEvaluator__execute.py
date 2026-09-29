"""Tests for analytical two-dimensional box evaluation."""

import numpy as np
import pytest

from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.qm.piab2d.base import Piab2D
from projectkoios.physkit.qm.piab2d.tise.analytical.solution import (
    Piab2DAnalyticalEvaluator,
    Piab2DAnalyticalSolution,
)
from projectkoios.physkit.units import PhysicalUnit, Unitless, UnitSystem


class TestPiab2DAnalyticalEvaluatorExecute:
    """Verify formula, ordering, degeneracy, scaling, units, and validation."""

    UNIT_LENGTH = 1.0
    UNIT_MASS = 1.0
    GROUND_QUANTUM_NUMBER = 1
    SECOND_QUANTUM_NUMBER = 2
    THIRD_QUANTUM_NUMBER = 3
    NUMERICAL_TOLERANCE = 2e-15
    METAL_ENERGY_TOLERANCE = 2e-9

    @classmethod
    def square_model(
        cls,
        *,
        length: float,
        mass: float = UNIT_MASS,
        unit_system: UnitSystem = UnitSystem.NONDIMENSIONAL,
    ) -> Piab2D:
        """Return a square PIAB2D model with explicit physical parameters."""
        return Piab2D(
            length_x=length,
            length_y=length,
            mass=mass,
            unit_system=unit_system,
        )

    def test__execute__orders_square_box_states_by_energy_then_pair(self) -> None:
        maximum_quantum_number = self.SECOND_QUANTUM_NUMBER
        result = Piab2DAnalyticalEvaluator().execute(
            model=self.square_model(length=self.UNIT_LENGTH),
            maximum_quantum_number_x=maximum_quantum_number,
            maximum_quantum_number_y=maximum_quantum_number,
        )
        expected_quantum_numbers = np.array(
            [
                [self.GROUND_QUANTUM_NUMBER, self.GROUND_QUANTUM_NUMBER],
                [self.GROUND_QUANTUM_NUMBER, self.SECOND_QUANTUM_NUMBER],
                [self.SECOND_QUANTUM_NUMBER, self.GROUND_QUANTUM_NUMBER],
                [self.SECOND_QUANTUM_NUMBER, self.SECOND_QUANTUM_NUMBER],
            ],
            dtype=np.int64,
        )
        expected_energy_coefficients = np.array(
            [1.0, 2.5, 2.5, 4.0],
            dtype=np.float64,
        )

        assert isinstance(result, ResultsObject)
        assert isinstance(result, Piab2DAnalyticalSolution)
        np.testing.assert_array_equal(
            result.quantum_numbers,
            expected_quantum_numbers,
        )
        np.testing.assert_allclose(
            result.energies.magnitude,
            np.pi**2 * expected_energy_coefficients,
            rtol=self.NUMERICAL_TOLERANCE,
            atol=0.0,
        )
        assert isinstance(result.energies.unit, Unitless)

    def test__execute__retains_square_box_exchange_degeneracy(self) -> None:
        box_length = 2.0
        maximum_quantum_number = self.THIRD_QUANTUM_NUMBER
        result = Piab2DAnalyticalEvaluator().execute(
            model=self.square_model(length=box_length),
            maximum_quantum_number_x=maximum_quantum_number,
            maximum_quantum_number_y=maximum_quantum_number,
        )
        pair_to_energy = {
            tuple(pair): energy
            for pair, energy in zip(
                result.quantum_numbers,
                result.energies.magnitude,
                strict=True,
            )
        }
        first_exchange_pair = (
            self.GROUND_QUANTUM_NUMBER,
            self.SECOND_QUANTUM_NUMBER,
        )
        first_reversed_pair = tuple(reversed(first_exchange_pair))
        second_exchange_pair = (
            self.GROUND_QUANTUM_NUMBER,
            self.THIRD_QUANTUM_NUMBER,
        )
        second_reversed_pair = tuple(reversed(second_exchange_pair))

        assert (
            pair_to_energy[first_exchange_pair] == pair_to_energy[first_reversed_pair]
        )
        assert (
            pair_to_energy[second_exchange_pair] == pair_to_energy[second_reversed_pair]
        )

    def test__execute__uses_both_rectangular_lengths(self) -> None:
        length_x = 2.0
        length_y = 4.0
        particle_mass = 3.0
        model = Piab2D(
            length_x=length_x,
            length_y=length_y,
            mass=particle_mass,
            unit_system=UnitSystem.NONDIMENSIONAL,
        )
        result = Piab2DAnalyticalEvaluator().execute(
            model=model,
            maximum_quantum_number_x=self.GROUND_QUANTUM_NUMBER,
            maximum_quantum_number_y=self.GROUND_QUANTUM_NUMBER,
        )
        expected_ground_energy = (
            np.pi**2 / (2.0 * particle_mass) * (1.0 / length_x**2 + 1.0 / length_y**2)
        )

        assert result.energies.magnitude[0] == pytest.approx(
            expected_ground_energy,
            rel=self.NUMERICAL_TOLERANCE,
        )

    def test__execute__has_inverse_square_uniform_length_scaling(self) -> None:
        evaluator = Piab2DAnalyticalEvaluator()
        length_scale_factor = 2.0
        maximum_quantum_number = self.SECOND_QUANTUM_NUMBER
        unit_box = evaluator.execute(
            model=self.square_model(length=self.UNIT_LENGTH),
            maximum_quantum_number_x=maximum_quantum_number,
            maximum_quantum_number_y=maximum_quantum_number,
        )
        doubled_box = evaluator.execute(
            model=self.square_model(length=length_scale_factor * self.UNIT_LENGTH),
            maximum_quantum_number_x=maximum_quantum_number,
            maximum_quantum_number_y=maximum_quantum_number,
        )

        np.testing.assert_allclose(
            doubled_box.energies.magnitude,
            unit_box.energies.magnitude / length_scale_factor**2,
            rtol=self.NUMERICAL_TOLERANCE,
            atol=0.0,
        )

    def test__execute__returns_well_scaled_metal_energies(self) -> None:
        box_length_angstrom = 10.0
        electron_mass_dalton = 5.485_799_090_65e-4
        maximum_quantum_number = self.SECOND_QUANTUM_NUMBER
        result = Piab2DAnalyticalEvaluator().execute(
            model=self.square_model(
                length=box_length_angstrom,
                mass=electron_mass_dalton,
                unit_system=UnitSystem.METAL,
            ),
            maximum_quantum_number_x=maximum_quantum_number,
            maximum_quantum_number_y=maximum_quantum_number,
        )
        expected_energies_electron_volt = np.array(
            [
                0.752_060_324_6,
                1.880_150_811_5,
                1.880_150_811_5,
                3.008_241_298_4,
            ],
            dtype=np.float64,
        )

        assert result.energies.unit == PhysicalUnit(expression="electron_volt")
        np.testing.assert_allclose(
            result.energies.magnitude,
            expected_energies_electron_volt,
            rtol=self.METAL_ENERGY_TOLERANCE,
            atol=0.0,
        )

    def test__execute__rejects_non_model(self) -> None:
        maximum_quantum_number = self.SECOND_QUANTUM_NUMBER
        with pytest.raises(TypeError, match="model must be Piab2D"):
            Piab2DAnalyticalEvaluator().execute(
                model=None,  # type: ignore[arg-type]
                maximum_quantum_number_x=maximum_quantum_number,
                maximum_quantum_number_y=maximum_quantum_number,
            )

    def test__execute__rejects_boolean_bound(self) -> None:
        invalid_bound = True
        with pytest.raises(TypeError, match="maximum_quantum_number_x"):
            Piab2DAnalyticalEvaluator().execute(
                model=self.square_model(length=self.UNIT_LENGTH),
                maximum_quantum_number_x=invalid_bound,
                maximum_quantum_number_y=self.SECOND_QUANTUM_NUMBER,
            )

    def test__execute__rejects_nonpositive_bound(self) -> None:
        nonpositive_bound = 0
        with pytest.raises(ValueError, match="maximum_quantum_number_y"):
            Piab2DAnalyticalEvaluator().execute(
                model=self.square_model(length=self.UNIT_LENGTH),
                maximum_quantum_number_x=self.SECOND_QUANTUM_NUMBER,
                maximum_quantum_number_y=nonpositive_bound,
            )
