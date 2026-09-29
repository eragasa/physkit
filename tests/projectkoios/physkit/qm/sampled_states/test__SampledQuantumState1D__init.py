"""Construction tests for ``SampledQuantumState1D``."""

from inspect import signature

import numpy as np
import pytest

from projectkoios.physkit.qm.sampled_states import SampledQuantumState1D
from projectkoios.physkit.units import ComplexVectorQuantity, Unitless, VectorQuantity


class TestSampledQuantumState1DInit:
    """Verify correlation of one-dimensional coordinates and amplitudes."""

    def test__init_exposes_only_coordinates_and_amplitudes(self) -> None:
        assert tuple(signature(SampledQuantumState1D).parameters) == (
            "coordinates",
            "amplitudes",
        )

    def test__init_retains_matching_coordinates_and_amplitudes(self) -> None:
        sample_count = 2
        coordinates = VectorQuantity(
            magnitude=np.arange(sample_count, dtype=np.float64),
            unit=Unitless(),
        )
        amplitudes = ComplexVectorQuantity(
            magnitude=np.ones(sample_count, dtype=np.complex128),
            unit=Unitless(),
        )

        state = SampledQuantumState1D(
            coordinates=coordinates,
            amplitudes=amplitudes,
        )

        assert state.coordinates is coordinates
        assert state.amplitudes is amplitudes

    def test__init_rejects_empty_coordinates(self) -> None:
        with pytest.raises(ValueError, match="coordinates must be nonempty"):
            SampledQuantumState1D(
                coordinates=VectorQuantity(
                    magnitude=np.array([], dtype=np.float64),
                    unit=Unitless(),
                ),
                amplitudes=ComplexVectorQuantity(
                    magnitude=np.array([], dtype=np.complex128),
                    unit=Unitless(),
                ),
            )

    def test__init_rejects_mismatched_amplitude_count(self) -> None:
        coordinate_count = 2
        amplitude_count = 1

        with pytest.raises(ValueError, match="amplitudes must match coordinates"):
            SampledQuantumState1D(
                coordinates=VectorQuantity(
                    magnitude=np.arange(coordinate_count, dtype=np.float64),
                    unit=Unitless(),
                ),
                amplitudes=ComplexVectorQuantity(
                    magnitude=np.ones(amplitude_count, dtype=np.complex128),
                    unit=Unitless(),
                ),
            )
