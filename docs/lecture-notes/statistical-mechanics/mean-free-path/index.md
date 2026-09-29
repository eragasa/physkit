# Mean free path in an ideal hard-sphere gas

For identical hard-sphere particles with collision diameter $d$, the collision
cross section is

$$
\sigma=\pi d^2.
$$

For an ideal gas at pressure $P$ and absolute temperature $T$, the number
density is

$$
n=\frac{P}{k_B T}.
$$

Accounting for the relative motion of identical particles gives the mean free
path

$$
\lambda=\frac{1}{\sqrt{2}\,n\sigma}
=\frac{k_B T}{\sqrt{2}\,\pi d^2P}.
$$

`HardSphereIdealGasState` retains explicit physical units for $P$, $T$, and
$d$, converts compatible units through the package unit system, and returns
unit-bearing values for $\sigma$, $n$, and $\lambda$.

The [computational laboratory](../../../../notebooks/thermal/statmech/kinetic/mfp.ipynb)
verifies inverse-pressure scaling and plots $\lambda(P)$ on logarithmic axes.
This is numerical verification of the represented idealized model, not
scientific validation for a real gas over the plotted range.
