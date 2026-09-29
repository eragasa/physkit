# `MaxwellBoltzmannSpeedDistributionEvaluator` mathematics

For nonnegative speed $v$, absolute temperature $T$, molar mass $M$, and SI
molar gas constant $R$, the evaluator computes

$$
f(v;T,M)=\frac{4}{\sqrt{\pi}}
\left(\frac{M}{2RT}\right)^{3/2}v^2
\exp\!\left(-\frac{Mv^2}{2RT}\right).
$$

| Symbol | Meaning | SI unit | Domain |
| --- | --- | --- | --- |
| $v$ | Speed magnitude | m/s | finite, nonnegative binary64 value |
| $T$ | Absolute temperature | K | positive finite built-in float |
| $M$ | Molar mass | kg/mol | positive finite built-in float |
| $R$ | Molar gas constant | J/(mol K) | package constant `SI.R_g` |
| $f$ | Probability density with respect to speed | s/m | nonnegative binary64 value |

The continuous model is normalized on $[0,\infty)$. Any notebook quadrature on a
finite grid approximates that integral and is not part of the evaluator.

## Navigation

- [Implementation](../index.md)
- [Testing](../testing/index.md)
- [Class contract](../../index.md)
