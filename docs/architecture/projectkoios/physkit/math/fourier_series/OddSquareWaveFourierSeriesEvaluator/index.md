# `OddSquareWaveFourierSeriesEvaluator`

## Responsibility

`OddSquareWaveFourierSeriesEvaluator` is an immutable ActionObject that owns the
finite odd-harmonic sum for the conventional $2\pi$-periodic odd square wave.
Its `term_count` field selects the finite truncation, and `execute` evaluates
that truncation at caller-supplied angles.

## Contract

- `term_count` is a positive built-in integer; booleans and NumPy integers are
  rejected.
- Input is an exact NumPy `float64` array containing finite, dimensionless angles
  in radians.
- Output is a newly allocated `float64` array with the same shape.
- Evaluation does not mutate or alias the input.
- Plotting, sampling-grid selection, error policy, and lesson interpretation are
  not owned by this class.

## Navigation

- [Implementation](implementation/index.md)
- [Module](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/math/fourier_series.py::OddSquareWaveFourierSeriesEvaluator`
- Construction tests: `tests/projectkoios/physkit/math/fourier_series/test__OddSquareWaveFourierSeriesEvaluator__init.py`
- Evaluation tests: `tests/projectkoios/physkit/math/fourier_series/test__OddSquareWaveFourierSeriesEvaluator__execute.py`
