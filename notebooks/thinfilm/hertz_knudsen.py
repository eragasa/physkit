# physkit/materials/transport/hertz_knudsen.py
# Eugene Joseph M. Ragasa

from __future__ import annotations
from dataclasses import dataclass
from typing import Union
import numpy as np

from physkit.constants import ConstantsSI
from physkit.units import Temperature
from vapor_pressure import VaporPressureCurve
ArrayLike = Union[float, np.ndarray]

k_B = ConstantsSI.k_B


@dataclass(frozen=True)
class HertzKnudsenLangmuir:
    r"""
    Hertz-Knudsen-Langmuir interfacial flux model.

    Number flux:
    $$
    \Phi(T) = \alpha \frac{\max(P_\mathrm{eq}(T)-P_\mathrm{bg},\,0)}
                         {\sqrt{2\pi m k_B T}}
    $$

    Mass flux:
    $$
    \Gamma(T) = m\,\Phi(T)
    $$
    """

    vapor_pressure: VaporPressureCurve
    m_kg: float
    alpha: float = 1.0
    P_bg_Pa: float = 0.0

    def _validate(self) -> None:
        if self.alpha < 0.0:
            raise ValueError("alpha must be >= 0.")
        if self.m_kg <= 0.0:
            raise ValueError("m_kg must be > 0.")
        if self.P_bg_Pa < 0.0:
            raise ValueError("P_bg_Pa must be >= 0.")

    def _T_to_K(self, T: ArrayLike) -> np.ndarray:
        T_arr = np.asarray(T, dtype=float)
        # Interpret T in the same input unit as the vapor-pressure model expects.
        T_K = Temperature.to_canonical(value=T_arr, unit=self.vapor_pressure.T_unit)
        T_K = np.asarray(T_K, dtype=float)
        if np.any(T_K <= 0.0):
            raise ValueError("T must be > 0 K.")
        return T_K

    def Phi(self, T: ArrayLike, check_range: bool = True) -> ArrayLike:
        """
        Number flux in 1/(m^2 s).
        """
        self._validate()

        # P_eq uses vapor_pressure's own T convention.
        P_eq = np.asarray(self.vapor_pressure.P_Pa(T, check_range=check_range), dtype=float)
        P_net = np.maximum(P_eq - self.P_bg_Pa, 0.0)

        # Thermal denominator needs Kelvin.
        T_K = self._T_to_K(T)
        denom = np.sqrt(2.0 * np.pi * self.m_kg * k_B * T_K)
        out = self.alpha * P_net / denom

        # preserve scalar if scalar input
        if np.ndim(out) == 0:
            return float(out)
        return out

    def Gamma(self, 
              T: ArrayLike, 
              check_range: bool = True) -> ArrayLike:
        """
        Mass flux in kg/(m^2 s).
        """
        out = self.m_kg * np.asarray(self.Phi(T, check_range=check_range), dtype=float)
        if np.ndim(out) == 0:
            return float(out)
        return out

    def __call__(self, T: ArrayLike, check_range: bool = True) -> ArrayLike:
        """
        Default: mass flux.
        """
        return self.Gamma(T, check_range=check_range)
