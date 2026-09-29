# Module `projectkoios.physkit.thermal.statmech.transport.knudsen`

## Current responsibility

This module owns unit-aware evaluation of $\mathrm{Kn}=\lambda/L$ from mean free
paths and one explicit characteristic length. It does not assign named flow
regimes or embed threshold conventions.

## Public façade and records

- [`KnudsenNumberModel`](KnudsenNumberModel/index.md)
- [`KnudsenNumberEvaluationRequest`](KnudsenNumberEvaluationRequest/index.md)
- [`KnudsenNumberEvaluation`](KnudsenNumberEvaluation/index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/statmech/transport/knudsen.py`
- Tests: `tests/projectkoios/physkit/thermal/statmech/transport/knudsen/`
- Laboratory: `notebooks/thermal/statmech/transport/knudsen-number.ipynb`
