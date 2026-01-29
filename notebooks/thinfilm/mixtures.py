# physkit/materials/thermo/activity.py

from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, runtime_checkable, Dict
import numpy as np

from physkit.units import Pressure, Temperature
from physkit.constants import ConstantsSI  # expect k_B, N_A, etc.
from vapor_pressure import VaporPressureCurve

ArrayLike = float | np.ndarray


@runtime_checkable
class ActivityModel(Protocol):
    """
    a_i(T_K, x) or gamma_i(T_K, x) for condensed phase.
    Convention: x is mole-fraction dict keyed by species string.
    """
    def gamma(self, T_K: ArrayLike, x: Dict[str, float]) -> Dict[str, ArrayLike]:
        ...

@dataclass(frozen=True)
class IdealSolution(ActivityModel):
    species: tuple[str, ...]
    def gamma(self, 
        T_K: ArrayLike, 
        x: Dict[str, float]
    ) -> Dict[str, ArrayLike]:
        return {sp: 1.0 for sp in self.species}


@dataclass(frozen=True)
class RegularSolutionBinary(ActivityModel):
    """
    Symmetric regular solution with interaction parameter Omega (J/mol).
    species = (A, B)
    """
    species: tuple[str, str]
    Omega_J_per_mol: float

    def gamma(self, T_K: ArrayLike, x: Dict[str, float]) -> Dict[str, ArrayLike]:
        A, B = self.species
        xA = float(x[A]); xB = float(x[B])
        if xA < 0 or xB < 0 or abs((xA + xB) - 1.0) > 1e-6:
            raise ValueError("Binary x must be nonnegative and sum to 1.")

        R = ConstantsSI.R_g  # J/(mol K)
        T = np.asarray(T_K, dtype=float)

        ln_gA = self.Omega_J_per_mol * (xB**2) / (R * T)
        ln_gB = self.Omega_J_per_mol * (xA**2) / (R * T)
        return {A: np.exp(ln_gA), B: np.exp(ln_gB)}


@dataclass(frozen=True)
class PartialPressureFromActivity:
    """
    P_i(T,x) = (gamma_i x_i) P_i*(T).
    """
    pure_vp: Dict[str, VaporPressureCurve]   # species -> pure VP curve
    activity: ActivityModel

    def P_i_Pa(self, 
        T: ArrayLike, 
        x: Dict[str, float], 
        check_range: bool = True
    ) -> Dict[str, ArrayLike]:
        T_arr = np.asarray(T, dtype=float)
        gam = self.activity.gamma(T_arr, x)

        out: Dict[str, ArrayLike] = {}
        for sp, vp in self.pure_vp.items():
            xi = float(x[sp])
            if xi < 0.0:
                raise ValueError("Mole fractions must be >= 0.")
            Pstar = np.asarray(vp.P_Pa(T_arr, check_range=check_range), dtype=float)
            out[sp] = (xi * np.asarray(gam[sp], dtype=float)) * Pstar
        return out

    def P_total_Pa(self, T: ArrayLike, x: Dict[str, float], check_range: bool = True) -> ArrayLike:
        Pi = self.P_i_Pa(T, x, check_range=check_range)
        total = None
        for v in Pi.values():
            total = v if total is None else (total + v)
        return total
