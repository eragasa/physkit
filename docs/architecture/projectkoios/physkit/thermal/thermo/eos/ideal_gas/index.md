# Module `projectkoios.physkit.thermal.thermo.eos.ideal_gas`

## Current responsibility

This module owns a unit-aware ideal-gas equation of state, single-isotherm
pressure evaluation, and ordered multi-isotherm construction.

## Supported façade and responses

- [`IdealGasEquationOfState`](IdealGasEquationOfState/index.md)
- [`IdealGasPressureEvaluation`](IdealGasPressureEvaluation/index.md)
- [`IdealGasIsotherms`](IdealGasIsotherms/index.md)

## Typed requests

- [`IdealGasPressureEvaluationRequest`](IdealGasPressureEvaluationRequest/index.md)
- [`IdealGasIsothermsEvaluationRequest`](IdealGasIsothermsEvaluationRequest/index.md)

Internal ActionObjects implement `action(request=...)`. Ordinary callers use
`evaluate_pressure(...)` or `evaluate_isotherms(...)`.

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/thermo/eos/ideal_gas.py`
- Tests: `tests/projectkoios/physkit/thermal/thermo/eos/ideal_gas/`
- Laboratory: `notebooks/thermal/thermo/eos/ideal_gas.ipynb`
