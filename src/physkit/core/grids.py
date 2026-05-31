from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]

class CartesianAxis:
    """
    One-dimensional Cartesian coordinate axis.

    This object stores the coordinate samples, spacing, and length
    for one Cartesian direction.
    """

    def __init__(
        self,
        name: str,
        lower: float,
        upper: float,
        N: int,
        *,
        endpoint: bool = True,
    ) -> None:
        self.name: str = name
        self.lower: float = lower
        self.upper: float = upper
        self.N: int = N
        self.endpoint: bool = endpoint

        self.check_args()

        self.L: float = self.upper - self.lower

        self.values: FloatArray = np.linspace(
            start=self.lower,
            stop=self.upper,
            num=self.N,
            endpoint=self.endpoint,
            dtype=np.float64,
        )
        self.values.setflags(write=False)

        self.d: float = self.values[1] - self.values[0]

    def check_args(self) -> None:
        if not isinstance(self.name, str):
            raise TypeError("name must be a string.")

        if not np.isfinite(self.lower):
            raise ValueError(f"{self.name}_min must be finite.")

        if not np.isfinite(self.upper):
            raise ValueError(f"{self.name}_max must be finite.")

        if self.upper <= self.lower:
            raise ValueError(
                f"{self.name}_max must be greater than {self.name}_min."
            )

        if not isinstance(self.N, int):
            raise TypeError(f"N{self.name} must be an integer.")

        if self.N < 2:
            raise ValueError(f"N{self.name} must be at least 2.")

        if not isinstance(self.endpoint, bool):
            raise TypeError(f"endpoint_{self.name} must be a bool.")

    def __repr__(self) -> str:
        return (
            f"CartesianAxis("
            f"name='{self.name}', "
            f"lower={self.lower}, "
            f"upper={self.upper}, "
            f"N={self.N}, "
            f"endpoint={self.endpoint})"
        )


class CartesianGrid1D:
    """
    One-dimensional Cartesian grid.

    A grid defines the discrete state space for functions of x.

    Parameters
    ----------
    x_min:
        Left boundary of the domain.
    x_max:
        Right boundary of the domain.
    Nx:
        Number of grid points.
    endpoint:
        If True, include x_max as a grid point.
        If False, exclude x_max. This is useful for periodic grids.
    """

    def __init__(
        self,
        x_min: float,
        x_max: float,
        Nx: int,
        *,
        endpoint: bool = True,
    ) -> None:
        self.x_axis = CartesianAxis(
            name="x",
            lower=x_min,
            upper=x_max,
            N=Nx,
            endpoint=endpoint,
        )

        self.x_min: float = self.x_axis.lower
        self.x_max: float = self.x_axis.upper
        self.Nx: int = self.x_axis.N
        self.endpoint: bool = self.x_axis.endpoint

        self.x: FloatArray = self.x_axis.values

        self.Lx: float = self.x_axis.L
        self.dx: float = self.x_axis.d

        self.shape: tuple[int] = (self.Nx,)
        self.size: int = self.Nx

    def __repr__(self) -> str:
        return (
            f"CartesianGrid1D("
            f"x_min={self.x_min}, "
            f"x_max={self.x_max}, "
            f"Nx={self.Nx}, "
            f"endpoint={self.endpoint})"
        )


class CartesianGrid2D:
    """
    Two-dimensional Cartesian grid.

    A grid defines the discrete state space for functions of x and y.

    A scalar field on this grid has shape

        (Nx, Ny)

    A flattened state vector has size

        Nx * Ny
    """

    def __init__(
        self,
        x_min: float,
        x_max: float,
        Nx: int,
        y_min: float,
        y_max: float,
        Ny: int,
        *,
        endpoint_x: bool = True,
        endpoint_y: bool = True,
    ) -> None:
        self.x_axis = CartesianAxis(
            name="x",
            lower=x_min,
            upper=x_max,
            N=Nx,
            endpoint=endpoint_x,
        )

        self.y_axis = CartesianAxis(
            name="y",
            lower=y_min,
            upper=y_max,
            N=Ny,
            endpoint=endpoint_y,
        )

        self.x_min: float = self.x_axis.lower
        self.x_max: float = self.x_axis.upper
        self.Nx: int = self.x_axis.N
        self.endpoint_x: bool = self.x_axis.endpoint

        self.y_min: float = self.y_axis.lower
        self.y_max: float = self.y_axis.upper
        self.Ny: int = self.y_axis.N
        self.endpoint_y: bool = self.y_axis.endpoint

        self.x: FloatArray = self.x_axis.values
        self.y: FloatArray = self.y_axis.values

        self.Lx: float = self.x_axis.L
        self.Ly: float = self.y_axis.L

        self.dx: float = self.x_axis.d
        self.dy: float = self.y_axis.d

        self.shape: tuple[int, int] = (self.Nx, self.Ny)
        self.size: int = self.Nx * self.Ny

    @property
    def mesh(self) -> tuple[FloatArray, FloatArray]:
        """
        Return coordinate mesh arrays X and Y.

        This allocates arrays of shape (Nx, Ny), so it is generated
        on demand rather than stored.
        """
        return np.meshgrid(
            self.x,
            self.y,
            indexing="ij",
        )

    @property
    def points(self) -> FloatArray:
        """
        Return flattened coordinate pairs.

        Shape:

            (Nx * Ny, 2)

        This allocates a new array.
        """
        X, Y = self.mesh

        return np.column_stack(
            [
                X.ravel(),
                Y.ravel(),
            ]
        )

    def __repr__(self) -> str:
        return (
            f"CartesianGrid2D("
            f"x_min={self.x_min}, "
            f"x_max={self.x_max}, "
            f"Nx={self.Nx}, "
            f"y_min={self.y_min}, "
            f"y_max={self.y_max}, "
            f"Ny={self.Ny}, "
            f"endpoint_x={self.endpoint_x}, "
            f"endpoint_y={self.endpoint_y})"
        )


class CartesianGrid3D:
    """
    Three-dimensional Cartesian grid.

    A grid defines the discrete state space for functions of x, y, and z.

    A scalar field on this grid has shape

        (Nx, Ny, Nz)

    A flattened state vector has size

        Nx * Ny * Nz
    """

    def __init__(
        self,
        x_min: float,
        x_max: float,
        Nx: int,
        y_min: float,
        y_max: float,
        Ny: int,
        z_min: float,
        z_max: float,
        Nz: int,
        *,
        endpoint_x: bool = True,
        endpoint_y: bool = True,
        endpoint_z: bool = True,
    ) -> None:
        self.x_axis = CartesianAxis(
            name="x",
            lower=x_min,
            upper=x_max,
            N=Nx,
            endpoint=endpoint_x,
        )

        self.y_axis = CartesianAxis(
            name="y",
            lower=y_min,
            upper=y_max,
            N=Ny,
            endpoint=endpoint_y,
        )

        self.z_axis = CartesianAxis(
            name="z",
            lower=z_min,
            upper=z_max,
            N=Nz,
            endpoint=endpoint_z,
        )

        self.x_min: float = self.x_axis.lower
        self.x_max: float = self.x_axis.upper
        self.Nx: int = self.x_axis.N
        self.endpoint_x: bool = self.x_axis.endpoint

        self.y_min: float = self.y_axis.lower
        self.y_max: float = self.y_axis.upper
        self.Ny: int = self.y_axis.N
        self.endpoint_y: bool = self.y_axis.endpoint

        self.z_min: float = self.z_axis.lower
        self.z_max: float = self.z_axis.upper
        self.Nz: int = self.z_axis.N
        self.endpoint_z: bool = self.z_axis.endpoint

        self.x: FloatArray = self.x_axis.values
        self.y: FloatArray = self.y_axis.values
        self.z: FloatArray = self.z_axis.values

        self.Lx: float = self.x_axis.L
        self.Ly: float = self.y_axis.L
        self.Lz: float = self.z_axis.L

        self.dx: float = self.x_axis.d
        self.dy: float = self.y_axis.d
        self.dz: float = self.z_axis.d

        self.shape: tuple[int, int, int] = (self.Nx, self.Ny, self.Nz)
        self.size: int = self.Nx * self.Ny * self.Nz

    @property
    def mesh(self) -> tuple[FloatArray, FloatArray, FloatArray]:
        """
        Return coordinate mesh arrays X, Y, and Z.

        This allocates arrays of shape (Nx, Ny, Nz), so it is generated
        on demand rather than stored.
        """
        return np.meshgrid(
            self.x,
            self.y,
            self.z,
            indexing="ij",
        )

    @property
    def points(self) -> FloatArray:
        """
        Return flattened coordinate triples.

        Shape:

            (Nx * Ny * Nz, 3)

        This allocates a new array.
        """
        X, Y, Z = self.mesh

        return np.column_stack(
            [
                X.ravel(),
                Y.ravel(),
                Z.ravel(),
            ]
        )

    def __repr__(self) -> str:
        return (
            f"CartesianGrid3D("
            f"x_min={self.x_min}, "
            f"x_max={self.x_max}, "
            f"Nx={self.Nx}, "
            f"y_min={self.y_min}, "
            f"y_max={self.y_max}, "
            f"Ny={self.Ny}, "
            f"z_min={self.z_min}, "
            f"z_max={self.z_max}, "
            f"Nz={self.Nz}, "
            f"endpoint_x={self.endpoint_x}, "
            f"endpoint_y={self.endpoint_y}, "
            f"endpoint_z={self.endpoint_z})"
        )
