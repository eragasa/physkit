from __future__ import annotations

import numpy as np

from projectkoios.physkit.periodic.lattice.lattice1d import DirectLattice1D


def test_multiplies_integer_modes_by_lattice_constant() -> None:
    lattice = DirectLattice1D(2.5)

    vectors = lattice.vector(np.array([-2, 0, 3]))

    np.testing.assert_array_equal(vectors, [-5.0, 0.0, 7.5])
