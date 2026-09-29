# Module `projectkoios.physkit.thermal.statmech.kinetic_theory`

## Current responsibility

This module owns unit-aware state and numerical evaluation for the
Maxwell–Boltzmann speed distribution. It distinguishes physical model
parameters, closed-form characteristic speeds, sampled probability density,
finite-grid quadrature, and claims about real gases.

## Supported data, façade, and response objects

- [`MaxwellBoltzmannGasState`](MaxwellBoltzmannGasState/index.md)
- [`MaxwellBoltzmannSpeedDistributionEvaluation`](MaxwellBoltzmannSpeedDistributionEvaluation/index.md)
- [`HardSphereIdealGasState`](HardSphereIdealGasState/index.md)

## Typed operation request

- [`MaxwellBoltzmannSpeedDistributionEvaluationRequest`](MaxwellBoltzmannSpeedDistributionEvaluationRequest/index.md)

`MaxwellBoltzmannSpeedDistributionEvaluator` is the internal ActionObject behind
`MaxwellBoltzmannGasState.evaluate_speed_distribution(...)`.

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/statmech/kinetic_theory.py`
- Tests: `tests/projectkoios/physkit/thermal/statmech/kinetic_theory/`
- Laboratories:
  - `notebooks/thermal/statmech/kinetic/maxwell-boltzmann-speed-distribution.ipynb`
  - `notebooks/thermal/statmech/kinetic/mfp.ipynb`
