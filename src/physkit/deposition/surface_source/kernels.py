from __future__ import annotations
import numpy as np

Array = np.ndarray


def r2_disk_to_substrate(ell: Array, rho: Array, psi: Array, h: float) -> Array:
    """
    Squared distance between:
      substrate point at (ell, 0, 0)
      source disk point at (rho cos psi, rho sin psi, -h)

    Broadcasting convention:
      ell: (Ne,)
      rho: (Nr,)
      psi: (Npsi,)
    Output:
      r2: (Ne, Nr, Npsi)
    """
    ell = ell[:, None, None]
    rho = rho[None, :, None]
    psi = psi[None, None, :]
    return ell**2 + rho**2 - 2.0 * ell * rho * np.cos(psi) + h**2


def r_pow_minus(r2: Array, p: float) -> Array:
    """
    Return r^(-p) from r2.
    """
    r = np.sqrt(r2)
    return r ** (-p)

