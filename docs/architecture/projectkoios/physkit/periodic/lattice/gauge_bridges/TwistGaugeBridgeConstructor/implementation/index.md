# `TwistGaugeBridgeConstructor` implementation

## Current implementation

For each last-axis-fastest site index, the constructor resolves the integer
coordinate, evaluates the phase from the unreduced twist lift, assembles one
unit-magnitude complex diagonal entry, and returns a canonical unitless CSR
matrix with the correlated quotient-seam target fiber.

## Data flow

1. Validate exact domain and source-fiber types and dimensions.
2. Resolve each linear site index to an integer coordinate.
3. Evaluate the site phase from coordinate, lift, and domain extents.
4. Assemble the sparse diagonal matrix.
5. Construct the quotient-seam target fiber and correlated result.

## Navigation

- [Mathematics](mathematics/index.md)
- [References](references/index.md)
- [Testing](testing/index.md)
- [Class contract](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/gauge_bridges.py::TwistGaugeBridgeConstructor.execute`
- Test: `tests/projectkoios/physkit/periodic/lattice/gauge_bridges/test__TwistGaugeBridgeConstructor__execute.py::test__execute__matches_diagonal_phases_and_declared_seam_relation`

## Evidence boundary

The mapped test establishes implementation conformance and a bounded numerical
matrix identity. It does not establish physical-model adequacy, scientific
validation, or human acceptance.
