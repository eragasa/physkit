# Module `projectkoios.physkit.plasmas.gas_discharge.townsend`

## Current responsibility

This module owns a Townsend-discharge state, correlated current result, and
three evaluation routes for the geometric secondary-emission model.

## Public classes

- [`TownsendDischargeState`](TownsendDischargeState/index.md)
- [`TownsendCurrentResult`](TownsendCurrentResult/index.md)
- [`TownsendClosedFormCurrentEvaluator`](TownsendClosedFormCurrentEvaluator/index.md)
- [`TownsendGenerationalCurrentEvaluator`](TownsendGenerationalCurrentEvaluator/index.md)
- [`TownsendFixedPointCurrentEvaluator`](TownsendFixedPointCurrentEvaluator/index.md)

## Source lineage

The implementation was extracted from
`src/physkit/plasmas/gas_discharge/townsend.ipynb`, now maintained as
`notebooks/plasma-physics/gas-discharge/townsend-current.ipynb`. The former
`breakdown.ipynb` and `paschen.ipynb` package artifacts were empty and were
removed.

## Local mapping

- Code: `src/python/projectkoios/physkit/plasmas/gas_discharge/townsend.py`
- Tests: `tests/projectkoios/physkit/plasmas/gas_discharge/townsend/`
- Lecture note: `docs/lecture-notes/plasma-physics/townsend-discharge/index.md`
