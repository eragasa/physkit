# Exponential Boltzmann energy distribution

Let $\theta=k_B T>0$ be a thermal-energy scale. Under a constant density-of-states
assumption, the normalized continuous density on $E\geq0$ is

$$
f(E)=\frac{1}{\theta}\exp\!\left(-\frac{E}{\theta}\right).
$$

Its normalization follows from

$$
\int_0^\infty f(E)\,dE=1,
$$

and the probability represented on a finite interval $[0,E_{\max}]$ is

$$
1-\exp\!\left(-\frac{E_{\max}}{\theta}\right).
$$

The maintained implementation uses explicit physical energy quantities and
returns density in reciprocal input-energy units. The [computational
laboratory](../../../../notebooks/thermal/statmech/distributions/boltzmann-exponential-energy-distribution.ipynb)
checks the finite-interval probability and plots three thermal-energy scales.

This constant-density-of-states model must not be confused with the
three-dimensional translational kinetic-energy distribution, which contains a
$\sqrt{E}$ density-of-states factor. The plotted examples are illustrative and
do not establish material-specific scientific validation.
