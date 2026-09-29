# `TownsendClosedFormCurrentEvaluator`

## Responsibility

`TownsendClosedFormCurrentEvaluator` is a stateless ActionObject that evaluates

$$
i=\frac{i_0M}{1-r}
$$

for a `TownsendDischargeState` with $r<1$.

At $r\ge1$, it returns an infinite current with `converged=False`. Closed-form
results use `term_count=0`.

## Local mapping

- Code: `src/python/projectkoios/physkit/plasmas/gas_discharge/townsend.py::TownsendClosedFormCurrentEvaluator`
- Tests: `tests/projectkoios/physkit/plasmas/gas_discharge/townsend/test__TownsendClosedFormCurrentEvaluator__execute.py`

## Navigation

- [Module](../index.md)
