# `MaxwellBoltzmannSpeedDistributionEvaluator` testing

## Current coverage

Tests cover temperature and molar-mass units, compatible unit conversion,
positive physical quantities, selected formula values, reciprocal speed-density
units, finite-grid normalization, and the analytic most-probable-speed location.

| Evidence kind | Current result |
| --- | --- |
| Implementation conformance | Covered for the documented state, request, ActionObject, and response contracts. |
| Numerical verification | Bounded selected-value, normalization, conversion, and peak-location checks using synthetic test data. |
| Scientific validation | Not evaluated; no experimental gas data or declared validation protocol is used. |
| Pedagogical validation | Not evaluated by package tests or notebook execution. |
| Human acceptance | Not established by automated checks. |

## Local mapping

- `tests/projectkoios/physkit/thermal/statmech/kinetic_theory/test__MaxwellBoltzmannGasState__init.py`
- `tests/projectkoios/physkit/thermal/statmech/kinetic_theory/test__MaxwellBoltzmannGasState__characteristic_speeds.py`
- `tests/projectkoios/physkit/thermal/statmech/kinetic_theory/test__MaxwellBoltzmannGasState__evaluate_speed_distribution.py`

## Navigation

- [Implementation](../index.md)
- [Mathematics](../mathematics/index.md)
- [Class contract](../../index.md)
