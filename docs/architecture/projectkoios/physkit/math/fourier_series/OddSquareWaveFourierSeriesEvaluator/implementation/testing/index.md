# `OddSquareWaveFourierSeriesEvaluator` testing

## Current coverage

The construction tests cover positive, zero, negative, boolean, and NumPy
integer term counts. Evaluation tests compare one- and three-term results with
independently written formulas, verify shape and input preservation, and reject
non-`float64`, non-array, NaN, and infinite inputs.

| Evidence kind | Current result |
| --- | --- |
| Implementation conformance | Covered for the documented constructor and evaluation contracts. |
| Numerical verification | Bounded agreement with one- and three-term formulas at selected binary64 inputs using absolute tolerance `1e-15`. |
| Scientific validation | Not applicable to this standalone mathematical evaluator. |
| Pedagogical validation | Not evaluated by package tests or notebook execution. |
| Human acceptance | Not established by automated checks. |

## Local mapping

- `tests/projectkoios/physkit/math/fourier_series/test__OddSquareWaveFourierSeriesEvaluator__init.py`
- `tests/projectkoios/physkit/math/fourier_series/test__OddSquareWaveFourierSeriesEvaluator__execute.py`

## Navigation

- [Implementation](../index.md)
- [Mathematics](../mathematics/index.md)
- [Class contract](../../index.md)
