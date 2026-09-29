# Two-dimensional rectangular particle-in-a-box spectrum

## Physical model

A particle of mass $m$ is confined to the rectangle

$$
0\le x\le L_x,
\qquad
0\le y\le L_y,
$$

with homogeneous Dirichlet boundary conditions on all four edges. In the
interior, the time-independent Schrödinger equation is

$$
-\frac{\hbar^2}{2m}
\left(
\frac{\partial^2\psi}{\partial x^2}
+
\frac{\partial^2\psi}{\partial y^2}
\right)
=E\psi.
$$

This is a continuum boundary-value problem on a rectangle. It is distinct from
a periodic free-particle problem on a Bravais cell.

## Separation of variables

Write the stationary state as

$$
\psi(x,y)=X(x)Y(y).
$$

Each factor satisfies a one-dimensional homogeneous-Dirichlet box problem. The
positive integer quantum numbers are

$$
n_x=1,2,3,\ldots,
\qquad
n_y=1,2,3,\ldots.
$$

The normalized product eigenfunctions are

$$
\psi_{n_x,n_y}(x,y)
=
\frac{2}{\sqrt{L_xL_y}}
\sin\left(\frac{n_x\pi x}{L_x}\right)
\sin\left(\frac{n_y\pi y}{L_y}\right),
$$

and the energies are

$$
E_{n_x,n_y}
=
\frac{\hbar^2\pi^2}{2m}
\left(
\frac{n_x^2}{L_x^2}
+
\frac{n_y^2}{L_y^2}
\right).
$$

## State inventory and ordering

`Piab2DAnalyticalEvaluator` evaluates a finite rectangular inventory containing
all pairs

$$
1\le n_x\le n_{x,\max},
\qquad
1\le n_y\le n_{y,\max}.
$$

`Piab2DAnalyticalSolution` orders the pairs by nondecreasing energy and uses
lexicographic pair order to resolve exact energy ties. The ordering is a software
contract for a finite requested inventory, not an additional physical quantum
number.

## Degeneracy

For a square box, $L_x=L_y=L$, the energy depends on
$n_x^2+n_y^2$. Exchanging the axes therefore gives

$$
E_{n_x,n_y}=E_{n_y,n_x}.
$$

When $n_x\ne n_y$, these are distinct product states with the same energy. A
rectangular box with unequal side lengths generally breaks this exchange
degeneracy. Additional degeneracies can occur when different integer pairs
produce the same weighted sum.

## Units and scaling

The model uses a selected coherent numerical `UnitSystem`. Doubling both side
lengths while holding mass fixed divides every energy by four. Increasing the
mass divides every energy by the same factor.

The
[computational laboratory](../../../../../../notebooks/qm/piab2d/tise/analytical/piab2d.ipynb)
uses a nondimensional example and checks the represented formula and square-box
degeneracies.

## Exercises

1. Verify normalization of the product eigenfunctions.
2. Derive the exchange degeneracy for a square box.
3. Find distinct positive integer pairs with equal $n_x^2+n_y^2$ that are not
   related only by exchanging coordinates.
4. Show the inverse-square scaling under a uniform change of both side lengths.
