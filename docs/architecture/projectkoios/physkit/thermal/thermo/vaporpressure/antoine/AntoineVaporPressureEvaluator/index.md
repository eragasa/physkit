# `AntoineVaporPressureEvaluator`

## Responsibility

`AntoineVaporPressureEvaluator` is the ActionObject mapping one typed evaluation
request to a correlated pressure response. Ordinary callers use
`AntoineVaporPressureModel.evaluate(...)`.

## Contract

The action converts physical temperature quantities to the coefficient-table
unit, optionally enforces the validity range, evaluates the Antoine equation,
and converts native pressures to the explicitly requested pressure unit.
Singular denominators and nonfinite pressure results are rejected.

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/thermo/vaporpressure/antoine.py::AntoineVaporPressureEvaluator`
- Tests: `tests/projectkoios/physkit/thermal/thermo/vaporpressure/antoine/test__AntoineVaporPressureModel__evaluate.py`

## Navigation

- [Module](../index.md)
