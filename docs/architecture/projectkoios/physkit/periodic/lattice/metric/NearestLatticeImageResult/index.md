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
- `image_cartesian = A image_fractional` within represented rounding.
- Result arrays own immutable storage.

## Navigation

- [Parent module](../index.md)
- [Resolver class](../NearestLatticeImageResolver/index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/metric.py::NearestLatticeImageResult`
- Tests: `tests/projectkoios/physkit/periodic/lattice/metric/test__NearestLatticeImageResolver__execute.py`

## Evidence

Resolver tests cover correlation, immutable storage, exact integer images, skew
cells, and two- and three-dimensional results. No physical cutoff or tie policy
is inferred.
