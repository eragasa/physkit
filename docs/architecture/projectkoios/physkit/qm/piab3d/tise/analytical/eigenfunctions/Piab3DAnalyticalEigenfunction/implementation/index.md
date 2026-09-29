# Implementation

## Algorithm

1. Validate the PIAB3D model, positive built-in integer quantum numbers, plane
   normal, in-plane coordinate vectors, and fixed coordinate.
2. Convert all coordinates to the model length unit.
3. Map the plane normal to deterministic in-plane axes, lengths, and quantum
   numbers.
4. Reject coordinates outside the corresponding closed box intervals.
5. Evaluate the two in-plane sine factors, the fixed-axis sine factor, and the
   three-dimensional normalization prefactor.
6. Return an immutable correlated plane-slice result.

## Detailed views

- [Mathematics](mathematics/index.md)
- [References](references/index.md)
- [Testing](testing/index.md)

## Navigation

- [Class](../index.md)
