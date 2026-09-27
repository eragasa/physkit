from __future__ import annotations

import json

import numpy as np
import pytest

from physkit.periodic.lattice.lattice3d import DirectLattice3D
from physkit.periodic.unit_cell.base import (
    AtomicBasis,
    ConventionalUnitCell,
    PrimitiveUnitCell,
)
from physkit.periodic.unit_cell.errors import UnitCellSerializationError
from physkit.periodic.unit_cell.serialization import UnitCellJsonCodec
from physkit.units.quantities import PhysicalUnit, ScalarQuantity


def test_round_trip_preserves_primitive_nominal_type(
    fcc_direct_lattice: DirectLattice3D,
    silicon_basis: AtomicBasis,
) -> None:
    cell = PrimitiveUnitCell(
        direct_lattice=fcc_direct_lattice,
        lattice_parameter=ScalarQuantity(5.43, PhysicalUnit("angstrom")),
        atomic_basis=silicon_basis,
    )
    serialized = UnitCellJsonCodec().dumps(
        cell,
        structure_id="Si.PrimitiveUnitCell",
    )

    restored = UnitCellJsonCodec().loads(
        serialized,
        expected_structure_id="Si.PrimitiveUnitCell",
    )

    assert isinstance(restored, PrimitiveUnitCell)
    np.testing.assert_array_equal(restored.A.magnitude, cell.A.magnitude)
    np.testing.assert_array_equal(restored.H.magnitude, cell.H.magnitude)


def test_round_trip_preserves_conventional_nominal_type(
    fcc_direct_lattice: DirectLattice3D,
    silicon_basis: AtomicBasis,
) -> None:
    cell = ConventionalUnitCell(
        direct_lattice=fcc_direct_lattice,
        lattice_parameter=ScalarQuantity(5.43, PhysicalUnit("angstrom")),
        atomic_basis=silicon_basis,
    )

    restored = UnitCellJsonCodec().loads(
        UnitCellJsonCodec().dumps(
            cell,
            structure_id="Si.ConventionalUnitCell",
        ),
        expected_structure_id="Si.ConventionalUnitCell",
    )

    assert isinstance(restored, ConventionalUnitCell)


def test_rejects_structure_identity_mismatch(
    fcc_direct_lattice: DirectLattice3D,
    silicon_basis: AtomicBasis,
) -> None:
    content = UnitCellJsonCodec().dumps(
        PrimitiveUnitCell(
            direct_lattice=fcc_direct_lattice,
            lattice_parameter=ScalarQuantity(5.43, PhysicalUnit("angstrom")),
            atomic_basis=silicon_basis,
        ),
        structure_id="Si.PrimitiveUnitCell",
    )

    with pytest.raises(UnitCellSerializationError, match="identity does not match"):
        UnitCellJsonCodec().loads(
            content,
            expected_structure_id="different",
        )


def test_rejects_non_column_vector_convention(
    fcc_direct_lattice: DirectLattice3D,
    silicon_basis: AtomicBasis,
) -> None:
    content = UnitCellJsonCodec().dumps(
        PrimitiveUnitCell(
            direct_lattice=fcc_direct_lattice,
            lattice_parameter=ScalarQuantity(5.43, PhysicalUnit("angstrom")),
            atomic_basis=silicon_basis,
        ),
        structure_id="Si.PrimitiveUnitCell",
    )
    payload = json.loads(content)
    payload["lattice"]["A"]["vector_axis"] = "rows"

    with pytest.raises(UnitCellSerializationError, match="vectors as columns"):
        UnitCellJsonCodec().loads(
            json.dumps(payload),
            expected_structure_id="Si.PrimitiveUnitCell",
        )


def test_preserves_json_decode_error_as_cause() -> None:
    with pytest.raises(UnitCellSerializationError) as captured:
        UnitCellJsonCodec().loads(
            "{not-json",
            expected_structure_id="Si.PrimitiveUnitCell",
        )

    assert isinstance(captured.value.__cause__, json.JSONDecodeError)
    assert captured.value.__traceback__ is not None


def test_preserves_invalid_unit_error_as_cause(
    fcc_direct_lattice: DirectLattice3D,
    silicon_basis: AtomicBasis,
) -> None:
    content = UnitCellJsonCodec().dumps(
        PrimitiveUnitCell(
            direct_lattice=fcc_direct_lattice,
            lattice_parameter=ScalarQuantity(5.43, PhysicalUnit("angstrom")),
            atomic_basis=silicon_basis,
        ),
        structure_id="Si.PrimitiveUnitCell",
    )
    payload = json.loads(content)
    payload["lattice"]["lattice_parameter"]["unit"] = "not-a-unit"

    with pytest.raises(UnitCellSerializationError) as captured:
        UnitCellJsonCodec().loads(
            json.dumps(payload),
            expected_structure_id="Si.PrimitiveUnitCell",
        )

    assert isinstance(captured.value.__cause__, TypeError | ValueError)
