# Analytical PIAB2D eigenfunctions

For the rectangular homogeneous-Dirichlet box, normalized stationary states are

$$
\psi_{n_x,n_y}(x,y)=
\frac{2}{\sqrt{L_xL_y}}
\sin\left(\frac{n_x\pi x}{L_x}\right)
\sin\left(\frac{n_y\pi y}{L_y}\right),
$$

where $n_x,n_y$ are positive integers. The product normalization gives

$$
\int_0^{L_x}\int_0^{L_y}
|\psi_{n_x,n_y}(x,y)|^2\,dy\,dx=1.
$$

## Boundary and nodal structure

The sine factors make every state vanish on all four box boundaries. Along the
$x$ direction, the state has $n_x-1$ interior nodal lines; along the $y$
direction it has $n_y-1$. Probability density removes the wavefunction sign but
retains these nodes.

For a square box, exchanging $n_x$ and $n_y$ rotates the density pattern and
leaves the energy unchanged. For unequal side lengths the rotated pattern still
exists as a product state, but its energy generally differs.

## Sampled evaluation

A numerical visualization selects explicit coordinate vectors and evaluates the
analytical product on their Cartesian product. The resulting matrix is a sampled
representation, not a finite-difference solution. Numerical integration of its
squared magnitude checks the coordinate sampling and quadrature, while the
underlying analytical state remains exactly normalized.

The [computational laboratory](../../../../../../notebooks/qm/piab2d/tise/analytical/piab2d__eigenfunctions.ipynb)
uses package-owned evaluation to visualize four low-order probability densities
and check boundary values and represented normalization.

## Exercises

1. Derive the normalization coefficient from one-dimensional sine integrals.
2. Relate each quantum number to the number and orientation of interior nodes.
3. Compare $(1,2)$ and $(2,1)$ in square and rectangular boxes.
4. Explain why a sampled analytical state is not a finite-difference eigenstate.
