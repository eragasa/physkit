"""Verification of immutable complex matrix quantities."""

import numpy as np

from physkit.units.quantities import ComplexMatrixQuantity, PhysicalUnit


def test_preserves_finite_complex_values() -> None:
    quantity = ComplexMatrixQuantity(
        np.array([[1.0 + 2.0j, 0.0], [0.0, -3.0j]]),
        PhysicalUnit("joule"),
    )

    np.testing.assert_array_equal(
        quantity.magnitude,
        [[1.0 + 2.0j, 0.0], [0.0, -3.0j]],
    )
    assert not quantity.magnitude.flags.writeable
