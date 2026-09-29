# Class `projectkoios.physkit.periodic.lattice.gauge_bridges.TwistGaugeBridgeConstructor`

## Current contract

`execute(shape, source_fiber)` accepts a one-, two-, or three-dimensional finite
periodic domain and a centered uniform-link twist fiber. It returns the
site-diagonal unitary, the unchanged source fiber, and the corresponding
quotient-seam target fiber.

## Invariants

- Domain and fiber dimensions agree.
- The unreduced twist lift determines the site phases.
- Site enumeration uses the finite domain's last-axis-fastest ordering.
- The returned matrix is canonical unitless CSR data.

## Navigation

- [Implementation](implementation/index.md)
- [Parent module](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/gauge_bridges.py::TwistGaugeBridgeConstructor`
- Test: `tests/projectkoios/physkit/periodic/lattice/gauge_bridges/test__TwistGaugeBridgeConstructor__execute.py::test__execute__matches_diagonal_phases_and_declared_seam_relation`

## Evidence

Implementation conformance and bounded numerical verification are supported by
hand-derived three-site phases and the transformed seam matrix at absolute
tolerance `1e-15`. Scientific validation and human acceptance are not evaluated.
