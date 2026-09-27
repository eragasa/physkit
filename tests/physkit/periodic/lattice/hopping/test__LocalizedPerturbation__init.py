"""Tests for ``LocalizedPerturbation`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from physkit.periodic.lattice.finite_domain import (
    LatticeCoordinate,
    LatticeDimension,
    LatticeDisplacement,
)
from physkit.periodic.lattice.hopping import (
    LocalizedBondTerm,
    LocalizedOnsiteTerm,
    LocalizedPerturbation,
)
from physkit.units import PhysicalUnit, Unitless


def test_retains_canonical_mixed_terms_and_physkit_native_units() -> None:
    onsite = LocalizedOnsiteTerm(
        LatticeCoordinate(LatticeDimension.TWO, (0, 0)), 0.2, 0.0
    )
    bond = LocalizedBondTerm(
        LatticeCoordinate(LatticeDimension.TWO, (0, 0)),
        LatticeDisplacement(LatticeDimension.TWO, (1, 1)),
        0.05,
        0.0,
    )
    unit = PhysicalUnit("electron_volt")
    perturbation = LocalizedPerturbation(
        "defect",
        LatticeDimension.TWO,
        (onsite, bond),
        unit,
        "parent_zero",
        "scalar_cell_basis",
    )

    assert perturbation.terms == (onsite, bond)
    assert perturbation.energy_unit is unit
    assert tuple(term.value for term in perturbation.terms) == (
        0.2 + 0.0j,
        0.05 + 0.0j,
    )
    with pytest.raises(FrozenInstanceError):
        perturbation.identifier = "other"  # type: ignore[misc]


def test_accepts_explicit_unitless_coefficients() -> None:
    onsite = LocalizedOnsiteTerm(
        LatticeCoordinate(LatticeDimension.ONE, (0,)), 0.2, 0.0
    )
    perturbation = LocalizedPerturbation(
        "dimensionless", LatticeDimension.ONE, (onsite,), Unitless(),
        "zero", "basis"
    )

    assert isinstance(perturbation.energy_unit, Unitless)


def test_rejects_noncanonical_duplicate_and_dimensionally_inconsistent_terms() -> None:
    onsite = LocalizedOnsiteTerm(
        LatticeCoordinate(LatticeDimension.TWO, (0, 0)), 0.2, 0.0
    )
    bond = LocalizedBondTerm(
        LatticeCoordinate(LatticeDimension.TWO, (0, 0)),
        LatticeDisplacement(LatticeDimension.TWO, (1, 0)),
        0.05,
        0.0,
    )
    with pytest.raises(ValueError, match="canonically sorted and unique"):
        LocalizedPerturbation(
            "wrong_order", LatticeDimension.TWO, (bond, onsite), Unitless(),
            "zero", "basis"
        )
    with pytest.raises(ValueError, match="canonically sorted and unique"):
        LocalizedPerturbation(
            "duplicate", LatticeDimension.TWO, (onsite, onsite), Unitless(),
            "zero", "basis"
        )
    with pytest.raises(ValueError, match="dimension must match"):
        LocalizedPerturbation(
            "wrong_dimension", LatticeDimension.ONE, (onsite,), Unitless(),
            "zero", "basis"
        )


def test_rejects_empty_terms_and_nonunit_values() -> None:
    with pytest.raises(ValueError, match="terms must be nonempty"):
        LocalizedPerturbation(
            "empty", LatticeDimension.ONE, (), Unitless(), "zero", "basis"
        )
    onsite = LocalizedOnsiteTerm(
        LatticeCoordinate(LatticeDimension.ONE, (0,)), 0.2, 0.0
    )
    with pytest.raises(TypeError, match="PhysicalUnit or Unitless"):
        LocalizedPerturbation(
            "bad_unit", LatticeDimension.ONE, (onsite,), "electron_volt",  # type: ignore[arg-type]
            "zero", "basis"
        )
