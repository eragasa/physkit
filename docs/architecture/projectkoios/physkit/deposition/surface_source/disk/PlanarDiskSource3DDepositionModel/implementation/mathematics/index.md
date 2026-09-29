# Mathematics

For radius $a$, separation $h$, lateral offset $\ell$, source radius $\rho$,
azimuth $\psi$, and cosine exponent $n\geq0$, the represented shape is

$$
J_n(\ell)\propto\int_0^a\int_0^{2\pi}
\frac{h^{n+1}\rho\,d\psi\,d\rho}
{(\ell^2+\rho^2-2\ell\rho\cos\psi+h^2)^{(n+3)/2}}.
$$

The output is $J_n(\ell)/J_n(0)$. Radial integration uses the trapezoidal rule;
azimuthal integration uses the periodic uniform rule.
