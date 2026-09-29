# Vapor-pressure correlations

Reusable unit-aware Antoine behavior is owned by
`projectkoios.physkit.thermal.thermo.vaporpressure.antoine`:

- `AntoineVaporPressureModel` retains unit-bearing coefficients, native units,
  an optional `AntoineTemperatureRange`, and provenance;
- `AntoineVaporPressureModel.evaluate(...)` accepts compatible physical
  temperature units and an explicit output pressure unit; and
- `AntoineVaporPressureEvaluation` retains the complete request and correlated
  pressure vector.

See the maintained
[Antoine lecture note](lecture-notes/thermodynamics/vapor-pressure/antoine/index.md)
and
[computational laboratory](../notebooks/thermal/thermo/vapor-pressure/antoine-vapor-pressure.ipynb).
