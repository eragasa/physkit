# Module `projectkoios.physkit.thermal.statmech.distributions.boltzmann_energy`

## Current responsibility

This module owns the normalized exponential density
$f(E)=\exp(-E/\theta)/\theta$ on nonnegative energy, where $\theta$ is a
positive thermal-energy scale. The model assumes a constant density of states;
it is not the three-dimensional translational kinetic-energy distribution.

## Public façade and records

- [`BoltzmannExponentialEnergyDistribution`](BoltzmannExponentialEnergyDistribution/index.md)
- [`BoltzmannExponentialEnergyEvaluationRequest`](BoltzmannExponentialEnergyEvaluationRequest/index.md)
- [`BoltzmannExponentialEnergyEvaluation`](BoltzmannExponentialEnergyEvaluation/index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/thermal/statmech/distributions/boltzmann_energy.py`
- Tests: `tests/projectkoios/physkit/thermal/statmech/distributions/boltzmann_energy/`
- Laboratory: `notebooks/thermal/statmech/distributions/boltzmann-exponential-energy-distribution.ipynb`
