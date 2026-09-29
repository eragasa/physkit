# `BlackbodyWavelengthSpectrumModel` implementation

The evaluator converts wavelength and temperature to metres and kelvin, computes
all three spectral densities in SI units, rejects non-finite binary64 results,
and converts them to the requested compatible spectral-density unit.

The Planck denominator is evaluated as `-expm1(-x)` after factoring out
$\exp(-x)$. This avoids direct overflow of $\exp(x)$ at large $x$ and reduces
cancellation at small positive $x$.

## Navigation

- [Mathematics](mathematics/index.md)
- [References](references/index.md)
- [Testing](testing/index.md)
- [Class](../index.md)
