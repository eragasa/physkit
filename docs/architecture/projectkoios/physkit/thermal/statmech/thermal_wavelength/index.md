# Module `projectkoios.physkit.thermal.statmech.thermal_wavelength`

## Current responsibility

This module owns unit-aware evaluation of the canonical thermal de Broglie
wavelength and the associated unitless parameter $n\lambda_T^3$. It does not
apply a universal classical-versus-quantum classification threshold.

## Public façade and records

- [`ThermalDeBroglieWavelengthModel`](ThermalDeBroglieWavelengthModel/index.md)
- [`ThermalDeBroglieWavelengthEvaluationRequest`](ThermalDeBroglieWavelengthEvaluationRequest/index.md)
- [`ThermalDeBroglieWavelengthEvaluation`](ThermalDeBroglieWavelengthEvaluation/index.md)
- [`ThermalDegeneracyParameterEvaluationRequest`](ThermalDegeneracyParameterEvaluationRequest/index.md)
- [`ThermalDegeneracyParameterEvaluation`](ThermalDegeneracyParameterEvaluation/index.md)

Internal ActionObjects implement typed `action(request=...)` methods. Callers use
`evaluate_wavelengths(...)` and `evaluate_degeneracy_parameter(...)`.

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/statmech/thermal_wavelength.py`
- Tests: `tests/projectkoios/physkit/thermal/statmech/thermal_wavelength/`
- Laboratory: `notebooks/thermal/statmech/quantum/thermal-de-broglie-wavelength.ipynb`
- Derivation: `docs/lecture-notes/statistical-mechanics/thermal-de-broglie-wavelength/index.md`
