"""Verification of ``Piab1D`` construction."""

import pytest

from physkit.qm.piab1d.base import Piab1D
from physkit.units import UnitSystem


def test_accepts_positive_selected_scale_values() -> None:
    model = Piab1D(
        length=10.0,
        mass=5.485_799_090_65e-4,
        unit_system=UnitSystem.METAL,
    )

    assert model.length == 10.0
    assert model.mass == 5.485_799_090_65e-4
    assert model.unit_system is UnitSystem.METAL


def test_rejects_invalid_values_and_unit_system() -> None:
    with pytest.raises(TypeError, match="built-in float"):
        Piab1D(10, 1.0, UnitSystem.METAL)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="positive"):
        Piab1D(0.0, 1.0, UnitSystem.METAL)
    with pytest.raises(ValueError, match="positive"):
        Piab1D(1.0, -1.0, UnitSystem.METAL)
    with pytest.raises(TypeError, match="UnitSystem"):
        Piab1D(1.0, 1.0, "metal")  # type: ignore[arg-type]
