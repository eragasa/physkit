# `ThreeDimensionalVonMisesStressEvaluator`

## Responsibility

`ThreeDimensionalVonMisesStressEvaluator` is a stateless ActionObject for a
represented $3\times3$ stress tensor. It averages each off-diagonal pair and
evaluates

$$
\sigma_{\mathrm{vM}}=
\sqrt{
\frac{1}{2}\left[
(\sigma_{xx}-\sigma_{yy})^2
+(\sigma_{yy}-\sigma_{zz})^2
+(\sigma_{zz}-\sigma_{xx})^2
\right]
+3\left(\tau_{xy}^2+\tau_{yz}^2+\tau_{xz}^2\right)
}.
$$

## Contract

- Input is an exact NumPy `float64` array with shape `(3, 3)` and finite entries.
- Tensor entries use one consistent stress unit.
- Every transposed off-diagonal pair is averaged before evaluation.
- Output is a built-in float in the input stress unit.
- NumPy binary64 arithmetic can produce overflow or a nonfinite result for
  sufficiently large finite inputs.

## Verification

Tests cover hydrostatic, uniaxial, pure-shear, asymmetric, and embedded
plane-stress tensors together with array ownership, dtype, shape, finite values,
and input preservation.

## Local mapping

- Code: `src/python/projectkoios/physkit/mechanics/continuum_stress.py::ThreeDimensionalVonMisesStressEvaluator`
- Tests: `tests/projectkoios/physkit/mechanics/continuum_stress/test__ThreeDimensionalVonMisesStressEvaluator__execute.py`

## Navigation

- [Module](../index.md)
- [Plane-stress evaluator](../PlaneStressVonMisesEvaluator/index.md)
