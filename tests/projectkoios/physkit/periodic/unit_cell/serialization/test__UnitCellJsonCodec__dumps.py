from __future__ import annotations

import json

from projectkoios.physkit.periodic.lattice.lattice3d import DirectLattice3D
from projectkoios.physkit.periodic.unit_cell.base import AtomicBasis, PrimitiveUnitCell
from projectkoios.physkit.periodic.unit_cell.serialization import UnitCellJsonCodec
from projectkoios.physkit.units.quantities import PhysicalUnit, ScalarQuantity


def test_emits_deterministic_version_one_payload(
    fcc_direct_lattice: DirectLattice3D,
    silicon_basis: AtomicBasis,
) -> None:
    cell = PrimitiveUnitCell(
        direct_lattice=fcc_direct_lattice,
        lattice_parameter=ScalarQuantity(5.43, PhysicalUnit("angstrom")),
        atomic_basis=silicon_basis,
    )

    first = UnitCellJsonCodec().dumps(
        cell,
        structure_id="Si.PrimitiveUnitCell",
    )
    second = UnitCellJsonCodec().dumps(
        cell,
        structure_id="Si.PrimitiveUnitCell",
    )
    payload = json.loads(first)

    assert first == second
    assert first.endswith("\n")
    assert payload["schema_version"] == 1
    assert payload["structure_id"] == "Si.PrimitiveUnitCell"
    assert payload["representation"] == "primitive"
    assert payload["lattice"]["A"]["vector_axis"] == "columns"
