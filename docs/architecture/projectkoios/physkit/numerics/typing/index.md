# Package `projectkoios.physkit.numerics.typing`

## Current responsibility

The package owns shared type aliases for backend-independent scalar values and
supported NumPy and SciPy numerical representations.

## Public contract

Backend-specific aliases remain in their defining modules rather than being
recursively re-exported.

## Navigation

- [Module `base`](base/index.md)
- [Package `numpy`](numpy/index.md)
- [Package `scipy`](scipy/index.md)
- [Parent package](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/numerics/typing/`
- Tests: aliases are exercised through their consuming numerical and model tests.

## Evidence

Compilation and consuming-module tests verify that supported annotations resolve
under Python 3.14. This is typing conformance rather than runtime validation.
