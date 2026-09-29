# Knudsen number

## Definition

The Knudsen number compares the molecular mean free path $\lambda$ with a
characteristic geometric length $L$:

$$
\mathrm{Kn}=\frac{\lambda}{L}.
$$

Because both quantities are lengths, $\mathrm{Kn}$ is dimensionless. The
characteristic length is part of the model definition: changing it changes the
reported Knudsen number even when the gas state is unchanged.

## Composition with hard-sphere kinetic theory

For identical hard spheres with number density $n$ and collision cross section
$\sigma$, the maintained mean-free-path convention is

$$
\lambda=\frac{1}{\sqrt{2}\,n\sigma}.
$$

For an ideal gas, $n=P/(k_BT)$, so at fixed temperature, collision diameter, and
characteristic length,

$$
\mathrm{Kn}\propto P^{-1}.
$$

This scaling is checked computationally rather than embedded as a second
Knudsen-number implementation.

## Regime classification boundary

Named continuum, slip, transitional, and molecular-flow regimes require
threshold conventions and may depend on the application and characteristic
length definition. The maintained ratio model therefore reports $\mathrm{Kn}$
without selecting labels or thresholds. Equality $\mathrm{Kn}=1$ means only that
the represented mean free path and characteristic length are equal.

The [computational laboratory](../../../../notebooks/thermal/statmech/transport/knudsen-number.ipynb)
combines the unit-aware hard-sphere mean-free-path state with the ratio model,
checks inverse-pressure scaling, and retains a logarithmic plot. Its parameters
are synthetic illustrative values rather than material-specific validation
data.
