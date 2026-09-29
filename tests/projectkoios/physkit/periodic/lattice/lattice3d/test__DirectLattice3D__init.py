from __future__ import annotations

import numpy as np
import pytest

from projectkoios.physkit.periodic.lattice.lattice3d import DirectLattice3D


def test__DirectLattice3D__init__preserves_vector_constructor_and_copies() -> None:
    a1 = np.array([1.0, 0.0, 0.0])
    a2 = np.array([0.5, 2.0, 0.0])
    a3 = np.array([0.25, 0.75, 3.0])
    expected = np.column_stack((a1, a2, a3))

    lattice = DirectLattice3D(a1, a2, a3)
    a1[:] = -1.0
    a2[:] = -2.0
    a3[:] = -3.0

    np.testing.assert_array_equal(lattice.A, expected)
    assert lattice.A.flags.writeable is False
    assert not np.shares_memory(lattice.A, a1)
    assert not np.shares_memory(lattice.A, a2)
    assert not np.shares_memory(lattice.A, a3)


@pytest.mark.parametrize("scale", [1.0e-200, 1.0, 1.0e200])
def test__DirectLattice3D__init__accepts_scaled_orthogonal_bases(
    scale: float,
) -> None:
    lattice = DirectLattice3D(
        scale * np.array([1.0, 0.0, 0.0]),
        scale * np.array([0.0, 1.0, 0.0]),
        scale * np.array([0.0, 0.0, 1.0]),
    )

    np.testing.assert_array_equal(lattice.A / scale, np.eye(3))


@pytest.mark.parametrize("scale", [1.0e-200, 1.0, 1.0e200])
def test__DirectLattice3D__init__accepts_scaled_resolved_near_collinearity(
    scale: float,
) -> None:
    lattice = DirectLattice3D(
        scale * np.array([1.0, 0.0, 0.0]),
        scale * np.array([1.0, 2.0e-8, 0.0]),
        scale * np.array([0.0, 0.0, 1.0]),
    )

    assert isinstance(lattice, DirectLattice3D)


@pytest.mark.parametrize("scale", [1.0e-200, 1.0, 1.0e200])
def test__DirectLattice3D__init__rejects_scaled_unresolved_near_collinearity(
    scale: float,
) -> None:
    with pytest.raises(ValueError, match="must be linearly independent"):
        DirectLattice3D(
            scale * np.array([1.0, 0.0, 0.0]),
            scale * np.array([1.0, 5.0e-9, 0.0]),
            scale * np.array([0.0, 0.0, 1.0]),
        )


@pytest.mark.parametrize("scale", [1.0e-200, 1.0, 1.0e200])
def test__DirectLattice3D__init__rejects_scaled_exact_dependence(
    scale: float,
) -> None:
    with pytest.raises(ValueError, match="must be linearly independent"):
        DirectLattice3D(
            scale * np.array([1.0, 0.0, 0.0]),
            scale * np.array([2.0, 0.0, 0.0]),
            scale * np.array([0.0, 0.0, 1.0]),
        )
