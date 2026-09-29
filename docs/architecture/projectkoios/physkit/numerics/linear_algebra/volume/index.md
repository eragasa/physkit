# Module `projectkoios.physkit.numerics.linear_algebra.volume`

## Current responsibility

The module computes the absolute determinant of a column-normalized square
matrix and checks numerical column independence against a caller-supplied
normalized-volume absolute tolerance.

## Public contract

`normalized_column_volume` validates a nonempty finite real square NumPy matrix,
uses stable column pre-scaling, and returns a dimensionless absolute
determinant. `columns_are_linearly_independent` treats normalized volume at or
below `norm_vol_atol` as dependent. It does not choose domain tolerances.

## Navigation

- [Parent package](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/numerics/linear_algebra/volume.py`
- Tests: `tests/projectkoios/physkit/numerics/linear_algebra/volume/`

## Evidence

Tests cover orthogonal, near-collinear, zero-column, invalid-matrix, invalid-
tolerance, and extreme uniform-scale cases.
