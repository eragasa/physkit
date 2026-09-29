# Class `projectkoios.physkit.periodic.lattice.metric.NearestLatticeImageResult`

## Current contract

The immutable result correlates a direct-lattice metric, one source fractional
displacement, the selected integer lattice translation, and the corresponding
fractional and Cartesian image vectors. `distance` is the Euclidean norm of the
Cartesian image.

## Invariants

- Every vector has the metric dimension.
- Fractional and Cartesian displacement arrays are finite.
- `image_fractional = displacement_fractional - translation_indices`.
- `image_cartesian = A image_fractional` within a componentwise binary64
  rounding bound derived from `abs(A) @ abs(image_fractional)` and the spacing
  of the expected mapped components; area or volume does not set this tolerance.
- Result arrays own immutable storage.

## Navigation

- [Parent module](../index.md)
- [Resolver class](../NearestLatticeImageResolver/index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/metric.py::NearestLatticeImageResult`
- Tests: `tests/projectkoios/physkit/periodic/lattice/metric/test__NearestLatticeImage*.py`

## Evidence

Tests cover correlation, immutable storage, exact integer images, skew cells,
and two- and three-dimensional results. Direct-constructor checks use large 2D
and tiny 3D basis scales, accepting mapped vectors while rejecting materially
inconsistent vectors. No physical cutoff or tie policy is inferred.
