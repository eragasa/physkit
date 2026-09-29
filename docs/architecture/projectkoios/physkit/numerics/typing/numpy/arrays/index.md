# Module `projectkoios.physkit.numerics.typing.numpy.arrays`

## Current responsibility

The module defines canonical NumPy aliases for real, complex, and integer
arrays, vectors, and matrices.

## Public contract

Real aliases use `numpy.float64`, complex aliases use `numpy.complex128`, and
integer aliases use `numpy.int64`. Vector and matrix names communicate intended
rank; runtime shape validation remains with the consuming owner.

## Navigation

- [Parent package](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/numerics/typing/numpy/arrays.py`

## Evidence

Python compilation and consuming-module tests verify annotation resolution.
