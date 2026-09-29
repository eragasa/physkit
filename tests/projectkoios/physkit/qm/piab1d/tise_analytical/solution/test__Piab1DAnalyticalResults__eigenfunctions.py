"""Eigenfunction tests for ``Piab1DAnalyticalResults``."""

import numpy as np
import pytest

from projectkoios.physkit.qm.piab1d.base import Piab1D
from projectkoios.physkit.qm.piab1d.tise_analytical.solution import (
    Piab1DAnalyticalSolution,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    Unitless,
    UnitSystem,
    VectorQuantity,
)


class TestPiab1DAnalyticalResultsEigenfunctions:
    """Verify ordered normalized stationary-eigenvector evaluation."""

    UNIT_LENGTH = 1.0
    UNIT_MASS = 1.0
    NUMERICAL_TOLERANCE = 2.0e-16

    @classmethod
    def model(cls, *, unit_system: UnitSystem) -> Piab1D:
        """Return a unit-length model in the selected unit system."""
        return Piab1D(
            length=cls.UNIT_LENGTH,
            mass=cls.UNIT_MASS,
            unit_system=unit_system,
        )

    def test__eigenfunctions_returns_an_ordered_iterable_of_sine_modes(self) -> None:
        represented_mode_count = 2
        results = Piab1DAnalyticalSolution(
            model=self.model(unit_system=UnitSystem.NONDIMENSIONAL)
        ).evaluate(count=represented_mode_count)
        coordinate_values = np.array(
            [0.0, 0.25, 0.5, 0.75, self.UNIT_LENGTH],
            dtype=np.float64,
        )
        coordinates = VectorQuantity(
            magnitude=coordinate_values,
            unit=Unitless(),
        )

        eigenfunctions = results.eigenfunctions(coordinates=coordinates)

        expected = np.sqrt(2.0) * np.column_stack(
            (
                np.sin(np.pi * coordinates.magnitude),
                np.sin(2.0 * np.pi * coordinates.magnitude),
            )
        )
        assert len(eigenfunctions) == represented_mode_count
        assert tuple(
            eigenfunction.eigenvalue.magnitude for eigenfunction in eigenfunctions
        ) == tuple(results.energies.magnitude)
        np.testing.assert_allclose(
            eigenfunctions.amplitude_matrix.magnitude,
            expected,
            rtol=0.0,
            atol=self.NUMERICAL_TOLERANCE,
        )
        assert isinstance(eigenfunctions.amplitude_matrix.unit, Unitless)

    def test__eigenfunctions_converts_coordinates_to_model_length_unit(self) -> None:
        results = Piab1DAnalyticalSolution(
            model=self.model(unit_system=UnitSystem.SI)
        ).evaluate(count=1)
        centimeter_coordinates = VectorQuantity(
            magnitude=np.array([0.0, 50.0, 100.0], dtype=np.float64),
            unit=PhysicalUnit(expression="centimeter"),
        )

        eigenfunctions = results.eigenfunctions(
            coordinates=centimeter_coordinates,
        )

        midpoint_index = 1
        ground_state = next(iter(eigenfunctions))
        assert np.isclose(
            ground_state.amplitudes.magnitude[midpoint_index],
            np.sqrt(2.0),
            rtol=0.0,
            atol=self.NUMERICAL_TOLERANCE,
        )
        assert ground_state.amplitudes.unit == PhysicalUnit(
            expression="(meter) ** -0.5"
        )

    def test__eigenfunctions_rejects_coordinates_outside_box(self) -> None:
        results = Piab1DAnalyticalSolution(
            model=self.model(unit_system=UnitSystem.NONDIMENSIONAL)
        ).evaluate(count=1)
        outside_coordinate = -0.1
        coordinates = VectorQuantity(
            magnitude=np.array(
                [outside_coordinate, self.UNIT_LENGTH / 2.0],
                dtype=np.float64,
            ),
            unit=Unitless(),
        )

        with pytest.raises(ValueError, match="closed box interval"):
            results.eigenfunctions(coordinates=coordinates)
