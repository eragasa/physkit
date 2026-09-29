# Fourier series and the odd square wave

## Purpose

This note introduces the finite odd-harmonic Fourier representation used by the
[square-wave computational laboratory](../../../../notebooks/foundations/fourier-and-periodic-methods/square-wave-fourier-series.ipynb).
It distinguishes the periodic target function, its infinite Fourier series, the
finite numerical approximation, and the package evaluator.

## Periodic target

Define the $2\pi$-periodic odd square wave by

$$
f(x)=
\begin{cases}
-1, & -\pi < x < 0,\\
+1, & 0 < x < \pi.
\end{cases}
$$

Values at integer multiples of $\pi$ do not affect its Fourier coefficients. At
a jump, the Fourier series converges to the midpoint of the one-sided limits,
which is zero for this convention.

## Odd-harmonic representation

Because $f$ is odd, its cosine coefficients and constant coefficient vanish. Its
sine coefficients are

$$
b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin(nx)\,dx
=
\begin{cases}
\dfrac{4}{\pi n}, & n \text{ odd},\\
0, & n \text{ even}.
\end{cases}
$$

The infinite represented series is therefore

$$
f(x) \sim \frac{4}{\pi}
\sum_{j=0}^{\infty}\frac{\sin((2j+1)x)}{2j+1}.
$$

A numerical calculation retains only $M$ odd harmonics:

$$
S_M(x)=\frac{4}{\pi}
\sum_{j=0}^{M-1}\frac{\sin((2j+1)x)}{2j+1}.
$$

`OddSquareWaveFourierSeriesEvaluator` evaluates $S_M$ for a caller-supplied
NumPy array of finite, dimensionless angles in radians. The evaluator does not
represent the discontinuous target itself and does not choose a plotting grid or
an error metric.

## Interpretation and limitations

Expected behavior is convergence to the square wave at continuity points and to
the midpoint value at jumps. Finite truncations exhibit oscillatory overshoot
near a jump; increasing $M$ narrows the affected region but does not produce
uniform convergence across the discontinuity.

The notebook provides an illustrative numerical example and executable symmetry
checks. It is not a scientific-validation or pedagogical-validation study.

## Exercises

1. Derive $b_n$ directly by splitting the integral at $x=0$.
2. Show from the finite formula that $S_M(-x)=-S_M(x)$.
3. Compare pointwise error away from the jumps for several values of $M$.
4. Explain why values assigned to $f$ at isolated jump points do not change the
   coefficients.
