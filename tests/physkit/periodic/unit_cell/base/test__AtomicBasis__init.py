from __future__ import annotations

import pytest

from physkit.periodic.unit_cell.base import Atom, AtomicBasis


def test_preserves_declared_atom_order(silicon_basis: AtomicBasis) -> None:
    first, second = silicon_basis.atoms

    assert silicon_basis.atoms == (first, second)
    assert isinstance(first, Atom)


def test_rejects_empty_basis() -> None:
    with pytest.raises(ValueError, match="at least one atom"):
        AtomicBasis(atoms=())
