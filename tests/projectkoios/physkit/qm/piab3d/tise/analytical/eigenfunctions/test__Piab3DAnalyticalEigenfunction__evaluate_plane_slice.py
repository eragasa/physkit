"""Tests for analytical PIAB3D Cartesian-plane evaluation."""

import numpy as np
import pytest

from projectkoios.physkit.qm.piab3d.base import Piab3D
from projectkoios.physkit.qm.piab3d.tise.analytical.eigenfunctions import (
    Piab3DAnalyticalEigenfunction,
    Piab3DPlaneNormal,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    UnitSystem,
    VectorQuantity,
)


class TestPiab3DAnalyticalEigenfunctionExecute:
    """Verify slice weights, axis mapping, units, conversion, and validation."""

    BOX_LENGTH = 1.0
    PARTICLE_MASS = 1.0
    GROUND_QUANTUM_NUMBER = 1
    SECOND_QUANTUM_NUMBER = 2
    MIDPLANE_COORDINATE = 0.5
    NORMALIZATION_TOLERANCE = 3e-15
    NODE_TOLERANCE = 4e-16

    @classmethod
    def unit_cube(cls, unit_system: UnitSystem) -> Piab3D:
        """Return a unit-cube PIAB3D model in the selected unit system."""
        return Piab3D(
            length_x=cls.BOX_LENGTH,
            length_y=cls.BOX_LENGTH,
            length_z=cls.BOX_LENGTH,
            mass=cls.PARTICLE_MASS,
            unit_system=unit_system,
        )

    @classmethod
    def midpoint_coordinate(cls) -> ScalarQuantity:
        """Return the nondimensional unit-cube midpoint."""
        return ScalarQuantity(
            magnitude=cls.MIDPLANE_COORDINATE,
            unit=Unitless(),
        )

    def test__execute__evaluates_ground_state_z_midplane(self) -> None:
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

        result = Piab3DAnalyticalEigenfunction(
            model=self.unit_cube(unit_system=UnitSystem.NONDIMENSIONAL),
            quantum_number_x=self.GROUND_QUANTUM_NUMBER,
            quantum_number_y=self.GROUND_QUANTUM_NUMBER,
            quantum_number_z=self.GROUND_QUANTUM_NUMBER,
        ).evaluate_plane_slice(
            plane_normal=Piab3DPlaneNormal.Z,
            coordinates_u=coordinates,
            coordinates_v=coordinates,
            fixed_coordinate=self.midpoint_coordinate(),
        )
        density = result.probability_density.magnitude
        integrated_v = np.trapezoid(density, x=coordinate_values, axis=1)
        represented_slice_density = float(
            np.trapezoid(integrated_v, x=coordinate_values)
        )
        midpoint_index = (sample_count - 1) // 2
        expected_midpoint_amplitude = np.sqrt(
            8.0
            / (result.model.length_x * result.model.length_y * result.model.length_z)
        )

        assert result.in_plane_axis_labels == ("x", "y")
        assert result.amplitudes.magnitude.shape == (sample_count, sample_count)
        assert np.isclose(
            result.amplitudes.magnitude[midpoint_index, midpoint_index],
            expected_midpoint_amplitude,
        )
        assert np.allclose(result.amplitudes.magnitude[[0, -1], :], 0.0)
        assert np.allclose(result.amplitudes.magnitude[:, [0, -1]], 0.0)
        assert np.isclose(
            represented_slice_density,
            result.expected_integrated_density.magnitude,
            rtol=0.0,
            atol=self.NORMALIZATION_TOLERANCE,
        )
        assert isinstance(result.amplitudes.unit, Unitless)

    @pytest.mark.parametrize(
        ("normal", "labels"),
        [
            (Piab3DPlaneNormal.X, ("y", "z")),
            (Piab3DPlaneNormal.Y, ("x", "z")),
            (Piab3DPlaneNormal.Z, ("x", "y")),
        ],
    )
    def test__execute__maps_each_plane_to_deterministic_in_plane_axes(
        self,
        normal: Piab3DPlaneNormal,
        labels: tuple[str, str],
    ) -> None:
        coordinate_values = np.array(
            [0.0, self.MIDPLANE_COORDINATE, self.BOX_LENGTH],
            dtype=np.float64,
        )
        coordinates = VectorQuantity(
            magnitude=coordinate_values,
            unit=Unitless(),
        )

        result = Piab3DAnalyticalEigenfunction(
            model=self.unit_cube(unit_system=UnitSystem.NONDIMENSIONAL),
            quantum_number_x=self.GROUND_QUANTUM_NUMBER,
            quantum_number_y=self.GROUND_QUANTUM_NUMBER,
            quantum_number_z=self.GROUND_QUANTUM_NUMBER,
        ).evaluate_plane_slice(
            plane_normal=normal,
            coordinates_u=coordinates,
            coordinates_v=coordinates,
            fixed_coordinate=self.midpoint_coordinate(),
        )
        midpoint_index = 1
        expected_midpoint_amplitude = np.sqrt(
            8.0
            / (result.model.length_x * result.model.length_y * result.model.length_z)
        )
        expected_integrated_density = ScalarQuantity(
            magnitude=2.0 / self.BOX_LENGTH,
            unit=Unitless(),
        )

        assert result.in_plane_axis_labels == labels
        assert np.isclose(
            result.amplitudes.magnitude[midpoint_index, midpoint_index],
            expected_midpoint_amplitude,
        )
        assert result.expected_integrated_density == expected_integrated_density

    def test__execute__converts_plane_coordinates_and_returns_physical_unit(
        self,
    ) -> None:
        centimeter_coordinates = VectorQuantity(
            magnitude=np.array([0.0, 50.0, 100.0], dtype=np.float64),
            unit=PhysicalUnit(expression="centimeter"),
        )
        meter_coordinates = VectorQuantity(
            magnitude=np.array(
                [0.0, self.MIDPLANE_COORDINATE, self.BOX_LENGTH],
                dtype=np.float64,
            ),
            unit=PhysicalUnit(expression="meter"),
        )
        fixed_coordinate = ScalarQuantity(
            magnitude=50.0,
            unit=PhysicalUnit(expression="centimeter"),
        )

        result = Piab3DAnalyticalEigenfunction(
            model=self.unit_cube(unit_system=UnitSystem.SI),
            quantum_number_x=self.GROUND_QUANTUM_NUMBER,
            quantum_number_y=self.GROUND_QUANTUM_NUMBER,
            quantum_number_z=self.GROUND_QUANTUM_NUMBER,
        ).evaluate_plane_slice(
            plane_normal=Piab3DPlaneNormal.X,
            coordinates_u=centimeter_coordinates,
            coordinates_v=meter_coordinates,
            fixed_coordinate=fixed_coordinate,
        )
        midpoint_index = 1
        expected_midpoint_amplitude = np.sqrt(
            8.0
            / (result.model.length_x * result.model.length_y * result.model.length_z)
        )

        assert np.isclose(
            result.amplitudes.magnitude[midpoint_index, midpoint_index],
            expected_midpoint_amplitude,
        )
        assert result.fixed_coordinate == ScalarQuantity(
            magnitude=self.MIDPLANE_COORDINATE,
            unit=PhysicalUnit(expression="meter"),
        )
        assert result.amplitudes.unit == PhysicalUnit(expression="(meter) ** -1.5")
        assert result.probability_density.unit == PhysicalUnit(
            expression="((meter) ** -1.5) ** 2"
        )
        assert result.expected_integrated_density.unit == PhysicalUnit(
            expression="(meter) ** -1"
        )

    def test__execute__returns_zero_slice_on_normal_direction_node(self) -> None:
        sample_count = 21
        coordinates = VectorQuantity(
            magnitude=np.linspace(
                0.0,
                self.BOX_LENGTH,
                sample_count,
                dtype=np.float64,
            ),
            unit=Unitless(),
        )

        result = Piab3DAnalyticalEigenfunction(
            model=self.unit_cube(unit_system=UnitSystem.NONDIMENSIONAL),
            quantum_number_x=self.SECOND_QUANTUM_NUMBER,
            quantum_number_y=self.GROUND_QUANTUM_NUMBER,
            quantum_number_z=self.GROUND_QUANTUM_NUMBER,
        ).evaluate_plane_slice(
            plane_normal=Piab3DPlaneNormal.X,
            coordinates_u=coordinates,
            coordinates_v=coordinates,
            fixed_coordinate=self.midpoint_coordinate(),
        )

        assert np.allclose(
            result.amplitudes.magnitude,
            0.0,
            atol=self.NODE_TOLERANCE,
        )

    def test__execute__rejects_boolean_quantum_number(self) -> None:
        invalid_quantum_number = True
        coordinates = VectorQuantity(
            magnitude=np.array(
                [self.MIDPLANE_COORDINATE],
                dtype=np.float64,
            ),
            unit=Unitless(),
        )

        with pytest.raises(TypeError, match="must be a built-in integer"):
            Piab3DAnalyticalEigenfunction(
                model=self.unit_cube(unit_system=UnitSystem.NONDIMENSIONAL),
                quantum_number_x=invalid_quantum_number,
                quantum_number_y=self.GROUND_QUANTUM_NUMBER,
                quantum_number_z=self.GROUND_QUANTUM_NUMBER,
            ).evaluate_plane_slice(
                plane_normal=Piab3DPlaneNormal.Z,
                coordinates_u=coordinates,
                coordinates_v=coordinates,
                fixed_coordinate=self.midpoint_coordinate(),
            )

    def test__execute__rejects_fixed_coordinate_outside_box(self) -> None:
        outside_box_coordinate = self.BOX_LENGTH + self.MIDPLANE_COORDINATE
        coordinates = VectorQuantity(
            magnitude=np.array(
                [self.MIDPLANE_COORDINATE],
                dtype=np.float64,
            ),
            unit=Unitless(),
        )

        with pytest.raises(ValueError, match="fixed_coordinate must lie"):
            Piab3DAnalyticalEigenfunction(
                model=self.unit_cube(unit_system=UnitSystem.NONDIMENSIONAL),
                quantum_number_x=self.GROUND_QUANTUM_NUMBER,
                quantum_number_y=self.GROUND_QUANTUM_NUMBER,
                quantum_number_z=self.GROUND_QUANTUM_NUMBER,
            ).evaluate_plane_slice(
                plane_normal=Piab3DPlaneNormal.Z,
                coordinates_u=coordinates,
                coordinates_v=coordinates,
                fixed_coordinate=ScalarQuantity(
                    magnitude=outside_box_coordinate,
                    unit=Unitless(),
                ),
            )
