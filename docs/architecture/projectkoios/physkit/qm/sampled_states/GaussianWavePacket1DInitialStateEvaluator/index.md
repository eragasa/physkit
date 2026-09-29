# `GaussianWavePacket1DInitialStateEvaluator`

## Responsibility

`GaussianWavePacket1DInitialStateEvaluator` maps one complete initial-state
evaluation request to one `SampledQuantumState1D`. It evaluates only the state
at the initial time; TDSE solvers own subsequent evolution.

## Local mapping

- Code: `src/python/projectkoios/physkit/qm/sampled_states.py::GaussianWavePacket1DInitialStateEvaluator`
- Integration tests: `tests/projectkoios/physkit/qm/sampled_states/test__GaussianWavePacket1DInitialState__evaluate.py`

## Navigation

- [Module](../index.md)
