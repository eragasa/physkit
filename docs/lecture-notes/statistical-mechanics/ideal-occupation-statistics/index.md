# Ideal occupation statistics

## Physical inputs

For single-particle energy $\varepsilon$, chemical potential $\mu$, and absolute
temperature $T>0$, define

$$
x=\frac{\varepsilon-\mu}{k_BT}.
$$

Although $x$ and the resulting occupation factors are dimensionless,
$\varepsilon$, $\mu$, and $T$ are physical quantities. The maintained APIs
therefore accept explicit energy and temperature units and construct $x$
internally.

## Occupation factors

The ideal Fermi--Dirac mean occupation is

$$
f_{\mathrm{FD}}(\varepsilon)=\frac{1}{e^x+1}.
$$

The ideal Bose--Einstein mean occupation is

$$
f_{\mathrm{BE}}(\varepsilon)=\frac{1}{e^x-1},
$$

with the represented excited-state domain $\varepsilon>\mu$. Treatment of a
condensate population is outside this evaluator.

The Maxwell--Boltzmann dilute-limit factor is

$$
f_{\mathrm{MB}}(\varepsilon)=e^{-x}.
$$

Unlike the Fermi--Dirac occupation, the classical factor is not intrinsically
bounded above by one for arbitrary negative $x$.

## Dilute limit

For $x\gg1$, $e^x\gg1$, so

$$
f_{\mathrm{FD}}\approx f_{\mathrm{BE}}\approx f_{\mathrm{MB}}.
$$

Thus high temperature alone does not define the classical limit. The energy
offset relative to both chemical potential and thermal energy is the relevant
quantity.

The [computational laboratory](../../../../notebooks/thermal/statmech/distributions/occupations/ideal-occupation-statistics.ipynb)
evaluates all three formulas on electron-volt coordinates at an explicit
kelvin temperature, verifies dilute-limit convergence, and retains a
semilogarithmic plot. It does not include a density of states, particle-number
constraint, interactions, or material-specific band structure.
