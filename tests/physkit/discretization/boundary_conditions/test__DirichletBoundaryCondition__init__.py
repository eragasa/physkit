"""Verification of ``DirichletBoundaryCondition`` construction."""

import pytest

from physkit.core.boundaries import BoundaryCondition, BoundaryConditionType
from physkit.discretization.boundary_conditions import DirichletBoundaryCondition
from physkit.units import ScalarQuantity, Unitless


def test_uses_nominal_boundary_ownership() -> None:
    boundary = DirichletBoundaryCondition(ScalarQuantity(0.0, Unitless()))

    assert isinstance(boundary, BoundaryCondition)
    assert boundary.type is BoundaryConditionType.DIRICHLET
    assert boundary.condition_kind == "dirichlet"


def test_requires_scalar_quantity() -> None:
    with pytest.raises(TypeError):
        DirichletBoundaryCondition(0.0)  # type: ignore[arg-type]
