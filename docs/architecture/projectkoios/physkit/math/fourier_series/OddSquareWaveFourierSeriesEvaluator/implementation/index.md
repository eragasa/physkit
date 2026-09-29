# `OddSquareWaveFourierSeriesEvaluator` implementation

## Current implementation

Construction validates the exact finite truncation. Evaluation validates an
exact finite `float64` array, allocates a zero-filled result with the same shape,
and accumulates each requested odd sine harmonic in ascending order.

The explicit accumulation preserves the represented ordering of the extracted
notebook formula while keeping memory proportional to the input array size.

## Navigation

- [Mathematics](mathematics/index.md)
- [Testing](testing/index.md)
- [Source lineage](references/index.md)
- [Class contract](../index.md)

## Evidence boundary

Tests establish the input contract and agreement with selected independently
written finite sums. They do not establish uniform convergence at jump
locations, pedagogical validation, or suitability for a physical model.
