from __future__ import annotations

import numpy as np

from projectkoios.physkit.periodic.lattice.lattice1d import (
    DirectLattice1D,
    ReciprocalLattice1D,
)


def test_constructs_dual_reciprocal_basis() -> None:
    direct = DirectLattice1D(2.5)

    reciprocal = ReciprocalLattice1D.from_direct_lattice(direct)

    np.testing.assert_allclose(
        direct.primitive_basis.T @ reciprocal.primitive_basis,
        2.0 * np.pi * np.eye(1),
    )
    assert reciprocal.primitive_basis.flags.writeable is False
