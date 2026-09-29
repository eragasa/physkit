from __future__ import annotations

import numpy as np
import pytest

from physkit.periodic.lattice.lattice3d import DirectLattice3D


def test_vector_constructor_remains_compatible_and_copies_inputs() -> None:
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
def test_accepts_orthogonal_bases_independently_of_uniform_scale(
    scale: float,
) -> None:
    lattice = DirectLattice3D(
        scale * np.array([1.0, 0.0, 0.0]),
        scale * np.array([0.0, 1.0, 0.0]),
        scale * np.array([0.0, 0.0, 1.0]),
    )

    np.testing.assert_array_equal(lattice.A / scale, np.eye(3))


@pytest.mark.parametrize("scale", [1.0e-200, 1.0, 1.0e200])
def test_accepts_resolved_near_collinearity_independently_of_uniform_scale(
    scale: float,
) -> None:
    lattice = DirectLattice3D(
        scale * np.array([1.0, 0.0, 0.0]),
        scale * np.array([1.0, 2.0e-8, 0.0]),
        scale * np.array([0.0, 0.0, 1.0]),
    )

    assert isinstance(lattice, DirectLattice3D)


@pytest.mark.parametrize("scale", [1.0e-200, 1.0, 1.0e200])
def test_rejects_unresolved_near_collinearity_independently_of_uniform_scale(
    scale: float,
) -> None:
    with pytest.raises(ValueError, match="must be linearly independent"):
        DirectLattice3D(
            scale * np.array([1.0, 0.0, 0.0]),
            scale * np.array([1.0, 5.0e-9, 0.0]),
            scale * np.array([0.0, 0.0, 1.0]),
        )


@pytest.mark.parametrize("scale", [1.0e-200, 1.0, 1.0e200])
def test_rejects_exact_dependence_independently_of_uniform_scale(
    scale: float,
) -> None:
    with pytest.raises(ValueError, match="must be linearly independent"):
        DirectLattice3D(
            scale * np.array([1.0, 0.0, 0.0]),
            scale * np.array([2.0, 0.0, 0.0]),
            scale * np.array([0.0, 0.0, 1.0]),
        )
