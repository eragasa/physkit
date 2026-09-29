# Mathematics

For box lengths $L_x$, $L_y$, and $L_z$, the normalized stationary product
state is

$$
\psi_{n_x,n_y,n_z}(x,y,z)=
\sqrt{\frac{8}{L_xL_yL_z}}
\prod_{q\in\{x,y,z\}}
\sin\left(\frac{n_q\pi q}{L_q}\right).
$$

A plane normal to axis $q$ fixes $q=q_0$ and evaluates the two remaining
coordinates. The integrated density over that plane is

$$
\rho_q(q_0)=
\int_{\mathrm{plane}}|\psi|^2\,dA
=
\frac{2}{L_q}
\sin^2\left(\frac{n_q\pi q_0}{L_q}\right).
$$

Accordingly, $\rho_q$ has inverse-length units for physical models. It is not a
normalized two-dimensional probability and generally is not equal to one.
Integrating $\rho_q(q_0)$ from zero to $L_q$ produces one.

## Axis ordering

The represented matrix uses the first coordinate along rows and the second
coordinate along columns:

| Plane normal | Fixed coordinate | Row coordinate $u$ | Column coordinate $v$ |
|---|---|---|---|
| `X` | $x$ | $y$ | $z$ |
| `Y` | $y$ | $x$ | $z$ |
| `Z` | $z$ | $x$ | $y$ |

## Navigation

- [Implementation](../index.md)
