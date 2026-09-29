# Package `projectkoios.physkit.numerics.typing.numpy`

## Current responsibility

The package owns precise NumPy dtype aliases used by maintained numerical and
model implementations.

## Public contract

Aliases are imported from their defining module and describe float64,
complex128, and int64 arrays with vector and matrix intent where applicable.

## Navigation

- [Module `arrays`](arrays/index.md)
- [Parent package](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/numerics/typing/numpy/`

## Evidence

Consuming numerical, quantity, and quantum-model tests exercise these aliases.
