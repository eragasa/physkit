from __future__ import annotations

import numpy as np
import pytest

from projectkoios.physkit.periodic.lattice.lattice1d import DirectLattice1D


def test_stores_immutable_primitive_basis() -> None:
    lattice = DirectLattice1D(2.5)

    assert lattice.dimension == 1
    assert lattice.a1 == 2.5
    np.testing.assert_array_equal(lattice.primitive_basis, [[2.5]])
    assert lattice.primitive_basis.flags.writeable is False


@pytest.mark.parametrize("value", [0.0, -1.0, np.inf, np.nan])
def test_rejects_nonpositive_or_nonfinite_lattice_constant(value: float) -> None:
    with pytest.raises(ValueError):
        DirectLattice1D(value)
