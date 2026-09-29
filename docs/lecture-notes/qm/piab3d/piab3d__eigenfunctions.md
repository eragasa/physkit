# Analytical PIAB3D eigenfunction plane slices

Normalized stationary states of the rectangular homogeneous-Dirichlet cuboid
are

$$
\psi_{n_x,n_y,n_z}(x,y,z)=
\sqrt{\frac{8}{L_xL_yL_z}}
\sin\left(\frac{n_x\pi x}{L_x}\right)
\sin\left(\frac{n_y\pi y}{L_y}\right)
\sin\left(\frac{n_z\pi z}{L_z}\right).
$$

## Cartesian plane slices

A Cartesian plane slice holds one coordinate fixed and samples the other two.
The plane normal identifies the fixed axis:

- normal `X`: fix $x=x_0$ and sample $(y,z)$;
- normal `Y`: fix $y=y_0$ and sample $(x,z)$; and
- normal `Z`: fix $z=z_0$ and sample $(x,y)$.

For a fixed coordinate $q=q_0$ along normal direction $q$, with length $L_q$
and quantum number $n_q$, the integrated plane density is

$$
\int_{\mathrm{plane}} |\psi|^2\,dA
=
\frac{2}{L_q}
\sin^2\left(\frac{n_q\pi q_0}{L_q}\right).
$$

This quantity is a probability density with respect to the fixed coordinate, so
it generally is not one. Integrating these plane weights along the normal
coordinate restores full three-dimensional normalization.

## Nodal interpretation

The two in-plane quantum numbers determine visible nodal lines. The normal
quantum number controls the amplitude of the complete plane. If the fixed
coordinate is a node of the normal sine factor, the entire slice vanishes even
though the three-dimensional state is nonzero away from that plane.

A planar heatmap is a physical-coordinate slice, not an independently normalized
two-dimensional state and not a quantum-number inventory plot.

The [computational laboratory](../../../../notebooks/qm/piab3d/piab3d__eigenfunctions.ipynb)
uses a `Z`-normal midplane for four states and then compares `X`-, `Y`-, and
`Z`-normal slices through one state with the same evaluator.

## Exercises

1. Reproduce the plots on `X`- and `Y`-normal planes.
2. Identify all nodal planes of a selected state.
3. Compare slices of permutation-related cubic states.
4. Explain how a sequence of parallel plane slices reconstructs the full
   probability density.
