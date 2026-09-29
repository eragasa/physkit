# `MaxwellBoltzmannSpeedDistributionEvaluator`

## Responsibility

`MaxwellBoltzmannSpeedDistributionEvaluator` is the ActionObject that maps one
typed speed-distribution request to a correlated unit-aware response. Ordinary
callers use `MaxwellBoltzmannGasState.evaluate_speed_distribution(...)` rather
than constructing the ActionObject or request directly.

## Contract

- The ActionObject exposes `action(request=...)`.
- State parameters are converted to kelvin and kilograms per mole for formula
  evaluation.
- Requested speeds are converted to metres per second.
- Returned probability density uses reciprocal requested-speed units.
- Grid construction, quadrature policy, plotting, and real-gas validation remain
  outside the ActionObject.

## Navigation

- [Implementation](implementation/index.md)
- [Gas state](../MaxwellBoltzmannGasState/index.md)
- [Module](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/statmech/kinetic_theory.py::MaxwellBoltzmannSpeedDistributionEvaluator`
- Tests: `tests/projectkoios/physkit/thermal/statmech/kinetic_theory/test__MaxwellBoltzmannGasState__evaluate_speed_distribution.py`
