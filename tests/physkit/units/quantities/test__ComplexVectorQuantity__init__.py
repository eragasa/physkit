"""Verification of immutable complex vector quantities."""

import numpy as np
import pytest

from physkit.units.quantities import ComplexVectorQuantity, Unitless


def test_owns_finite_immutable_complex128_values() -> None:
    source = np.array([1.0 + 2.0j, -3.0j], dtype=np.complex64)
    quantity = ComplexVectorQuantity(source, Unitless())
    source[:] = 0.0

    np.testing.assert_array_equal(quantity.magnitude, [1.0 + 2.0j, -3.0j])
    assert quantity.magnitude.dtype == np.dtype("<c16")
    assert not quantity.magnitude.flags.writeable


def test_rejects_nonvector_and_nonfinite_values() -> None:
    with pytest.raises(ValueError, match="vector"):
        ComplexVectorQuantity(np.ones((1, 1)), Unitless())
    with pytest.raises(ValueError, match="finite"):
        ComplexVectorQuantity(np.array([complex(np.nan, 0.0)]), Unitless())
