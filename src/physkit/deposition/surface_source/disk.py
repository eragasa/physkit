from __future__ import annotations
from dataclasses import dataclass
import numpy as np

from .types import DiskSourceParams
from .quadrature import DiskPolarGrid
from .kernels import r2_disk_to_substrate, r_pow_minus

Array = np.ndarray


@dataclass(frozen=True)
class SurfaceSourceDiskDeposition:
    """
    Finite surface source: emitting disk (radius a) in plane z=-h, centered on axis.
    Substrate plane: z=0, normal +z.
    Emission law: intensity ∝ cos^n(phi) about the +z source normal.
    """
    params: DiskSourceParams

    def J_shape(self, ell: Array, grid: DiskPolarGrid | None = None) -> Array:
        """
        Returns J_s(ell) up to a multiplicative constant.
        """
        ell = np.asarray(ell, dtype=float)

        p = self.params
        if grid is None:
            grid = DiskPolarGrid(a=p.a)

        rho, psi = grid.nodes()
        drho, dpsi = grid.weights()

        # r^(-(n+3))
        r2 = r2_disk_to_substrate(ell=ell, rho=rho, psi=psi, h=p.h)
        rpow = r_pow_minus(r2, p.n + 3.0)

        # dA = rho d rho d psi
        integrand = (p.h ** (p.n + 1.0)) * rpow * rho[None, :, None]

        # integrate over psi then rho
        J_psi = np.sum(integrand, axis=2) * dpsi     # (Ne, Nr)
        J = np.sum(J_psi, axis=1) * drho             # (Ne,)
        return J

    def thickness_ratio(self, ell_over_h: Array, grid: DiskPolarGrid | None = None) -> Array:
        """
        Normalized thickness profile d/d0 vs x = ell/h.
        """
        x = np.asarray(ell_over_h, dtype=float)
        ell = x * self.params.h
        J = self.J_shape(ell, grid=grid)
        return J / J[0]

