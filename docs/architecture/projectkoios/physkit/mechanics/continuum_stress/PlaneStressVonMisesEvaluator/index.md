# `PlaneStressVonMisesEvaluator`

## Responsibility

`PlaneStressVonMisesEvaluator` is a stateless ActionObject for a represented
$2\times2$ plane-stress tensor. It averages the off-diagonal pair and evaluates

$$
\sigma_{\mathrm{vM}}=
\sqrt{\sigma_{xx}^2-\sigma_{xx}\sigma_{yy}+\sigma_{yy}^2+3\tau_{xy}^2}.
$$

## Contract

- Input is an exact NumPy `float64` array with shape `(2, 2)` and finite entries.
- Tensor entries use one consistent stress unit.
- The off-diagonal shear value is
  $\tau_{xy}=(\sigma_{xy}+\sigma_{yx})/2$.
- Output is a built-in float in the input stress unit.
- NumPy binary64 arithmetic can produce overflow or a nonfinite result for
  sufficiently large finite inputs.

## Verification

Tests cover uniaxial stress, pure shear, asymmetric off-diagonal entries, input
preservation, array ownership, dtype, shape, and finite values.

## Local mapping

- Code: `src/python/projectkoios/physkit/mechanics/continuum_stress.py::PlaneStressVonMisesEvaluator`
- Tests: `tests/projectkoios/physkit/mechanics/continuum_stress/test__PlaneStressVonMisesEvaluator__execute.py`

## Navigation

- [Module](../index.md)
- [Three-dimensional evaluator](../ThreeDimensionalVonMisesStressEvaluator/index.md)
