"""Verification of ``Piab1D.length_quantity``."""

from projectkoios.physkit.qm.piab1d.base import Piab1D
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    UnitSystem,
)


class TestPiab1DLengthQuantity:
    """Own the cohesive evidence in this module."""

    def test_returns_length_in_selected_unit_system(self) -> None:
        metal = Piab1D(length=10.0, mass=1.0, unit_system=UnitSystem.METAL)
        nondimensional = Piab1D(
            length=1.0, mass=1.0, unit_system=UnitSystem.NONDIMENSIONAL
        )

        assert metal.length_quantity == ScalarQuantity(
            magnitude=10.0, unit=PhysicalUnit(expression="angstrom")
        )
        assert nondimensional.length_quantity == ScalarQuantity(
            magnitude=1.0, unit=Unitless()
        )
