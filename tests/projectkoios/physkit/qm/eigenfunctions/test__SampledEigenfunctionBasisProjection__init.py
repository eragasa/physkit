"""Construction tests for ``SampledEigenfunctionBasisProjection``."""

import numpy as np
import pytest

from projectkoios.physkit.qm.eigenfunctions import (
    SampledEigenfunction1D,
    SampledEigenfunctionBasisProjection,
    SampledEigenfunctionBasisProjectionRequest,
    SampledEigenfunctions1D,
)
from projectkoios.physkit.qm.sampled_states import SampledQuantumState1D
from projectkoios.physkit.units import (
    ComplexVectorQuantity,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestSampledEigenfunctionBasisProjectionInit:
    """Verify coefficient-probability correlation and represented total."""

    @staticmethod
    def _request(
        *, eigenfunction_count: int
    ) -> SampledEigenfunctionBasisProjectionRequest:
        coordinates = VectorQuantity(
            magnitude=np.arange(eigenfunction_count, dtype=np.float64),
            unit=Unitless(),
        )
        eigenfunctions = SampledEigenfunctions1D(
            eigenfunctions=tuple(
                SampledEigenfunction1D(
                    eigenvalue=ScalarQuantity(
                        magnitude=float(index + 1),
                        unit=Unitless(),
                    ),
                    coordinates=coordinates,
                    amplitudes=ComplexVectorQuantity(
                        magnitude=np.eye(
                            eigenfunction_count,
                            dtype=np.complex128,
                        )[:, index],
                        unit=Unitless(),
                    ),
                )
                for index in range(eigenfunction_count)
            )
        )
        return SampledEigenfunctionBasisProjectionRequest(
            eigenfunctions=eigenfunctions,
            state=SampledQuantumState1D(
                coordinates=coordinates,
                amplitudes=ComplexVectorQuantity(
                    magnitude=np.ones(
                        eigenfunction_count,
                        dtype=np.complex128,
                    ),
                    unit=Unitless(),
                ),
            ),
            quadrature_weights=VectorQuantity(
                magnitude=np.ones(eigenfunction_count, dtype=np.float64),
                unit=Unitless(),
            ),
        )

    def test__init_retains_correlated_vectors(self) -> None:
        coefficient_values = np.array(
            [0.6 + 0.0j, 0.0 + 0.8j],
            dtype=np.complex128,
        )

        projection = SampledEigenfunctionBasisProjection(
            request=self._request(eigenfunction_count=coefficient_values.size),
            coefficients=ComplexVectorQuantity(
                magnitude=coefficient_values,
                unit=Unitless(),
            ),
            probabilities=VectorQuantity(
                magnitude=np.abs(coefficient_values) ** 2,
                unit=Unitless(),
            ),
        )

        assert np.isclose(projection.represented_probability, 1.0)

    def test__init_rejects_uncorrelated_probabilities(self) -> None:
        eigenfunction_count = 1

        with pytest.raises(ValueError, match="must equal squared"):
            SampledEigenfunctionBasisProjection(
                request=self._request(eigenfunction_count=eigenfunction_count),
                coefficients=ComplexVectorQuantity(
                    magnitude=np.array([1.0 + 0.0j], dtype=np.complex128),
                    unit=Unitless(),
                ),
                probabilities=VectorQuantity(
                    magnitude=np.array([0.5], dtype=np.float64),
                    unit=Unitless(),
                ),
            )
