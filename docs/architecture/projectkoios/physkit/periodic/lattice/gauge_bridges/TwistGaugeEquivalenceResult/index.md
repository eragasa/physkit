# Class `projectkoios.physkit.periodic.lattice.gauge_bridges.TwistGaugeEquivalenceResult`

## Current contract

The immutable result retains the exact source, target, bridge, caller-owned
absolute tolerance, compatibility issues, and maximum absolute residual when
arithmetic was admissible. `compatible` reports metadata compatibility;
`is_equivalent` additionally requires an available residual not greater than the
inclusive tolerance.

## Invariants

- The tolerance is a finite nonnegative built-in float.
- Compatibility issues are sorted and unique.
- A residual exists exactly when no compatibility issue blocks arithmetic.
- An available residual is finite and nonnegative.

## Navigation

- [Parent module](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/gauge_bridges.py::TwistGaugeEquivalenceResult`
- Test: `tests/projectkoios/physkit/periodic/lattice/gauge_bridges/test__TwistGaugeEquivalenceResult__init.py::test__init__requires_residual_presence_to_agree_with_compatibility`

## Evidence

Implementation conformance is supported by exact zero-residual state and
contradictory-state rejection tests.
