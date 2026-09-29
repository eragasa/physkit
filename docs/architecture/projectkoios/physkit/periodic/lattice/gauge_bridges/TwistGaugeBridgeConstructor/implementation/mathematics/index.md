# `TwistGaugeBridgeConstructor` mathematics

## Model

For site coordinate vector $r$, finite-domain extents $N$, and unreduced
twist lift $\phi$ measured in turns, the diagonal bridge entry is

<a id="eq-twist-gauge-bridge"></a>
$$
\begin{equation}
U_{rr} = \exp\!\left(2\pi i\sum_a \frac{r_a\phi_a}{N_a}\right)
\tag{EQ-TWIST-GAUGE-BRIDGE}
\end{equation}
$$

The supported direction convention is

<a id="eq-twist-gauge-direction"></a>
$$
\begin{equation}
H_{\mathrm{seam}} = U H_{\mathrm{uniform}} U^\dagger
\tag{EQ-TWIST-GAUGE-DIRECTION}
\end{equation}
$$

| Symbol | Meaning | Unit | Domain |
| --- | --- | --- | --- |
| $r_a$ | Integer coordinate along axis $a$ | dimensionless | $0,\ldots,N_a-1$ |
| $N_a$ | Finite-domain extent along axis $a$ | dimensionless | positive integer |
| $\phi_a$ | Unreduced boundary-twist lift | turns | finite real number |
| $U$ | Site-diagonal gauge transformation | dimensionless | complex unitary matrix |
| $H_{\mathrm{uniform}}$ | Uniform-link represented operator | operator unit | compatible finite site basis |
| $H_{\mathrm{seam}}$ | Quotient-seam represented operator | operator unit | same compatible finite site basis |

## Assumptions and validity

The construction supports only one-, two-, and three-dimensional finite periodic
integer domains. Source and target matrices must already identify the same basis,
unit, energy reference, finite domain, and correlated twist reduction before the
transformation is used for comparison. The equations do not independently
establish physical alignment or gauge invariance for an arbitrary model.

## Evidence

- **Implementation conformance — supported:** the mapped constructor implements
  both equations directly.
- **Numerical verification — supported:** a three-site quarter-twist case is
  compared with hand-derived diagonal phases and seam matrix using maximum
  elementwise absolute difference and tolerance `1e-15` under NumPy/SciPy on
  CPython 3.14.
- **Scientific validation — not evaluated:** no independent physical dataset or
  declared-use validation protocol is part of this test.
- **Human acceptance — not evaluated:** no human scientific-acceptance decision
  is represented by the calculation.

## Navigation

- [Implementation](../index.md)
- [Class contract](../../index.md)
- [Reference notes](../references/index.md)
- [Testing detail](../testing/index.md)
