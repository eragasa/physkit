# Module `projectkoios.physkit.qm.sampled_states`

## Current responsibility

This module owns one-dimensional sampled general quantum states, Gaussian
wave-packet initial-state sampling, explicit weighted state normalization, and explicit weighted state normalization. TDSE solvers own time evolution and
return sampled evolution responses from this module.

## Public classes

- [`GaussianWavePacket1DInitialState`](GaussianWavePacket1DInitialState/index.md)
- [`GaussianWavePacket1DInitialStateModel`](GaussianWavePacket1DInitialStateModel/index.md)
- [`GaussianWavePacket1DInitialStateEvaluationRequest`](GaussianWavePacket1DInitialStateEvaluationRequest/index.md)
- [`GaussianWavePacket1DInitialStateEvaluator`](GaussianWavePacket1DInitialStateEvaluator/index.md)
- [`SampledQuantumState1D`](SampledQuantumState1D/index.md)
- [`SampledQuantumStateEvolution1D`](SampledQuantumStateEvolution1D/index.md)
- [`SampledQuantumState1DNormalizationRequest`](SampledQuantumState1DNormalizationRequest/index.md)
- [`SampledQuantumState1DNormalization`](SampledQuantumState1DNormalization/index.md)
- [`SampledQuantumState1DNormalizer`](SampledQuantumState1DNormalizer/index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/qm/sampled_states.py`
- Tests: `tests/projectkoios/physkit/qm/sampled_states/`
- Lecture note: `docs/lecture-notes/qm/piab1d/piab1d__basis_projection.md`
