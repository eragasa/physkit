from __future__ import annotations

import numpy as np
import pytest

from physkit.periodic.lattice.lattice3d import DirectLattice3D
from physkit.periodic.unit_cell.base import Atom, AtomicBasis
from physkit.units.quantities import Unitless, VectorQuantity


@pytest.fixture
def fcc_direct_lattice() -> DirectLattice3D:
    return DirectLattice3D(
        a1=np.array([0.5, 0.5, 0.0]),
        a2=np.array([0.5, 0.0, 0.5]),
        a3=np.array([0.0, 0.5, 0.5]),
    )


@pytest.fixture
def silicon_basis() -> AtomicBasis:
    return AtomicBasis(
        atoms=(
            Atom(
                symbol="Si",
                position_fractional=VectorQuantity(np.zeros(3), Unitless()),
            ),
            Atom(
                symbol="Si",
                position_fractional=VectorQuantity(
                    np.array([0.25, 0.25, 0.25]),
                    Unitless(),
                ),
            ),
        )
    )
