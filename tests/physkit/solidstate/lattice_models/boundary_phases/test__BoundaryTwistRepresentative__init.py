"""Tests for ``BoundaryTwistRepresentative`` construction."""

import pytest

from physkit.solidstate.lattice_models.boundary_phases import (
    BoundaryTwistRepresentative,
)
from physkit.solidstate.lattice_models.geometry import LatticeDimension


def test_accepts_half_open_unit_interval_components() -> None:
    representative = BoundaryTwistRepresentative(
        LatticeDimension.THREE,
        (0.0, 0.5, 0.9999999999999999),
    )

    assert representative.turns == (0.0, 0.5, 0.9999999999999999)


def test_rejects_noncanonical_components() -> None:
    with pytest.raises(ValueError, match=r"must lie in \[0, 1\)"):
        BoundaryTwistRepresentative(LatticeDimension.ONE, (-0.1,))
    with pytest.raises(ValueError, match=r"must lie in \[0, 1\)"):
        BoundaryTwistRepresentative(LatticeDimension.ONE, (1.0,))
    with pytest.raises(ValueError, match="must be finite"):
        BoundaryTwistRepresentative(LatticeDimension.ONE, (float("inf"),))
