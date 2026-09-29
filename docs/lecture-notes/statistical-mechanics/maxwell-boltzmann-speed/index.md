# Maxwell–Boltzmann speed distribution

## Purpose and assumptions

This note introduces the speed probability density used by the
[Maxwell–Boltzmann computational laboratory](../../../../notebooks/thermal/statmech/kinetic/maxwell-boltzmann-speed-distribution.ipynb).
The model assumes a dilute classical gas in thermal equilibrium, with no
quantum-statistical or interaction correction.

## Speed probability density

For nonnegative speed $v$, absolute temperature $T$, molar mass $M$, and molar
gas constant $R$, the Maxwell–Boltzmann speed density is

$$
f(v;T,M)=\frac{4}{\sqrt{\pi}}
\left(\frac{M}{2RT}\right)^{3/2}v^2
\exp\!\left(-\frac{Mv^2}{2RT}\right),
\qquad v\ge 0.
$$

Its normalization is

$$
\int_0^\infty f(v;T,M)\,dv=1.
$$

When $v$ is in metres per second, $T$ is in kelvin, $M$ is in kilograms per
mole, and $R$ is in joules per mole kelvin, $f$ is numerically expressed in
seconds per metre. Thus $f(v)\,dv$ is dimensionless.

## Characteristic speeds

The most probable, mean, and root-mean-square speeds are

$$
v_{\mathrm{mp}}=\sqrt{\frac{2RT}{M}},
$$

$$
\langle v\rangle=\sqrt{\frac{8RT}{\pi M}},
$$

and

$$
v_{\mathrm{rms}}=\sqrt{\frac{3RT}{M}}.
$$

They satisfy

$$
v_{\mathrm{mp}} < \langle v\rangle < v_{\mathrm{rms}}.
$$

`MaxwellBoltzmannGasState` owns positive unit-aware temperature and molar-mass
parameters and these intrinsic closed-form properties. Its
`evaluate_speed_distribution(...)` façade accepts speed quantities in compatible
physical units and returns $f$ in reciprocal requested-speed units. The internal
ActionObject performs the numerical evaluation and unit conversion.

## Numerical interpretation

A finite speed grid represents only a bounded quadrature approximation to the
normalization integral. Agreement with normalization and characteristic-speed
formulas is numerical verification of the represented model. It does not show
that a particular experimental gas satisfies the model assumptions.

## Exercises

1. Derive $v_{\mathrm{mp}}$ by differentiating $f(v)$.
2. Verify the units of $f(v)$ from the defining equation.
3. Compare the finite-domain normalization error for several upper speed bounds.
4. Predict how every characteristic speed changes when $T$ is doubled at fixed
   $M$.
