"""Projection tests for ``SampledEigenfunctions1D``."""

import numpy as np
import pytest

from projectkoios.physkit.qm.eigenfunctions import (
    SampledEigenfunction1D,
    SampledEigenfunctions1D,
)
from projectkoios.physkit.qm.sampled_states import SampledQuantumState1D
from projectkoios.physkit.units import (
    ComplexVectorQuantity,
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestSampledEigenfunctions1DProject:
    """Verify weighted projection onto iterable sampled eigenvectors."""

    @staticmethod
    def _eigenfunctions(
        *,
        coordinates: VectorQuantity,
        amplitude_unit: PhysicalUnit | Unitless,
    ) -> SampledEigenfunctions1D:
        basis_values = np.sqrt(2.0) * np.eye(2, dtype=np.complex128)
        return SampledEigenfunctions1D(
            eigenfunctions=tuple(
                SampledEigenfunction1D(
                    eigenvalue=ScalarQuantity(
                        magnitude=float(index + 1),
                        unit=Unitless(),
                    ),
                    coordinates=coordinates,
                    amplitudes=ComplexVectorQuantity(
                        magnitude=basis_values[:, index],
                        unit=amplitude_unit,
                    ),
                )
                for index in range(basis_values.shape[1])
            )
        )

    def test__project_recovers_weighted_orthonormal_coefficients(self) -> None:
        amplitude_unit = PhysicalUnit(expression="meter ** -0.5")
        coordinate_values = np.array([0.0, 0.5], dtype=np.float64)
        coordinates = VectorQuantity(
            magnitude=coordinate_values,
            unit=PhysicalUnit(expression="meter"),
        )
        eigenfunctions = self._eigenfunctions(
            coordinates=coordinates,
            amplitude_unit=amplitude_unit,
        )
        expected_coefficients = np.array(
            [1.0 / np.sqrt(2.0), 1.0j / np.sqrt(2.0)],
            dtype=np.complex128,
        )
        state = SampledQuantumState1D(
            coordinates=coordinates,
            amplitudes=ComplexVectorQuantity(
                magnitude=(
                    eigenfunctions.amplitude_matrix.magnitude @ expected_coefficients
                ),
                unit=amplitude_unit,
            ),
        )
        quadrature_weights = VectorQuantity(
            magnitude=np.array([0.5, 0.5], dtype=np.float64),
            unit=PhysicalUnit(expression="meter"),
        )

        projection = eigenfunctions.project(
            state=state,
            quadrature_weights=quadrature_weights,
        )

        np.testing.assert_allclose(
            projection.coefficients.magnitude,
            expected_coefficients,
            rtol=0.0,
            atol=2.0e-16,
        )
        np.testing.assert_allclose(
            projection.probabilities.magnitude,
            np.array([0.5, 0.5], dtype=np.float64),
            rtol=0.0,
            atol=2.0e-16,
        )
        assert np.isclose(projection.represented_probability, 1.0)

    def test__project_rejects_incoherent_inner_product_units(self) -> None:
        sample_count = 2
        coordinates = VectorQuantity(
            magnitude=np.arange(sample_count, dtype=np.float64),
            unit=Unitless(),
        )
        eigenfunctions = self._eigenfunctions(
            coordinates=coordinates,
            amplitude_unit=Unitless(),
        )
        state = SampledQuantumState1D(
            coordinates=coordinates,
            amplitudes=ComplexVectorQuantity(
                magnitude=np.ones(sample_count, dtype=np.complex128),
                unit=Unitless(),
            ),
        )

        with pytest.raises(ValueError, match="dimensionless inner products"):
            eigenfunctions.project(
                state=state,
                quadrature_weights=VectorQuantity(
                    magnitude=np.ones(sample_count, dtype=np.float64),
                    unit=PhysicalUnit(expression="meter"),
                ),
            )

    def test__project_rejects_different_representation_coordinates(self) -> None:
        sample_count = 2
        basis_coordinates = VectorQuantity(
            magnitude=np.arange(sample_count, dtype=np.float64),
            unit=Unitless(),
        )
        state_coordinates = VectorQuantity(
            magnitude=np.arange(sample_count, dtype=np.float64),
            unit=Unitless(),
        )
        eigenfunctions = self._eigenfunctions(
            coordinates=basis_coordinates,
            amplitude_unit=Unitless(),
        )
        state = SampledQuantumState1D(
            coordinates=state_coordinates,
            amplitudes=ComplexVectorQuantity(
                magnitude=np.ones(sample_count, dtype=np.complex128),
                unit=Unitless(),
            ),
        )

        with pytest.raises(ValueError, match="must share coordinates"):
            eigenfunctions.project(
                state=state,
                quadrature_weights=VectorQuantity(
                    magnitude=np.ones(sample_count, dtype=np.float64),
                    unit=Unitless(),
                ),
            )
