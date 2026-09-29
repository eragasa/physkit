# `OddSquareWaveFourierSeriesEvaluator` source lineage

## Internal extraction

The initial formula was extracted from two byte-identical exploratory notebooks:

- `notebooks/math/fourier_series.ipynb`
- `notebooks/math/fourier/fourier_series.ipynb`

Git history retains both source identities. Their duplicate implementations were
replaced by one defining module and one maintained computational laboratory.
The extraction preserves the finite odd-harmonic formula while adding explicit
runtime types, finite-value checks, tests, and ownership boundaries.

The mathematical derivation is maintained in
[`docs/lecture-notes/foundations/fourier-series/index.md`](../../../../../../../../lecture-notes/foundations/fourier-series/index.md).
No external publication is claimed as the source of the extracted software
implementation.

## Navigation

- [Implementation](../index.md)
- [Mathematics](../mathematics/index.md)
- [Class contract](../../index.md)
