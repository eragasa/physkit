"""Verification of ``Piab1D.mass_quantity``."""

from projectkoios.physkit.qm.piab1d.base import Piab1D
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, UnitSystem


class TestPiab1DMassQuantity:
    """Own the cohesive evidence in this module."""

    def test_returns_particle_mass_in_selected_unit_system(self) -> None:
        model = Piab1D(
            length=10.0, mass=5.485_799_090_65e-4, unit_system=UnitSystem.METAL
        )

        assert model.mass_quantity == ScalarQuantity(
            magnitude=5.485_799_090_65e-4, unit=PhysicalUnit(expression="dalton")
        )
