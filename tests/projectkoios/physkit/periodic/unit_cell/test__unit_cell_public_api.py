from __future__ import annotations

import projectkoios.physkit.periodic.unit_cell as unit_cell


def test_exposes_only_the_coherent_unit_cell_family() -> None:
    assert unit_cell.__all__ == [
        "Atom",
        "AtomicBasis",
        "ConventionalUnitCell",
        "PrimitiveUnitCell",
        "UnitCell",
        "UnitCellJsonCodec",
        "UnitCellSerializationError",
    ]
