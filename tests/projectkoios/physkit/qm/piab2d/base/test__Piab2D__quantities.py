"""Tests for unit-bearing two-dimensional box parameters."""

from projectkoios.physkit.qm.piab2d.base import Piab2D
from projectkoios.physkit.units import PhysicalUnit, Unitless, UnitSystem


class TestPiab2DQuantities:
    """Verify selected-scale length, mass, and action quantities."""

    def test__quantities__represent_nondimensional_model(self) -> None:
        length_x = 2.0
        length_y = 3.0
        particle_mass = 4.0
        model = Piab2D(
            length_x=length_x,
            length_y=length_y,
            mass=particle_mass,
            unit_system=UnitSystem.NONDIMENSIONAL,
        )

        assert model.length_x_quantity.magnitude == length_x
        assert model.length_y_quantity.magnitude == length_y
        assert model.mass_quantity.magnitude == particle_mass
        assert model.hbar_quantity.magnitude == 1.0
        assert isinstance(model.length_x_quantity.unit, Unitless)
        assert isinstance(model.length_y_quantity.unit, Unitless)
        assert isinstance(model.mass_quantity.unit, Unitless)
        assert isinstance(model.hbar_quantity.unit, Unitless)

    def test__quantities__represent_metal_scale_without_si_rescaling(self) -> None:
        length_x_angstrom = 10.0
        length_y_angstrom = 20.0
        particle_mass_dalton = 5.0
        model = Piab2D(
            length_x=length_x_angstrom,
            length_y=length_y_angstrom,
            mass=particle_mass_dalton,
            unit_system=UnitSystem.METAL,
        )

        assert model.length_x_quantity.unit == PhysicalUnit(expression="angstrom")
        assert model.length_y_quantity.unit == PhysicalUnit(expression="angstrom")
        assert model.mass_quantity.unit == PhysicalUnit(expression="dalton")
        assert model.hbar_quantity.unit == PhysicalUnit(
            expression="electron_volt * picosecond"
        )
