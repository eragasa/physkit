# `Piab2DAnalyticalEvaluator`

## Responsibility

`Piab2DAnalyticalEvaluator` is a stateless ActionObject that enumerates every
positive quantum-number pair within explicit axis bounds, evaluates

$$
E_{n_x,n_y}=\frac{\hbar^2\pi^2}{2m}
\left(\frac{n_x^2}{L_x^2}+\frac{n_y^2}{L_y^2}\right),
$$

converts energies to the model's selected numerical scale, and orders states by
nondecreasing energy with lexicographic tie-breaking. Its `execute` inputs are
keyword-only.

## Local mapping

- Code: `src/python/projectkoios/physkit/qm/piab2d/tise/analytical/solution.py::Piab2DAnalyticalEvaluator`
- Tests: `tests/projectkoios/physkit/qm/piab2d/tise/analytical/solution/test__Piab2DAnalyticalEvaluator__execute.py`

## Navigation

- [Module](../index.md)
