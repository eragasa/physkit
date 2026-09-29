# `MaxwellBoltzmannGasState`

## Responsibility

`MaxwellBoltzmannGasState` is an immutable unit-aware DataObject containing the
absolute temperature and molar mass required by the Maxwell–Boltzmann speed
model. It owns their intrinsic validity, the three characteristic speeds, and
the `evaluate_speed_distribution(...)` façade.

## Contract

- `temperature` is a positive `ScalarQuantity` with temperature-compatible
  physical units; affine conversion to kelvin is supported.
- `molar_mass` is a positive `ScalarQuantity` with molar-mass-compatible
  physical units.
- Most probable, mean, and root-mean-square speeds are `ScalarQuantity` values
  in metres per second.
- Speed-distribution evaluation accepts a `VectorQuantity` in compatible speed
  units and returns density in reciprocal requested-speed units.
- The record does not claim that a real gas satisfies the model assumptions.

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/statmech/kinetic_theory.py::MaxwellBoltzmannGasState`
- Construction tests: `tests/projectkoios/physkit/thermal/statmech/kinetic_theory/test__MaxwellBoltzmannGasState__init.py`
- Characteristic-speed tests: `tests/projectkoios/physkit/thermal/statmech/kinetic_theory/test__MaxwellBoltzmannGasState__characteristic_speeds.py`
- Evaluation tests: `tests/projectkoios/physkit/thermal/statmech/kinetic_theory/test__MaxwellBoltzmannGasState__evaluate_speed_distribution.py`

## Navigation

- [Module](../index.md)
