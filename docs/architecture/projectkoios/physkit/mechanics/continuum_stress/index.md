# Module `projectkoios.physkit.mechanics.continuum_stress`

## Current responsibility

This module owns plane-stress and three-dimensional von Mises equivalent-stress
evaluation. Both evaluators accept one consistent caller-selected stress unit,
average transposed off-diagonal pairs, and return a scalar in the input unit.

## Public classes

- [`PlaneStressVonMisesEvaluator`](PlaneStressVonMisesEvaluator/index.md)
- [`ThreeDimensionalVonMisesStressEvaluator`](ThreeDimensionalVonMisesStressEvaluator/index.md)

## Imports

```python
from projectkoios.physkit.mechanics.continuum_stress import (
    PlaneStressVonMisesEvaluator,
    ThreeDimensionalVonMisesStressEvaluator,
)
```

## Source lineage

The implementation consolidates formulas from:

- `notebooks/materials-science/mechanical-properties/two-dimensional-von-mises-stress.ipynb`
- `notebooks/materials-science/mechanical-properties/three-dimensional-von-mises-stress.ipynb`

Git history retains both source notebooks. Their maintained laboratory now lives
at `notebooks/mechanics/continuum-mechanics/von-mises-equivalent-stress.ipynb`.

## Local mapping

- Code: `src/python/projectkoios/physkit/mechanics/continuum_stress.py`
- Tests: `tests/projectkoios/physkit/mechanics/continuum_stress/`
