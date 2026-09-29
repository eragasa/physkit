# `TownsendFixedPointCurrentEvaluator`

## Responsibility

`TownsendFixedPointCurrentEvaluator` is an ActionObject that applies

$$
i_{k+1}=i_0M+ri_k
$$

until the configured stopping rule or iteration limit is reached.

## Contract

The evaluator owns a positive finite built-in float `relative_tolerance` and a
positive built-in integer `maximum_iterations`. Its result reports the completed
iteration count and convergence status.

## Local mapping

- Code: `src/python/projectkoios/physkit/plasmas/gas_discharge/townsend.py::TownsendFixedPointCurrentEvaluator`
- Construction tests: `tests/projectkoios/physkit/plasmas/gas_discharge/townsend/test__TownsendFixedPointCurrentEvaluator__init.py`
- Evaluation tests: `tests/projectkoios/physkit/plasmas/gas_discharge/townsend/test__TownsendFixedPointCurrentEvaluator__execute.py`

## Navigation

- [Module](../index.md)
