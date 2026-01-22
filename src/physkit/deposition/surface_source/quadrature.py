from __future__ import annotations
from dataclasses import dataclass
import numpy as np

Array = np.ndarray


@dataclass(frozen=True)
class DiskPolarGrid:
    """
    Simple uniform polar grid over disk:
      rho in [0, a], psi in [0, 2pi)
    """
    a: float
    Nr: int = 250
    Npsi: int = 360

    def nodes(self) -> tuple[Array, Array]:
        rho = np.linspace(0.0, self.a, self.Nr)
        psi = np.linspace(0.0, 2.0 * np.pi, self.Npsi, endpoint=False)
        return rho, psi

    def weights(self) -> tuple[float, float]:
        dpsi = 2.0 * np.pi / self.Npsi
        drho = self.a / (self.Nr - 1) if self.Nr > 1 else 0.0
        return drho, dpsi

