# `TownsendGenerationalCurrentEvaluator`

## Responsibility

`TownsendGenerationalCurrentEvaluator` is an ActionObject that accumulates

$$
i_0M,\quad i_0Mr,\quad i_0Mr^2,\ldots
$$

until the newest generation meets the configured relative stopping rule or the
iteration limit is reached. An optional analytic correction adds the remaining
geometric tail after convergence.

## Contract

The evaluator owns a positive finite built-in float `relative_tolerance`, a
positive built-in integer `maximum_iterations`, and a built-in boolean
`apply_tail_correction`. The result term count includes the primary avalanche
term.

## Local mapping

- Code: `src/python/projectkoios/physkit/plasmas/gas_discharge/townsend.py::TownsendGenerationalCurrentEvaluator`
- Construction tests: `tests/projectkoios/physkit/plasmas/gas_discharge/townsend/test__TownsendGenerationalCurrentEvaluator__init.py`
- Evaluation tests: `tests/projectkoios/physkit/plasmas/gas_discharge/townsend/test__TownsendGenerationalCurrentEvaluator__execute.py`

## Navigation

- [Module](../index.md)
