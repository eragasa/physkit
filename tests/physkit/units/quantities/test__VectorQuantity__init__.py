"""Verification of immutable ``VectorQuantity`` storage."""

import numpy as np

from physkit.units.quantities import Unitless, VectorQuantity


def test_owns_immutable_binary64_values() -> None:
    source = np.array([1.0, 2.0], dtype=np.float32)
    quantity = VectorQuantity(source, Unitless())
    source[:] = 0.0

    np.testing.assert_array_equal(quantity.magnitude, [1.0, 2.0])
    assert quantity.magnitude.dtype == np.dtype("<f8")
    assert not quantity.magnitude.flags.writeable
