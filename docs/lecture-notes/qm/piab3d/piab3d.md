# Three-dimensional rectangular particle-in-a-box spectrum

## Physical model

A particle of mass $m$ occupies the rectangular cuboid

$$
0<x<L_x,\qquad 0<y<L_y,\qquad 0<z<L_z,
$$

with homogeneous Dirichlet conditions on all six faces. Inside the cuboid the
potential is zero. The stationary Hamiltonian is

$$
\hat H=-\frac{\hbar^2}{2m}
\left(
\frac{\partial^2}{\partial x^2}
+\frac{\partial^2}{\partial y^2}
+\frac{\partial^2}{\partial z^2}
\right).
$$

## Separable stationary states

Separation of variables gives positive integer quantum numbers
$(n_x,n_y,n_z)$ and normalized product eigenfunctions

$$
\psi_{n_x,n_y,n_z}(x,y,z)=
\sqrt{\frac{8}{L_xL_yL_z}}
\sin\left(\frac{n_x\pi x}{L_x}\right)
\sin\left(\frac{n_y\pi y}{L_y}\right)
\sin\left(\frac{n_z\pi z}{L_z}\right).
$$

The corresponding energies are

$$
E_{n_x,n_y,n_z}
=
\frac{\hbar^2\pi^2}{2m}
\left(
\frac{n_x^2}{L_x^2}
+
\frac{n_y^2}{L_y^2}
+
\frac{n_z^2}{L_z^2}
\right).
$$

For a finite computational inventory, each quantum number receives an explicit
positive upper bound. Ordering by nondecreasing energy and then lexicographically
for exact ties gives deterministic state identities.

## Cubic permutation degeneracy

For a cube, $L_x=L_y=L_z=L$, so energy depends on

$$
n_x^2+n_y^2+n_z^2.
$$

Every distinct permutation of a triple has equal energy. For example,
$(1,1,2)$, $(1,2,1)$, and $(2,1,1)$ form a threefold permutation multiplet.
Triples with all entries distinct can produce sixfold permutation multiplets.
Additional arithmetic coincidences can produce larger energy multiplicities.

An orthorhombic box with unequal side lengths generally splits these
permutation-related states because the three squared quantum numbers acquire
different length factors.

## Scaling and interpretation

Uniformly scaling all side lengths by $s$ scales every energy by $s^{-2}$.
Changing one side length affects only the corresponding term. The analytical
spectrum is a continuum homogeneous-Dirichlet result; it is not a periodic
reciprocal-space spectrum or a finite-difference approximation.

The [computational laboratory](../../../../notebooks/qm/piab3d/piab3d.ipynb)
evaluates a finite cubic inventory, identifies permutation degeneracies, and
shows their splitting in an orthorhombic box.

## Exercises

1. Derive the normalization coefficient of the product eigenfunction.
2. List the permutation multiplicity of triples with one, two, and three
   distinct entries.
3. Verify inverse-square scaling under uniform changes of box size.
4. Distinguish permutation degeneracy from unrelated equal sums of three
   squares.
