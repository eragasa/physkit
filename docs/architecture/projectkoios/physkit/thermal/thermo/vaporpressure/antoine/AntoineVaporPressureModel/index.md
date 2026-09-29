# `AntoineVaporPressureModel`

## Responsibility

`AntoineVaporPressureModel` is an immutable unit-aware DataObject retaining one
Antoine coefficient set, coefficient-table units, optional physical validity
range, and source description. Its `evaluate(...)` façade constructs a typed
request and returns pressures in an explicitly requested physical unit.

## Contract

- `A` is a unitless `ScalarQuantity`.
- `B` and `C` are `ScalarQuantity` values in the declared coefficient
  temperature unit.
- Coefficient temperature and pressure units are compatible physical units.
- The optional validity range uses explicit temperature quantities.
- `source` is nonempty provenance text.

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/thermo/vaporpressure/antoine.py::AntoineVaporPressureModel`
- Construction tests: `tests/projectkoios/physkit/thermal/thermo/vaporpressure/antoine/test__AntoineVaporPressureModel__init.py`
- Evaluation tests: `tests/projectkoios/physkit/thermal/thermo/vaporpressure/antoine/test__AntoineVaporPressureModel__evaluate.py`

## Navigation

- [Module](../index.md)
