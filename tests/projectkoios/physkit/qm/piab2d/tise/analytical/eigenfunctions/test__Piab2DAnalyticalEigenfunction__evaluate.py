"""Tests for analytical PIAB2D stationary eigenfunction evaluation."""

import numpy as np
import pytest

from projectkoios.physkit.qm.piab2d.base import Piab2D
from projectkoios.physkit.qm.piab2d.tise.analytical.eigenfunctions import (
    Piab2DAnalyticalEigenfunction,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    Unitless,
    UnitSystem,
    VectorQuantity,
)


class TestPiab2DAnalyticalEigenfunctionExecute:
    """Verify normalization, boundaries, units, conversion, and validation."""

    BOX_LENGTH = 1.0
    PARTICLE_MASS = 1.0
    GROUND_QUANTUM_NUMBER = 1
    SECOND_QUANTUM_NUMBER = 2
    MIDPOINT_COORDINATE = 0.5
    NORMALIZATION_TOLERANCE = 2e-15
    NODE_TOLERANCE = 3e-16

    @classmethod
    def unit_square(cls, unit_system: UnitSystem) -> Piab2D:
        """Return a unit-square PIAB2D model in the selected unit system."""
        return Piab2D(
            length_x=cls.BOX_LENGTH,
            length_y=cls.BOX_LENGTH,
            mass=cls.PARTICLE_MASS,
            unit_system=unit_system,
        )

    def test__execute__evaluates_normalized_ground_state(self) -> None:
        sample_count = 401
        coordinate_values = np.linspace(
            0.0,
            self.BOX_LENGTH,
            sample_count,
            dtype=np.float64,
        )
        coordinates = VectorQuantity(
            magnitude=coordinate_values,
            unit=Unitless(),
        )

        result = Piab2DAnalyticalEigenfunction(
            model=self.unit_square(unit_system=UnitSystem.NONDIMENSIONAL),
            quantum_number_x=self.GROUND_QUANTUM_NUMBER,
            quantum_number_y=self.GROUND_QUANTUM_NUMBER,
        ).evaluate(coordinates_x=coordinates, coordinates_y=coordinates)
        density = result.probability_density.magnitude
        integrated_y = np.trapezoid(density, x=coordinate_values, axis=1)
        represented_norm = float(np.trapezoid(integrated_y, x=coordinate_values))
        midpoint_index = (sample_count - 1) // 2
        expected_midpoint_amplitude = 2.0 / np.sqrt(
            result.model.length_x * result.model.length_y
        )

        assert result.amplitudes.magnitude.shape == (sample_count, sample_count)
        assert np.isclose(
            result.amplitudes.magnitude[midpoint_index, midpoint_index],
            expected_midpoint_amplitude,
        )
        assert np.allclose(result.amplitudes.magnitude[[0, -1], :], 0.0)
        assert np.allclose(result.amplitudes.magnitude[:, [0, -1]], 0.0)
        assert np.isclose(
            represented_norm,
            1.0,
            rtol=0.0,
            atol=self.NORMALIZATION_TOLERANCE,
        )
        assert isinstance(result.amplitudes.unit, Unitless)

    def test__execute__represents_higher_state_internal_node(self) -> None:
        quarter_coordinate = self.BOX_LENGTH / 4.0
        three_quarter_coordinate = 3.0 * self.BOX_LENGTH / 4.0
        coordinates = VectorQuantity(
            magnitude=np.array(
                [
                    0.0,
                    quarter_coordinate,
                    self.MIDPOINT_COORDINATE,
                    three_quarter_coordinate,
                    self.BOX_LENGTH,
                ],
                dtype=np.float64,
            ),
            unit=Unitless(),
        )

        result = Piab2DAnalyticalEigenfunction(
            model=self.unit_square(unit_system=UnitSystem.NONDIMENSIONAL),
            quantum_number_x=self.SECOND_QUANTUM_NUMBER,
            quantum_number_y=self.GROUND_QUANTUM_NUMBER,
        ).evaluate(coordinates_x=coordinates, coordinates_y=coordinates)
        node_index = 2
        quarter_index = 1
        midpoint_index = 2
        expected_antinode_amplitude = 2.0 / np.sqrt(
            result.model.length_x * result.model.length_y
        )

        assert np.allclose(
            result.amplitudes.magnitude[node_index, :],
            0.0,
            atol=self.NODE_TOLERANCE,
        )
        assert np.isclose(
            result.amplitudes.magnitude[quarter_index, midpoint_index],
            expected_antinode_amplitude,
        )

    def test__execute__converts_coordinates_and_returns_physical_unit(self) -> None:
        centimeter_coordinates = VectorQuantity(
            magnitude=np.array([0.0, 50.0, 100.0], dtype=np.float64),
            unit=PhysicalUnit(expression="centimeter"),
        )
        meter_coordinates = VectorQuantity(
            magnitude=np.array(
                [0.0, self.MIDPOINT_COORDINATE, self.BOX_LENGTH],
                dtype=np.float64,
            ),
            unit=PhysicalUnit(expression="meter"),
        )

        result = Piab2DAnalyticalEigenfunction(
            model=self.unit_square(unit_system=UnitSystem.SI),
            quantum_number_x=self.GROUND_QUANTUM_NUMBER,
            quantum_number_y=self.GROUND_QUANTUM_NUMBER,
        ).evaluate(
            coordinates_x=centimeter_coordinates, coordinates_y=meter_coordinates
        )
        midpoint_index = 1
        expected_midpoint_amplitude = 2.0 / np.sqrt(
            result.model.length_x * result.model.length_y
        )

        assert np.isclose(
            result.amplitudes.magnitude[midpoint_index, midpoint_index],
            expected_midpoint_amplitude,
        )
        assert result.coordinates_x.unit == PhysicalUnit(expression="meter")
        assert result.amplitudes.unit == PhysicalUnit(expression="(meter) ** -1")
        assert result.probability_density.unit == PhysicalUnit(
            expression="((meter) ** -1) ** 2"
        )

    def test__execute__rejects_boolean_quantum_number(self) -> None:
        invalid_quantum_number = True
        coordinates = VectorQuantity(
            magnitude=np.array([self.MIDPOINT_COORDINATE], dtype=np.float64),
            unit=Unitless(),
        )

        with pytest.raises(TypeError, match="must be a built-in integer"):
            Piab2DAnalyticalEigenfunction(
                model=self.unit_square(unit_system=UnitSystem.NONDIMENSIONAL),
                quantum_number_x=invalid_quantum_number,
                quantum_number_y=self.GROUND_QUANTUM_NUMBER,
            ).evaluate(coordinates_x=coordinates, coordinates_y=coordinates)

    def test__execute__rejects_nonpositive_quantum_number(self) -> None:
        nonpositive_quantum_number = 0
        coordinates = VectorQuantity(
            magnitude=np.array([self.MIDPOINT_COORDINATE], dtype=np.float64),
            unit=Unitless(),
        )

        with pytest.raises(ValueError, match="quantum_number_y must be positive"):
            Piab2DAnalyticalEigenfunction(
                model=self.unit_square(unit_system=UnitSystem.NONDIMENSIONAL),
                quantum_number_x=self.GROUND_QUANTUM_NUMBER,
                quantum_number_y=nonpositive_quantum_number,
            ).evaluate(coordinates_x=coordinates, coordinates_y=coordinates)

    def test__execute__rejects_coordinate_outside_box(self) -> None:
        outside_box_coordinate = -self.MIDPOINT_COORDINATE
        outside_coordinates = VectorQuantity(
            magnitude=np.array([outside_box_coordinate], dtype=np.float64),
            unit=Unitless(),
        )
        inside_coordinates = VectorQuantity(
            magnitude=np.array([self.MIDPOINT_COORDINATE], dtype=np.float64),
            unit=Unitless(),
        )

        with pytest.raises(ValueError, match="coordinates_x must lie"):
            Piab2DAnalyticalEigenfunction(
                model=self.unit_square(unit_system=UnitSystem.NONDIMENSIONAL),
                quantum_number_x=self.GROUND_QUANTUM_NUMBER,
                quantum_number_y=self.GROUND_QUANTUM_NUMBER,
            ).evaluate(
                coordinates_x=outside_coordinates, coordinates_y=inside_coordinates
            )
