# Module `projectkoios.physkit.thermal.thermo.vaporpressure.antoine`

## Current responsibility

This module owns unit-aware Antoine coefficient records, physical validity
ranges, typed evaluation requests, numerical evaluation, and correlated
pressure responses. It does not own coefficient fitting or material-specific
source acceptance.

## Supported façade and response

- [`AntoineVaporPressureModel`](AntoineVaporPressureModel/index.md)
- [`AntoineTemperatureRange`](AntoineTemperatureRange/index.md)
- [`AntoineVaporPressureEvaluation`](AntoineVaporPressureEvaluation/index.md)

## Typed operation request

- [`AntoineVaporPressureEvaluationRequest`](AntoineVaporPressureEvaluationRequest/index.md)

`AntoineVaporPressureEvaluator` is the internal ActionObject behind
`AntoineVaporPressureModel.evaluate(...)`.

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/thermo/vaporpressure/antoine.py`
- Tests: `tests/projectkoios/physkit/thermal/thermo/vaporpressure/antoine/`
- Laboratory: `notebooks/thermal/thermo/vapor-pressure/antoine-vapor-pressure.ipynb`
