# Module `projectkoios.physkit.periodic.lattice.lattice3d`

## Current responsibility

The module owns three-dimensional direct and reciprocal Bravais-lattice
geometry, reciprocal conversion, and Wigner--Seitz and first-Brillouin-zone
constructions.

## Public contract

`DirectLattice3D` preserves its vector constructor and provides
`from_lattice_parameters` for a unitless canonical right-handed triclinic
direct basis. The factory accepts exact built-in floats, validates positive
lengths and a positive-definite angular metric, and uses stable half-angle and
fused arithmetic near metric boundaries. Direct-basis independence uses a
scale-invariant normalized-volume predicate with the lattice-owned absolute
tolerance `1.0e-8`.

A normalized unit-cell convention passes `a=1.0`, `b=b/a`, and `c=c/a`, while
`UnitCell.lattice_parameter` retains physical `a`.

## Navigation

- [Parent package](../index.md)
- [Numerical normalized-volume contract](../../../numerics/linear_algebra/volume/index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/lattice3d.py`
- Tests: `tests/projectkoios/physkit/periodic/lattice/lattice3d/`

## Evidence

Tests cover orthogonal, hexagonal, monoclinic, triclinic, extreme-scale,
near-boundary, invalid-metric, storage-ownership, and existing-constructor
behavior. Unit-cell integration tests recover requested physical lengths and
crystallographic angles. These checks establish represented software behavior.
