"""Tests for analytical PIAB2D eigenfunction evaluation correlation."""

import numpy as np
import pytest

from projectkoios.physkit.qm.piab2d.base import Piab2D
from projectkoios.physkit.qm.piab2d.tise.analytical.eigenfunctions import (
    Piab2DAnalyticalEigenfunction,
    Piab2DAnalyticalEigenfunctionEvaluation,
    Piab2DAnalyticalEigenfunctionEvaluationRequest,
)
from projectkoios.physkit.units import (
    MatrixQuantity,
    PhysicalUnit,
    Unitless,
    UnitSystem,
    VectorQuantity,
)


class TestPiab2DAnalyticalEigenfunctionEvaluationInit:
    """Verify sampled-grid and amplitude correlation invariants."""

    GROUND_QUANTUM_NUMBER = 1
    UNIT_LENGTH = 1.0
    UNIT_MASS = 1.0

    @classmethod
    def _request(
        cls,
        *,
        coordinates_x: VectorQuantity,
        coordinates_y: VectorQuantity,
    ) -> Piab2DAnalyticalEigenfunctionEvaluationRequest:
        eigenfunction = Piab2DAnalyticalEigenfunction(
            model=Piab2D(
                length_x=cls.UNIT_LENGTH,
                length_y=cls.UNIT_LENGTH,
                mass=cls.UNIT_MASS,
                unit_system=UnitSystem.NONDIMENSIONAL,
            ),
            quantum_number_x=cls.GROUND_QUANTUM_NUMBER,
            quantum_number_y=cls.GROUND_QUANTUM_NUMBER,
        )
        return Piab2DAnalyticalEigenfunctionEvaluationRequest(
            eigenfunction=eigenfunction,
            coordinates_x=coordinates_x,
            coordinates_y=coordinates_y,
        )

    @staticmethod
    def _coordinates(values: list[float]) -> VectorQuantity:
        return VectorQuantity(
            magnitude=np.array(values, dtype=np.float64),
            unit=Unitless(),
        )

    def test__init_rejects_grid_shape_mismatch(self) -> None:
        boundary_coordinates = self._coordinates([0.0, self.UNIT_LENGTH])
        mismatched_shape = (2, 3)
        request = self._request(
            coordinates_x=boundary_coordinates,
            coordinates_y=boundary_coordinates,
        )

        with pytest.raises(ValueError, match="must match the rectangular grid"):
            Piab2DAnalyticalEigenfunctionEvaluation(
                request=request,
                coordinates_x=boundary_coordinates,
                coordinates_y=boundary_coordinates,
                amplitudes=MatrixQuantity(
                    magnitude=np.zeros(mismatched_shape, dtype=np.float64),
                    unit=Unitless(),
                ),
            )

    def test__init_rejects_incorrect_amplitude_unit(self) -> None:
        midpoint_coordinates = self._coordinates([self.UNIT_LENGTH / 2.0])
        request = self._request(
            coordinates_x=midpoint_coordinates,
            coordinates_y=midpoint_coordinates,
        )

        with pytest.raises(ValueError, match="normalized eigenfunction unit"):
            Piab2DAnalyticalEigenfunctionEvaluation(
                request=request,
                coordinates_x=midpoint_coordinates,
                coordinates_y=midpoint_coordinates,
                amplitudes=MatrixQuantity(
                    magnitude=np.ones((1, 1), dtype=np.float64),
                    unit=PhysicalUnit(expression="meter ** -1"),
                ),
            )
