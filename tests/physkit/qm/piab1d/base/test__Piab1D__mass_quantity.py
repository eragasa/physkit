"""Verification of ``Piab1D.mass_quantity``."""

from physkit.qm.piab1d.base import Piab1D
from physkit.units import PhysicalUnit, ScalarQuantity, UnitSystem


def test_returns_particle_mass_in_selected_unit_system() -> None:
    model = Piab1D(
        10.0,
        5.485_799_090_65e-4,
        UnitSystem.METAL,
    )

    assert model.mass_quantity == ScalarQuantity(
        5.485_799_090_65e-4,
        PhysicalUnit("dalton"),
    )
