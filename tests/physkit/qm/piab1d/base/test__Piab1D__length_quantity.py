"""Verification of ``Piab1D.length_quantity``."""

from physkit.qm.piab1d.base import Piab1D
from physkit.units import PhysicalUnit, ScalarQuantity, UnitSystem, Unitless


def test_returns_length_in_selected_unit_system() -> None:
    metal = Piab1D(10.0, 1.0, UnitSystem.METAL)
    nondimensional = Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)

    assert metal.length_quantity == ScalarQuantity(
        10.0,
        PhysicalUnit("angstrom"),
    )
    assert nondimensional.length_quantity == ScalarQuantity(
        1.0,
        Unitless(),
    )
