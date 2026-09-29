# Molar and mass composition of finite mixtures

## Scope

A finite mixture contains an identified ordered set of chemical species. This
note relates two representations of the same composition: amount of substance
and mass. It does not provide activities, chemical potentials, phase equilibria,
or material-property data.

## Molar representation

Let $n_i\geq0$ denote the amount of species $i$, with total
$n=\sum_i n_i>0$. Its mole fraction is

$$
x_i=\frac{n_i}{n},\qquad \sum_i x_i=1.
$$

For species molar masses $M_i>0$, the mixture-average molar mass is

$$
\overline M=\sum_i x_iM_i.
$$

## Mass representation

Component masses satisfy

$$
m_i=n_iM_i.
$$

With total mass $m=\sum_i m_i>0$, the mass fractions are

$$
w_i=\frac{m_i}{m},\qquad \sum_iw_i=1.
$$

Substituting $n_i=m_i/M_i$ gives the equivalent mean-molar-mass expression

$$
\overline M=\left(\sum_i\frac{w_i}{M_i}\right)^{-1}.
$$

## Representation and units

Species order is part of the software representation: each amount and molar
mass must refer to the species at the same position. Amounts, masses, and molar
masses retain explicit physical units. Fractions alone are unitless.

A component may have zero amount, but the represented total must be positive.
Molar masses must be positive. Duplicate or empty species names would make the
mapping ambiguous and are rejected.

## Evidence boundary

Round-trip conversion and equality of the two mean-molar-mass formulas verify
the stated algebra and software contract. They do not validate supplied molar
masses or establish mixture thermodynamics. Material values require identified
and verified sources.
