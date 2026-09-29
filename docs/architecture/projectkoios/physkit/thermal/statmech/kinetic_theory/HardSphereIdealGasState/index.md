# `HardSphereIdealGasState`

## Responsibility

`HardSphereIdealGasState` is an immutable unit-aware DataObject representing an
equilibrium ideal gas of identical hard-sphere particles. It owns pressure,
absolute temperature, collision diameter, and their intrinsic collision cross
section, number density, and mean free path.

## Contract

- Pressure is a positive `ScalarQuantity` in pressure-compatible units.
- Temperature is above absolute zero and may use affine-compatible physical
  temperature units.
- Collision diameter is a positive `ScalarQuantity` in length-compatible units.
- Derived cross section, number density, and mean free path are returned in
  square metres, inverse cubic metres, and metres, respectively.
- The mean-free-path convention includes the $\sqrt{2}$ relative-speed factor
  for identical particles.

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/statmech/kinetic_theory.py::HardSphereIdealGasState`
- Tests: `tests/projectkoios/physkit/thermal/statmech/kinetic_theory/test__HardSphereIdealGasState__properties.py`
- Laboratory: `notebooks/thermal/statmech/kinetic/mfp.ipynb`

## Navigation

- [Module](../index.md)
