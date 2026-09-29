# Module `projectkoios.physkit.thermal.transport.phase_change.hertz_knudsen3d`

## Current responsibility

This module owns signed Hertz--Knudsen number and mass fluxes for a
three-dimensional ideal gas incident on a two-dimensional planar interface. It
retains separate evaporation and condensation coefficients and does not clamp
negative net flux.

## Public façade and records

- [`PlanarHertzKnudsen3DNetFluxModel`](PlanarHertzKnudsen3DNetFluxModel/index.md)
- [`PlanarHertzKnudsen3DFluxEvaluationRequest`](PlanarHertzKnudsen3DFluxEvaluationRequest/index.md)
- [`PlanarHertzKnudsen3DFluxEvaluation`](PlanarHertzKnudsen3DFluxEvaluation/index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/transport/phase_change/hertz_knudsen3d.py`
- Tests: `tests/projectkoios/physkit/thermal/transport/phase_change/hertz_knudsen3d/`
- Laboratory: `notebooks/thermal/transport/phase-change/hertz-knudsen-net-flux.ipynb`
- Derivation: `docs/lecture-notes/thermal-transport/phase-change/hertz-knudsen/index.md`
