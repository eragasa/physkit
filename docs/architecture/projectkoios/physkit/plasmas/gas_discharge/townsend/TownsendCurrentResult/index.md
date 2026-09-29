# `TownsendCurrentResult`

## Responsibility

`TownsendCurrentResult` is an immutable ResultObject correlating current,
avalanche gain, feedback factor, term count, and convergence status for one
evaluation route.

## Contract

- `current_amperes`, `avalanche_gain`, and `feedback_factor` are built-in floats.
- `term_count` is a nonnegative built-in integer.
- `converged` is a built-in boolean.
- Infinite current represents the model threshold outcome returned when the
  feedback factor is at least one.

## Local mapping

- Code: `src/python/projectkoios/physkit/plasmas/gas_discharge/townsend.py::TownsendCurrentResult`
- Tests: `tests/projectkoios/physkit/plasmas/gas_discharge/townsend/test__TownsendCurrentResult__init.py`

## Navigation

- [Module](../index.md)
