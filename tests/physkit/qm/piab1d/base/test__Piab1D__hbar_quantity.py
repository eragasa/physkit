"""Verification of ``Piab1D.hbar_quantity``."""

import numpy as np

from physkit.qm.piab1d.base import Piab1D
from physkit.units import PhysicalUnit, UnitSystem


def test_returns_hbar_in_selected_action_unit() -> None:
    model = Piab1D(10.0, 1.0, UnitSystem.METAL)

    assert model.hbar_quantity.unit == PhysicalUnit(
        "electron_volt * picosecond"
    )
    np.testing.assert_allclose(
        model.hbar_quantity.magnitude,
        6.582_119_565_476_075e-4,
        rtol=5.0e-10,
        atol=0.0,
    )
