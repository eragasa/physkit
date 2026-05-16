# physkit.thermo.vaporpressure.base.py
# Eugene Joseph M. Ragasa 2026

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np

from physkit.types import ArrayLike
from physkit.numeric import as_f64_array
from physkit.units import Temperature, Pressure


@dataclass
class VaporPressureBase:
    """
    Base class for saturation vapor-pressure correlations.

    Subclasses implement exactly one canonical evaluator:
        _ln_pressure_Pa_from_K(T_K: ndarray) -> ndarray
    returning ln(P/Pa) for input temperature in Kelvin.

    This base class provides:
    - scalar/array normalization (float64)
    - validity-range checks (optional)
    - unit conversions for input/output

    Public API
    ----------
    - ln_pressure_Pa(T_K): canonical, numerically stable
    - pressure_Pa(T_K): exp(ln_pressure_Pa)
    - pressure(T, T_unit, P_unit): unit-flexible convenience
    """

    # Metadata about the source parameterization
    param_P_unit: Pressure.Units = Pressure.Units.Pa
    param_T_unit: Temperature.Units = Temperature.Units.K
    param_T_valid_range: Optional[Tuple[float, float]] = None

    # Provenance string
    source: str = ""

    # ----------------------------
    # required subclass hooks
    # ----------------------------
    def _ln_pressure_Pa_from_K(self, T_K: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    # ----------------------------
    # Canonical API
    # ----------------------------
    def ln_pressure_Pa(self, T_K: ArrayLike) -> ArrayLike:
        """
        Canonical evaluation: ln(P/Pa) for temperature in Kelvin.

        Arguments:
        T_K: ArrayLike
          Temperature in Kelvin
        """

        # coerce to np.ndarray, dtype=64
        T_arr = as_f64_array(T_K)

        if np.any(T_arr <= 0.0):
            raise ValueError("Temperature must be > 0 K.")

        # calls subclass hook
        lnP = self._ln_pressure_Pa_from_K(T_arr)

        return as_f64_array(lnP)


    def pressure_Pa(self, T_K: ArrayLike) -> ArrayLike:
        """
        Canonical physical pressure: P in Pa for temperature in Kelvin.
        """
        lnP = self.ln_pressure_Pa(T_K)
        return np.exp(lnP)

    # ----------------------------
    # Unit-flexible API (user-facing)
    # ----------------------------
    def pressure(
        self,
        T: ArrayLike,
        T_units: Temperature.Units = Temperature.Units.K,
        P_units: Pressure.Units = Pressure.Units.Pa,
        check_valid_range: bool = True,
    ) -> ArrayLike:
        """
        Return saturation vapor pressure in requested units.

        Parameters
        ----------
        T : float or ndarray
            Temperature values in `T_unit`.
        T_unit : Temperature.Units
            Unit for the input temperature.
        P_unit : Pressure.Units
            Desired output pressure unit.
        check_valid_range : bool
            If True and T_valid_range is set, validate T against the parameter
            validity range (interpreted in param_T_unit).

        Returns
        -------
        float or ndarray
            Saturation vapor pressure in `P_unit`.
        """

        # Optional validity check: interpret metadata in param_T_unit
        if check_valid_range and (self.T_valid_range is not None):
            T_param = Temperature.convert(
                from_=(T, T_units), 
                to=self.param_T_unit,
            )
            Temperature.check_in_range(
                T=T_param,
                unit=self.param_T_unit,
                valid_range=self.param_T_valid_range,
            )

        # Convert to Kelvin
        T_K = Temperature.convert(
            from_=(T, T_units), 
            to=Temperature.Units.K
        )

        # Compute in Pa, then convert to requested output unit
        P_Pa = self.pressure_Pa(T_K)

        return Pressure.convert(
            from_=(P_Pa, Pressure.Units.Pa),
            to=P_units
        )
    