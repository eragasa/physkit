# Class `projectkoios.physkit.periodic.lattice.gauge_bridges.TwistGaugeBridgeResult`

## Current contract

The immutable result correlates one finite periodic domain, centered-uniform
source fiber, quotient-seam target fiber, unitless site-diagonal sparse
transformation, and explicit transformation convention. The retained field name
`shape` preserves the donor call contract, but its value is a
`FinitePeriodicDomain`.

## Invariants

- Source and target fibers share the same twist reduction and domain dimension.
- The transformation is square with one unit-magnitude diagonal value per site.
- The transformation unit is `Unitless`.
- The convention is `TARGET_EQUALS_U_SOURCE_U_DAGGER`.

## Navigation

- [Parent module](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/gauge_bridges.py::TwistGaugeBridgeResult`
- Tests: `tests/projectkoios/physkit/periodic/lattice/gauge_bridges/test__TwistGaugeBridgeResult__init.py`

## Evidence

Implementation conformance is supported by exact fiber correlation, matrix
shape, diagonal storage, and unit-magnitude rejection tests.
