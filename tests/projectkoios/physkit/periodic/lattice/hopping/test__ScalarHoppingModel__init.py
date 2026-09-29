"""Tests for ``ScalarHoppingModel`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from projectkoios.physkit.periodic.lattice.finite_domain import (
    LatticeDimension,
    LatticeDisplacement,
)
from projectkoios.physkit.periodic.lattice.hopping import (
    ScalarHoppingModel,
    ScalarHoppingTerm,
)
from projectkoios.physkit.units import PhysicalUnit, Unitless


def test_retains_canonical_terms_and_physkit_native_units() -> None:
    negative = ScalarHoppingTerm(
        LatticeDisplacement(LatticeDimension.TWO, (-1, 0)), -1.0, 0.0
    )
    positive = ScalarHoppingTerm(
        LatticeDisplacement(LatticeDimension.TWO, (1, 0)), -1.0, 0.0
    )
    unit = PhysicalUnit("electron_volt")
    model = ScalarHoppingModel(
        "parent",
        LatticeDimension.TWO,
        (negative, positive),
        unit,
        "parent_zero",
        "scalar_cell_basis",
    )

    assert model.terms == (negative, positive)
    assert model.energy_unit is unit
    assert tuple(term.value for term in model.terms) == (-1.0 + 0.0j,) * 2
    with pytest.raises(FrozenInstanceError):
        model.identifier = "other"  # type: ignore[misc]


def test_accepts_explicit_unitless_coefficients() -> None:
    term = ScalarHoppingTerm(LatticeDisplacement(LatticeDimension.ONE, (0,)), 1.0, 0.0)
    model = ScalarHoppingModel(
        "dimensionless",
        LatticeDimension.ONE,
        (term,),
        Unitless(),
        "zero",
        "basis",
    )

    assert isinstance(model.energy_unit, Unitless)


def test_rejects_duplicate_unsorted_and_dimensionally_inconsistent_terms() -> None:
    negative = ScalarHoppingTerm(
        LatticeDisplacement(LatticeDimension.TWO, (-1, 0)), -1.0, 0.0
    )
    positive = ScalarHoppingTerm(
        LatticeDisplacement(LatticeDimension.TWO, (1, 0)), -1.0, 0.0
    )

    with pytest.raises(ValueError, match="sorted and unique"):
        ScalarHoppingModel(
            "duplicate",
            LatticeDimension.TWO,
            (negative, negative),
            Unitless(),
            "zero",
            "basis",
        )
    with pytest.raises(ValueError, match="sorted and unique"):
        ScalarHoppingModel(
            "unsorted",
            LatticeDimension.TWO,
            (positive, negative),
            Unitless(),
            "zero",
            "basis",
        )
    with pytest.raises(ValueError, match="dimensions must match"):
        ScalarHoppingModel(
            "wrong_dimension",
            LatticeDimension.ONE,
            (negative,),
            Unitless(),
            "zero",
            "basis",
        )


def test_rejects_empty_identity_terms_and_nonunit_values() -> None:
    term = ScalarHoppingTerm(LatticeDisplacement(LatticeDimension.ONE, (0,)), 1.0, 0.0)
    with pytest.raises(ValueError, match="identifier must be nonempty"):
        ScalarHoppingModel(
            "", LatticeDimension.ONE, (term,), Unitless(), "zero", "basis"
        )
    with pytest.raises(ValueError, match="terms must be nonempty"):
        ScalarHoppingModel(
            "empty", LatticeDimension.ONE, (), Unitless(), "zero", "basis"
        )
    with pytest.raises(TypeError, match="PhysicalUnit or Unitless"):
        ScalarHoppingModel(
            "bad_unit",
            LatticeDimension.ONE,
            (term,),
            "electron_volt",  # type: ignore[arg-type]
            "zero",
            "basis",
        )
