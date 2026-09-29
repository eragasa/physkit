"""Verification of ``Piab1D.hbar_quantity``."""

import numpy as np

from projectkoios.physkit.qm.piab1d.base import Piab1D
from projectkoios.physkit.units import PhysicalUnit, UnitSystem


class TestPiab1DHbarQuantity:
    """Own the cohesive evidence in this module."""

    def test_returns_hbar_in_selected_action_unit(self) -> None:
        model = Piab1D(length=10.0, mass=1.0, unit_system=UnitSystem.METAL)

        assert model.hbar_quantity.unit == PhysicalUnit(
            expression="electron_volt * picosecond"
        )
        np.testing.assert_allclose(
            model.hbar_quantity.magnitude,
            6.582_119_565_476_075e-4,
            rtol=5.0e-10,
            atol=0.0,
        )
