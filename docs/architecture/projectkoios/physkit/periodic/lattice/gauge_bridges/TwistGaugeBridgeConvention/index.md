# Class `projectkoios.physkit.periodic.lattice.gauge_bridges.TwistGaugeBridgeConvention`

## Current contract

The enumeration identifies the supported transformation direction. Its sole
current value, `TARGET_EQUALS_U_SOURCE_U_DAGGER`, means
`H_target = U H_source U^dagger`.

## Invariants

- The represented value is `target_equals_u_source_u_dagger`.
- The convention does not imply that arbitrary source and target operators are
  compatible or equivalent.

## Navigation

- [Parent module](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/gauge_bridges.py::TwistGaugeBridgeConvention`
- Test: `tests/projectkoios/physkit/periodic/lattice/gauge_bridges/test__TwistGaugeBridgeConstructor__execute.py::test__execute__matches_diagonal_phases_and_declared_seam_relation`

## Evidence

Implementation conformance is supported by exact enumeration-identity and
matrix-relation assertions in the mapped test.
