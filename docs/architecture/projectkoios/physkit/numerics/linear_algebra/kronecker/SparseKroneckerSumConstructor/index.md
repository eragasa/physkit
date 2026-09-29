# Class `projectkoios.physkit.numerics.linear_algebra.kronecker.SparseKroneckerSumConstructor`

## Current contract

The stateless constructor assembles the sparse Kronecker sum of two or three
ordered square axis operators. It returns a new canonical CSR array and does not
mutate caller-owned sparse inputs.

## Invariants

- Exactly two or three axis operators are supplied in a tuple.
- Every operator is finite, numeric, nonempty, and square.
- The result shape is the product state size squared.
- The result dtype is the NumPy result type of all axis operators.
- C-order flattening makes the final tuple axis the fastest-varying state index.

## Navigation

- [Parent module](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/numerics/linear_algebra/kronecker.py::SparseKroneckerSumConstructor`
- Tests: `tests/projectkoios/physkit/numerics/linear_algebra/kronecker/test__SparseKroneckerSumConstructor__execute.py`

## Evidence

Tests compare represented spectra with independent sums of one-dimensional
spectra for real 2D and complex 3D examples and verify ordering and failure
behavior. They do not establish the adequacy of any consuming physical model.
