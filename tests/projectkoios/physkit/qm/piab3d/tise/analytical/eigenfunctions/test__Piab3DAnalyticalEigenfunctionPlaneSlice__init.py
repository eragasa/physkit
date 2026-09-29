"""Tests for analytical PIAB3D eigenfunction-plane-slice correlation."""

import numpy as np
import pytest

from projectkoios.physkit.qm.piab3d.base import Piab3D
from projectkoios.physkit.qm.piab3d.tise.analytical.eigenfunctions import (
    Piab3DAnalyticalEigenfunction,
    Piab3DAnalyticalEigenfunctionPlaneSlice,
    Piab3DAnalyticalEigenfunctionPlaneSliceEvaluationRequest,
    Piab3DPlaneNormal,
)
from projectkoios.physkit.units import (
    MatrixQuantity,
    ScalarQuantity,
    Unitless,
    UnitSystem,
    VectorQuantity,
)


class TestPiab3DAnalyticalEigenfunctionPlaneSliceInit:
    """Verify sampled-plane and amplitude correlation invariants."""

    GROUND_QUANTUM_NUMBER = 1
    UNIT_LENGTH = 1.0
    UNIT_MASS = 1.0

    @classmethod
    def _eigenfunction(cls) -> Piab3DAnalyticalEigenfunction:
        return Piab3DAnalyticalEigenfunction(
            model=Piab3D(
                length_x=cls.UNIT_LENGTH,
                length_y=cls.UNIT_LENGTH,
                length_z=cls.UNIT_LENGTH,
                mass=cls.UNIT_MASS,
                unit_system=UnitSystem.NONDIMENSIONAL,
            ),
            quantum_number_x=cls.GROUND_QUANTUM_NUMBER,
            quantum_number_y=cls.GROUND_QUANTUM_NUMBER,
            quantum_number_z=cls.GROUND_QUANTUM_NUMBER,
        )

    @staticmethod
    def _coordinates(values: list[float]) -> VectorQuantity:
        return VectorQuantity(
            magnitude=np.array(values, dtype=np.float64),
            unit=Unitless(),
        )

    @classmethod
    def _request(
        cls,
        *,
        coordinates_u: VectorQuantity,
        coordinates_v: VectorQuantity,
        fixed_coordinate: ScalarQuantity,
    ) -> Piab3DAnalyticalEigenfunctionPlaneSliceEvaluationRequest:
        return Piab3DAnalyticalEigenfunctionPlaneSliceEvaluationRequest(
            eigenfunction=cls._eigenfunction(),
            plane_normal=Piab3DPlaneNormal.Z,
            coordinates_u=coordinates_u,
            coordinates_v=coordinates_v,
            fixed_coordinate=fixed_coordinate,
        )

    def test__init_rejects_plane_shape_mismatch(self) -> None:
        boundary_coordinates = self._coordinates([0.0, self.UNIT_LENGTH])
        midpoint_coordinate = ScalarQuantity(
            magnitude=self.UNIT_LENGTH / 2.0,
            unit=Unitless(),
        )
        mismatched_shape = (2, 3)
        request = self._request(
            coordinates_u=boundary_coordinates,
            coordinates_v=boundary_coordinates,
            fixed_coordinate=midpoint_coordinate,
        )

        with pytest.raises(ValueError, match="must match the rectangular plane"):
            Piab3DAnalyticalEigenfunctionPlaneSlice(
                request=request,
                coordinates_u=boundary_coordinates,
                coordinates_v=boundary_coordinates,
                fixed_coordinate=midpoint_coordinate,
                amplitudes=MatrixQuantity(
                    magnitude=np.zeros(mismatched_shape, dtype=np.float64),
                    unit=Unitless(),
                ),
            )

    def test__init_rejects_fixed_coordinate_outside_box(self) -> None:
        midpoint_coordinates = self._coordinates([self.UNIT_LENGTH / 2.0])
        outside_box_coordinate = ScalarQuantity(
            magnitude=2.0 * self.UNIT_LENGTH,
            unit=Unitless(),
        )
        request = self._request(
            coordinates_u=midpoint_coordinates,
            coordinates_v=midpoint_coordinates,
            fixed_coordinate=outside_box_coordinate,
        )

        with pytest.raises(ValueError, match="fixed_coordinate must lie"):
            Piab3DAnalyticalEigenfunctionPlaneSlice(
                request=request,
                coordinates_u=midpoint_coordinates,
                coordinates_v=midpoint_coordinates,
                fixed_coordinate=outside_box_coordinate,
                amplitudes=MatrixQuantity(
                    magnitude=np.ones((1, 1), dtype=np.float64),
                    unit=Unitless(),
                ),
            )
