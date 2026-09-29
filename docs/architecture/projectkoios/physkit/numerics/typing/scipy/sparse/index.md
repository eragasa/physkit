# Module `projectkoios.physkit.numerics.typing.scipy.sparse`

## Current responsibility

The module defines the common SciPy sparse matrix-or-array annotation used by
maintained numerical and quantity implementations.

## Public contract

`SparseMatrix` accepts SciPy's sparse matrix and sparse array families. Numeric
dtype and canonical-storage validation remain with consuming owners.

## Navigation

- [Parent package](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/numerics/typing/scipy/sparse.py`

## Evidence

Sparse eigenproblem and immutable sparse-quantity tests verify consuming
contracts.
