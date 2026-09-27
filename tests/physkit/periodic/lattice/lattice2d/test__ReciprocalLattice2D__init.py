from __future__ import annotations

import numpy as np
import pytest

from physkit.periodic.lattice.lattice2d import ReciprocalLattice2D


def test_rejects_invalid_second_primitive_vector() -> None:
    with pytest.raises(ValueError, match="shape"):
        ReciprocalLattice2D(
            b1=np.array([1.0, 0.0]),
            b2=np.array([0.0, 1.0, 0.0]),
        )
