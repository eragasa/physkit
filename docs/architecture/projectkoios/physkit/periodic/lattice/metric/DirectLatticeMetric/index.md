# Class `projectkoios.physkit.periodic.lattice.metric.DirectLatticeMetric`

## Current contract

The immutable record derives constant metric geometry from an owned copy of a
`DirectLattice2D` or `DirectLattice3D`. It exposes the direct basis `A`,
reciprocal basis `B=2πA^{-T}`, covariant metric `g=A^T A`, inverse metric,
reciprocal metric, fundamental-region measure, and fractional-to-Cartesian
mapping.

## Invariants

- The dimension is exactly two or three and comes from a nominal direct-lattice
  owner.
- Stored arrays are independent, immutable binary64 arrays.
- Every derived array is finite; the metric must be invertible in binary64.
- `A^T B=2πI`, `B^T B=(2π)^2g^{-1}`, and mathematically
  `sqrt(det(g))=|det(A)|` up to represented floating-point rounding.
- Fundamental-region measure is evaluated from the owned direct basis rather
  than its squared Gram determinant, avoiding avoidable range loss for finite
  large or small measures.

## Navigation

- [Parent module](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/metric.py::DirectLatticeMetric`
- Tests: `tests/projectkoios/physkit/periodic/lattice/metric/test__DirectLatticeMetric__*.py`

## Evidence

Tests exercise both supported dimensions, duality and metric identities,
finite measures whose Gram determinants overflow or underflow, immutable
storage, batch coordinate mapping, and invalid inputs. This does not establish
physical units, material geometry, or scientific validation.
