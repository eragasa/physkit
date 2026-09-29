# `OddSquareWaveFourierSeriesEvaluator` mathematics

For a positive term count $M$ and dimensionless angle $x$ in radians, the
evaluator computes

<a id="eq-odd-square-wave-finite-series"></a>
$$
S_M(x)=\frac{4}{\pi}\sum_{j=0}^{M-1}
\frac{\sin((2j+1)x)}{2j+1}.
$$

This is a finite numerical representation of the Fourier series for the
conventional $2\pi$-periodic odd square wave. The evaluator returns $S_M$; it
does not return the discontinuous target function or an error estimate.

| Symbol | Meaning | Unit | Domain |
| --- | --- | --- | --- |
| $M$ | Number of retained odd harmonics | dimensionless | positive built-in integer |
| $j$ | Zero-based term index | dimensionless | $0,\ldots,M-1$ |
| $x$ | Evaluation angle | radians | finite binary64 number |
| $S_M(x)$ | Finite-series value | dimensionless | binary64 result |

The implementation evaluates arrays elementwise and preserves their shape.
Floating-point rounding follows NumPy binary64 sine and arithmetic behavior.
No overflow guarantee is made for an unbounded caller-selected term count.

## Navigation

- [Implementation](../index.md)
- [Testing](../testing/index.md)
- [Class contract](../../index.md)
