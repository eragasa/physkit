"""Verification of ``Piab1D`` construction."""

import pytest

from projectkoios.physkit.qm.piab1d.base import Piab1D
from projectkoios.physkit.units import UnitSystem


class TestPiab1DInit:
    """Own the cohesive evidence in this module."""

    def test_accepts_positive_selected_scale_values(self) -> None:
        model = Piab1D(
            length=10.0,
            mass=5.485_799_090_65e-4,
            unit_system=UnitSystem.METAL,
        )

        assert model.length == 10.0
        assert model.mass == 5.485_799_090_65e-4
        assert model.unit_system is UnitSystem.METAL

    def test_rejects_invalid_values_and_unit_system(self) -> None:
        with pytest.raises(TypeError, match="built-in float"):
            Piab1D(length=10, mass=1.0, unit_system=UnitSystem.METAL)  # type: ignore[arg-type]
        with pytest.raises(ValueError, match="positive"):
            Piab1D(length=0.0, mass=1.0, unit_system=UnitSystem.METAL)
        with pytest.raises(ValueError, match="positive"):
            Piab1D(length=1.0, mass=-1.0, unit_system=UnitSystem.METAL)
        with pytest.raises(TypeError, match="UnitSystem"):
            Piab1D(length=1.0, mass=1.0, unit_system="metal")  # type: ignore[arg-type]
