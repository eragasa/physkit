# Mathematics

For a homogeneous-Dirichlet rectangle with lengths $L_x$ and $L_y$, the
normalized stationary eigenfunction is

$$
\psi_{n_x,n_y}(x,y)=
\sqrt{\frac{4}{L_xL_y}}
\sin\left(\frac{n_x\pi x}{L_x}\right)
\sin\left(\frac{n_y\pi y}{L_y}\right),
$$

where $n_x,n_y\in\{1,2,\ldots\}$. It satisfies

$$
\int_0^{L_x}\int_0^{L_y}|\psi_{n_x,n_y}(x,y)|^2\,dy\,dx=1.
$$

The represented matrix places $x$ samples along rows and $y$ samples along
columns. Physical eigenfunction amplitudes have inverse-length units in two
dimensions, while nondimensional models use `Unitless`.

## Navigation

- [Implementation](../index.md)
