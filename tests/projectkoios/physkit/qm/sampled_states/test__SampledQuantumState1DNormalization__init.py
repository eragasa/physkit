"""Construction tests for ``SampledQuantumState1DNormalization``."""

import numpy as np
import pytest

from projectkoios.physkit.qm.sampled_states import (
    SampledQuantumState1D,
    SampledQuantumState1DNormalization,
    SampledQuantumState1DNormalizationRequest,
)
from projectkoios.physkit.units import (
    ComplexVectorQuantity,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestSampledQuantumState1DNormalizationInit:
    """Verify correlated normalized-state response invariants."""

    @staticmethod
    def _request(
        *,
        sample_count: int,
    ) -> SampledQuantumState1DNormalizationRequest:
        return SampledQuantumState1DNormalizationRequest(
            state=SampledQuantumState1D(
                coordinates=VectorQuantity(
                    magnitude=np.arange(sample_count, dtype=np.float64),
                    unit=Unitless(),
                ),
                amplitudes=ComplexVectorQuantity(
                    magnitude=np.ones(sample_count, dtype=np.complex128),
                    unit=Unitless(),
                ),
            ),
            quadrature_weights=VectorQuantity(
                magnitude=np.ones(sample_count, dtype=np.float64),
                unit=Unitless(),
            ),
        )

    @staticmethod
    def _normalized_state(
        *,
        request: SampledQuantumState1DNormalizationRequest,
        amplitudes: np.ndarray,
    ) -> SampledQuantumState1D:
        return SampledQuantumState1D(
            coordinates=request.state.coordinates,
            amplitudes=ComplexVectorQuantity(
                magnitude=amplitudes,
                unit=Unitless(),
            ),
        )

    def test__init_rejects_nonunit_represented_norm(self) -> None:
        sample_count = 1
        nonunit_amplitude = 2.0
        request = self._request(sample_count=sample_count)

        with pytest.raises(ValueError, match="must have unit quadrature norm"):
            SampledQuantumState1DNormalization(
                request=request,
                normalized_state=self._normalized_state(
                    request=request,
                    amplitudes=np.array(
                        [nonunit_amplitude + 0.0j],
                        dtype=np.complex128,
                    ),
                ),
                normalization_factor=ScalarQuantity(
                    magnitude=1.0,
                    unit=Unitless(),
                ),
            )

    def test__init_rejects_mismatched_sample_shapes(self) -> None:
        source_sample_count = 2
        normalized_sample_count = 1
        request = self._request(sample_count=source_sample_count)
        mismatched_coordinates = VectorQuantity(
            magnitude=np.arange(normalized_sample_count, dtype=np.float64),
            unit=Unitless(),
        )

        with pytest.raises(
            ValueError,
            match="normalized_state must retain the requested coordinates",
        ):
            SampledQuantumState1DNormalization(
                request=request,
                normalized_state=SampledQuantumState1D(
                    coordinates=mismatched_coordinates,
                    amplitudes=ComplexVectorQuantity(
                        magnitude=np.ones(
                            normalized_sample_count,
                            dtype=np.complex128,
                        ),
                        unit=Unitless(),
                    ),
                ),
                normalization_factor=ScalarQuantity(
                    magnitude=1.0,
                    unit=Unitless(),
                ),
            )
