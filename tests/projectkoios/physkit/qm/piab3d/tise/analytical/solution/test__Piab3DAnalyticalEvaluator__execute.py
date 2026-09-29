"""Tests for analytical three-dimensional box evaluation."""

import numpy as np
import pytest

from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.qm.piab3d.base import Piab3D
from projectkoios.physkit.qm.piab3d.tise.analytical.solution import (
    Piab3DAnalyticalEvaluator,
    Piab3DAnalyticalSolution,
)
from projectkoios.physkit.units import PhysicalUnit, Unitless, UnitSystem


class TestPiab3DAnalyticalEvaluatorExecute:
    """Verify formula, ordering, degeneracy, scaling, units, and validation."""

    UNIT_LENGTH = 1.0
    UNIT_MASS = 1.0
    GROUND_QUANTUM_NUMBER = 1
    SECOND_QUANTUM_NUMBER = 2
    THIRD_QUANTUM_NUMBER = 3
    NUMERICAL_TOLERANCE = 2e-15
    METAL_ENERGY_TOLERANCE = 2e-9

    @classmethod
    def cubic_model(
        cls,
        *,
        length: float,
        mass: float = UNIT_MASS,
        unit_system: UnitSystem = UnitSystem.NONDIMENSIONAL,
    ) -> Piab3D:
        """Return a cubic PIAB3D model with explicit physical parameters."""
        return Piab3D(
            length_x=length,
            length_y=length,
            length_z=length,
            mass=mass,
            unit_system=unit_system,
        )

    def test__execute__orders_cubic_box_states_by_energy_then_triple(self) -> None:
        maximum_quantum_number = self.SECOND_QUANTUM_NUMBER
        result = Piab3DAnalyticalEvaluator().execute(
            model=self.cubic_model(length=self.UNIT_LENGTH),
            maximum_quantum_number_x=maximum_quantum_number,
            maximum_quantum_number_y=maximum_quantum_number,
            maximum_quantum_number_z=maximum_quantum_number,
        )
        ground = self.GROUND_QUANTUM_NUMBER
        second = self.SECOND_QUANTUM_NUMBER
        expected_quantum_numbers = np.array(
            [
                [ground, ground, ground],
                [ground, ground, second],
                [ground, second, ground],
                [second, ground, ground],
                [ground, second, second],
                [second, ground, second],
                [second, second, ground],
                [second, second, second],
            ],
            dtype=np.int64,
        )
        expected_energy_coefficients = np.array(
            [1.5, 3.0, 3.0, 3.0, 4.5, 4.5, 4.5, 6.0],
            dtype=np.float64,
        )

        assert isinstance(result, ResultsObject)
        assert isinstance(result, Piab3DAnalyticalSolution)
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

    def test__execute__retains_cubic_permutation_degeneracy(self) -> None:
        box_length = 2.0
        maximum_quantum_number = self.THIRD_QUANTUM_NUMBER
        result = Piab3DAnalyticalEvaluator().execute(
            model=self.cubic_model(length=box_length),
            maximum_quantum_number_x=maximum_quantum_number,
            maximum_quantum_number_y=maximum_quantum_number,
            maximum_quantum_number_z=maximum_quantum_number,
        )
        triple_to_energy = {
            tuple(triple): energy
            for triple, energy in zip(
                result.quantum_numbers,
                result.energies.magnitude,
                strict=True,
            )
        }
        permutation_one = (
            self.GROUND_QUANTUM_NUMBER,
            self.GROUND_QUANTUM_NUMBER,
            self.SECOND_QUANTUM_NUMBER,
        )
        permutation_two = (
            self.GROUND_QUANTUM_NUMBER,
            self.SECOND_QUANTUM_NUMBER,
            self.GROUND_QUANTUM_NUMBER,
        )
        permutation_three = (
            self.SECOND_QUANTUM_NUMBER,
            self.GROUND_QUANTUM_NUMBER,
            self.GROUND_QUANTUM_NUMBER,
        )

        assert triple_to_energy[permutation_one] == triple_to_energy[permutation_two]
        assert triple_to_energy[permutation_two] == triple_to_energy[permutation_three]

    def test__execute__uses_all_rectangular_lengths(self) -> None:
        length_x = 2.0
        length_y = 4.0
        length_z = 8.0
        particle_mass = 3.0
        model = Piab3D(
            length_x=length_x,
            length_y=length_y,
            length_z=length_z,
            mass=particle_mass,
            unit_system=UnitSystem.NONDIMENSIONAL,
        )
        result = Piab3DAnalyticalEvaluator().execute(
            model=model,
            maximum_quantum_number_x=self.GROUND_QUANTUM_NUMBER,
            maximum_quantum_number_y=self.GROUND_QUANTUM_NUMBER,
            maximum_quantum_number_z=self.GROUND_QUANTUM_NUMBER,
        )
        expected_ground_energy = (
            np.pi**2
            / (2.0 * particle_mass)
            * (1.0 / length_x**2 + 1.0 / length_y**2 + 1.0 / length_z**2)
        )

        assert result.energies.magnitude[0] == pytest.approx(
            expected_ground_energy,
            rel=self.NUMERICAL_TOLERANCE,
        )

    def test__execute__has_inverse_square_uniform_length_scaling(self) -> None:
        evaluator = Piab3DAnalyticalEvaluator()
        length_scale_factor = 2.0
        maximum_quantum_number = self.SECOND_QUANTUM_NUMBER
        unit_box = evaluator.execute(
            model=self.cubic_model(length=self.UNIT_LENGTH),
            maximum_quantum_number_x=maximum_quantum_number,
            maximum_quantum_number_y=maximum_quantum_number,
            maximum_quantum_number_z=maximum_quantum_number,
        )
        doubled_box = evaluator.execute(
            model=self.cubic_model(length=length_scale_factor * self.UNIT_LENGTH),
            maximum_quantum_number_x=maximum_quantum_number,
            maximum_quantum_number_y=maximum_quantum_number,
            maximum_quantum_number_z=maximum_quantum_number,
        )

        np.testing.assert_allclose(
            doubled_box.energies.magnitude,
            unit_box.energies.magnitude / length_scale_factor**2,
            rtol=self.NUMERICAL_TOLERANCE,
            atol=0.0,
        )

    def test__execute__returns_well_scaled_metal_energy(self) -> None:
        box_length_angstrom = 10.0
        electron_mass_dalton = 5.485_799_090_65e-4
        result = Piab3DAnalyticalEvaluator().execute(
            model=self.cubic_model(
                length=box_length_angstrom,
                mass=electron_mass_dalton,
                unit_system=UnitSystem.METAL,
            ),
            maximum_quantum_number_x=self.GROUND_QUANTUM_NUMBER,
            maximum_quantum_number_y=self.GROUND_QUANTUM_NUMBER,
            maximum_quantum_number_z=self.GROUND_QUANTUM_NUMBER,
        )
        expected_ground_energy_electron_volt = 1.128_090_486_9

        assert result.energies.unit == PhysicalUnit(expression="electron_volt")
        assert result.energies.magnitude[0] == pytest.approx(
            expected_ground_energy_electron_volt,
            rel=self.METAL_ENERGY_TOLERANCE,
        )

    def test__execute__rejects_non_model(self) -> None:
        maximum_quantum_number = self.SECOND_QUANTUM_NUMBER
        with pytest.raises(TypeError, match="model must be Piab3D"):
            Piab3DAnalyticalEvaluator().execute(
                model=None,  # type: ignore[arg-type]
                maximum_quantum_number_x=maximum_quantum_number,
                maximum_quantum_number_y=maximum_quantum_number,
                maximum_quantum_number_z=maximum_quantum_number,
            )

    def test__execute__rejects_boolean_bound(self) -> None:
        invalid_bound = True
        with pytest.raises(TypeError, match="maximum_quantum_number_z"):
            Piab3DAnalyticalEvaluator().execute(
                model=self.cubic_model(length=self.UNIT_LENGTH),
                maximum_quantum_number_x=self.SECOND_QUANTUM_NUMBER,
                maximum_quantum_number_y=self.SECOND_QUANTUM_NUMBER,
                maximum_quantum_number_z=invalid_bound,
            )

    def test__execute__rejects_nonpositive_bound(self) -> None:
        nonpositive_bound = 0
        with pytest.raises(ValueError, match="maximum_quantum_number_y"):
            Piab3DAnalyticalEvaluator().execute(
                model=self.cubic_model(length=self.UNIT_LENGTH),
                maximum_quantum_number_x=self.SECOND_QUANTUM_NUMBER,
                maximum_quantum_number_y=nonpositive_bound,
                maximum_quantum_number_z=self.SECOND_QUANTUM_NUMBER,
            )
