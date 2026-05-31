import numpy as np

from physkit.core.grids import CartesianGrid1D
from physkit.qm.solver1d import TISESolver1D
from physkit.qm.potentials import Potential1D, ConstantPotential1D

from physkit.core.bc import DirichletBC

class ParticleInABox1D(TISESolver1D):
    def __init__(
            self,
            x_min: float,
            x_max: float,
            Nx: int, *,
            mass: float=1.0,
            hbar: float=1.0
        ):
        grid = CartesianGrid1D(x_min=x_min, x_max=x_max, Nx=Nx)
        potential: Potential1D = ConstantPotential1D(value=0)
        super().__init__(
            grid=grid,
            potential = potential,
            mass= mass,
            hbar = hbar,
            bc_x_min = DirichletBC(value=0),
            bc_x_max = DirichletBC(value=0)
        )
