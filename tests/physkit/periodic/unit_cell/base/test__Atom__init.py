from __future__ import annotations

import dataclasses

import numpy as np
import pytest

from physkit.periodic.unit_cell.base import Atom
from physkit.units.quantities import (
    PhysicalUnit,
    Unitless,
    VectorQuantity,
)


def test_constructs_element_at_fractional_position() -> None:
    position = VectorQuantity(np.array([0.0, 0.25, 0.5]), Unitless())

    atom = Atom(symbol="Si", position_fractional=position)

    assert atom.symbol == "Si"
    assert atom.position_fractional is position


def test_is_immutable() -> None:
    atom = Atom(
        symbol="Si",
        position_fractional=VectorQuantity(np.zeros(3), Unitless()),
    )

    with pytest.raises(dataclasses.FrozenInstanceError):
        atom.symbol = "Ge"  # type: ignore[misc]


def test_rejects_length_unit_for_fractional_position() -> None:
    with pytest.raises(ValueError, match="explicitly unitless"):
        Atom(
            symbol="Si",
            position_fractional=VectorQuantity(
                np.zeros(3),
                PhysicalUnit("angstrom"),
            ),
        )
