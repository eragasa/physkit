# Module `projectkoios.physkit.numerics.linear_algebra.kronecker`

## Current responsibility

The module owns unit-free sparse Kronecker-sum assembly for separable two- and
three-axis numerical representations.

## Public contract

`SparseKroneckerSumConstructor.execute` accepts an ordered tuple of two or three
finite numeric, nonempty, square SciPy sparse matrices or arrays. It returns an
owned canonical CSR array. Axis order follows C-order array flattening, so the
last axis varies fastest.

The constructor supplies numerical assembly only. It does not choose grids,
boundary conditions, physical units, Hamiltonian coefficients, eigensolver
policy, convergence tolerances, or scientific interpretation.

## Navigation

- [Class `SparseKroneckerSumConstructor`](SparseKroneckerSumConstructor/index.md)
- [Parent package](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/numerics/linear_algebra/kronecker.py`
- Tests: `tests/projectkoios/physkit/numerics/linear_algebra/kronecker/`

## Evidence

Tests verify C-order state indexing, exact two- and three-axis shapes, real and
complex dtype preservation, spectra equal to sums of axis spectra, canonical CSR
storage, and invalid input rejection. These tests establish numerical software
behavior only.
