# physkit/materials/thermo/vapor_pressure.py
# Eugene Joseph M. Ragasa

from __future__ import annotations
from dataclasses import dataclass, field
from typing import (
    Union, 
    Protocol, 
    runtime_checkable, 
    Optional, 
    Tuple
)
import numpy as np
ArrayLike = Union[float, np.ndarray]

from physkit.units import Pressure
from physkit.units import Temperature

@runtime_checkable
class VaporPressureCurve(Protocol):
    """
    Interface for equilibrium vapor-pressure models.

    Implementations provide a canonical method `P_Pa(T)` returning the
    equilibrium vapor pressure in Pascals. Optional metadata may describe
    units, validity range, and data provenance.

    Attributes
    ----------
    P_unit : Pressure.Units
        Native pressure unit associated with the correlation parameters.
        Informational only; `P_Pa` always returns Pascals.
    T_unit : Temperature.Units
        Temperature unit expected by the implementation. Conventions are
        implementation-defined.
    valid_range_K : tuple[float, float] or None
        Valid temperature range in Kelvin for which the correlation is valid.
    source : str
        Human-readable citation or provenance string.
    """
    P_unit: Pressure.Units
    T_unit: Temperature.Units
    valid_range_K: Optional[Tuple[float, float]]
    source: str

    def P_Pa(self, 
             T: ArrayLike, 
             check_range: bool = True
    ) -> ArrayLike:
        """
        Return equilibrium vapor pressure in Pascals.

        Parameters
        ----------
        T : ArrayLike
            Temperature(s) in the units expected by the implementation.
        check_range : bool, default=True
            If True and a validity range is defined, raise an error when
            temperatures are outside the stated range.

        Returns
        -------
        ArrayLike
            Equilibrium vapor pressure in Pascals.
        """
        ...

@dataclass(frozen=True)
class VaporPressureCurveBase:
    """
    Base class for equilibrium vapor-pressure correlations.

    This class defines the authoritative evaluation pathway for vapor-pressure
    models with explicit unit handling and validation. Subclasses implement the
    physics of the correlation in Kelvin space via `_P_Pa_from_K(...)`, while this
    base class handles:

    - temperature unit conversion to Kelvin
    - validity-range checking
    - canonicalization of output to Pascals
    - optional conversion to other pressure units

    Subclasses MUST implement:

        _P_Pa_from_K(T_K, check_range=True) -> ArrayLike

    which computes the equilibrium vapor pressure in Pascals from temperatures
    expressed in Kelvin.

    Attributes
    ----------
    P_unit : Pressure.Units
        Native pressure unit associated with the correlation parameters.
        This is metadata only; all public evaluation returns Pascals or
        user-requested units via conversion.
    T_unit : Temperature.Units
        Unit expected for temperature inputs provided to `P(...)` and `P_Pa(...)`.
        Inputs are converted to Kelvin internally before evaluation.
    valid_range_K : tuple[float, float] or None
        Valid temperature range (T_min, T_max) in Kelvin for the correlation.
        If provided and `check_range=True`, inputs outside this range raise
        ValueError.
    source : str
        Human-readable citation or provenance string for the correlation.

    Notes
    -----
    - This class enforces Kelvin-space evaluation and range checking centrally.
    - Subclasses should NOT re-check temperature ranges.
    - Pressure-unit conversion is handled via `physkit.units.Pressure`.
    - The public API is `P_Pa(...)` (canonical) and `P(...)` (converted output).
    """

    P_unit: Pressure.Units
    T_unit: Temperature.Units

      # kw-only metadata (safe to have defaults)
    valid_range_K: Optional[Tuple[float, float]] \
      = field(default=None, kw_only=True)
    source: str \
      = field(default="unknown", kw_only=True)

    def _temperature_to_kelvin(self, 
        T: ArrayLike
        ) -> np.ndarray:
        """
        Convert input temperature(s) from `self.T_unit` to Kelvin.

        Returns
        -------
        np.ndarray
            Temperatures in Kelvin.
        """
        T_arr = np.asarray(T, dtype=float)
        T_K = Temperature.to_canonical(
            value=T_arr,
            unit=self.T_unit
        )
        return np.asarray(T_K, dtype=float)

    def _check_temperature_K(self, 
        T_K: np.ndarray, 
        check_range: bool) -> None:
        """
        Validate temperatures for correlation evaluation.

        Parameters
        ----------
        T_K : np.ndarray
            Temperature values in Kelvin.
        check_range : bool
            If True and `valid_range_K` is provided, enforce the validity range.

        Raises
        ------
        ValueError
            If any temperature is non-positive, or (optionally) outside the
            validity interval.
        """
        if np.any(T_K <= 0.0):
            raise ValueError("T must be > 0 K.")
        if check_range and self.valid_range_K is not None:
            Tmin, Tmax = self.valid_range_K
            if np.any(T_K < Tmin) or np.any(T_K > Tmax):
                raise ValueError(f"T outside validity range [{Tmin}, {Tmax}] K.")
  
    def _P_Pa_from_K(self, 
        T_K: np.ndarray, 
        check_range: bool = True
    ) -> ArrayLike:
        """
        Compute equilibrium vapor pressure in Pa from Kelvin temperatures.

        Subclasses MUST implement this method.

        Parameters
        ----------
        T_K : np.ndarray
            Temperature(s) in Kelvin.
        check_range : bool, default=True
            Provided for API symmetry; range checking is already enforced in
            `P_Pa(...)` by the base class.
        """
        raise NotImplementedError("Subclasses must implement _P_Pa_from_K(T_K, ...)")

    # -----------------------------
    # Public API (authoritative)
    # -----------------------------
    def P_Pa(self, 
        T: ArrayLike, 
        check_range: bool = True
    ) -> ArrayLike:
        """
        Return equilibrium vapor pressure in Pascals.

        Parameters
        ----------
        T : ArrayLike
            Temperature(s) expressed in `self.T_unit`.
        check_range : bool, default=True
            If True and `valid_range_K` is set, enforce the validity range
            after conversion to Kelvin.

        Returns
        -------
        ArrayLike
            Equilibrium vapor pressure in Pascals.
        """
        T_K = self._temperature_to_kelvin(T)
        self._check_temperature_K(T_K, check_range=check_range)
        return self._P_Pa_from_K(T_K, check_range=check_range)

    def P(
        self,
        T: ArrayLike,
        unit: Pressure.Units = Pressure.Units.Pa,
        check_range: bool = True,
        *,
        scalar_out: bool = False,
    ) -> ArrayLike:
        """
        Evaluate vapor pressure and return it in the requested unit.

        Parameters
        ----------
        T : ArrayLike
            Temperature(s) expressed in `self.T_unit`.
        unit : Pressure.Units, default=Pressure.Units.Pa
            Desired output pressure unit.
        check_range : bool, default=True
            Forwarded to `P_Pa(...)`.
        scalar_out : bool, default=False
            If True and input is scalar, return a Python float instead of a 0-d array.

        Returns
        -------
        ArrayLike
            Vapor pressure in the requested unit.
        """
        P_pa = np.asarray(
            self.P_Pa(T, check_range=check_range), 
            dtype=float)
        

        if unit is not Pressure.Units.Pa:
            P_out = Pressure.convert(
                from_=(P_pa, Pressure.Units.Pa), 
                to=unit)
        else:
            P_out = P_pa

        if scalar_out and np.ndim(P_out) == 0:
            return float(P_out)
        return P_out
    

@dataclass(frozen=True)
class VaporPressureAntoineCurve(VaporPressureCurveBase):
    r"""
    Antoine vapor-pressure correlation (base-10).

    Model
    -----
    The Antoine form is evaluated as

    $$
    \log_{10} P_{\mathrm{native}}
    =
    A - \frac{B}{T_{\mathrm{coeff}} + C},
    $$

    where $T_{\mathrm{coeff}}$ is the temperature expressed in the unit assumed
    by the coefficient table (see `T_unit_coeff`), and $P_{\mathrm{native}}$ is
    expressed in the coefficient-native pressure unit (see `P_unit_native`).

    Unit conventions (important)
    ----------------------------
    Antoine coefficient tables are not universal. In particular, many sources
    use $T_{\mathrm{coeff}}$ in °C and $P_{\mathrm{native}}$ in Torr (or bar).
    This class makes the convention explicit:

    - `T_unit_coeff` selects whether the formula uses Kelvin or Celsius.
    - `P_unit_native` declares the pressure unit produced by the coefficients.

    Evaluation pathway
    ------------------
    - Public API comes from `VaporPressureCurveBase`:
      - `P_Pa(T)` returns pressure in Pa (canonical).
      - `P(T, unit=...)` returns pressure converted via `Pressure.convert`.
    - The base class converts input temperatures from `self.T_unit` to Kelvin,
      checks `valid_range_K` in Kelvin, and then calls `_P_Pa_from_K(T_K, ...)`.
    - This subclass converts Kelvin to `T_unit_coeff` as needed, evaluates the
      Antoine expression, and converts `P_unit_native -> Pa`.

    Parameters
    ----------
    A, B, C : float
        Antoine coefficients for the specified table convention.
    T_unit_coeff : Temperature.Units
        Temperature unit expected by the Antoine table (commonly `C` or `K`).
        This controls the $T_{\mathrm{coeff}}$ used inside the formula.
    P_unit_native : Pressure.Units
        Pressure unit produced by the Antoine coefficients.

    Inherited metadata
    ------------------
    T_unit : Temperature.Units
        Unit expected for public inputs to `P_Pa` / `P` (converted internally to K).
    valid_range_K : tuple[float, float] or None
        Valid Kelvin interval for the correlation.
    source : str
        Citation/provenance for the coefficients.

    Raises
    ------
    ValueError
        If $T_K \le 0$, if outside `valid_range_K` when enabled, or if
        $T_{\mathrm{coeff}} + C = 0$ (Antoine singularity).
    """
    A: float
    B: float
    C: float

    P_unit_native: Pressure.Units \
      = field(default=Pressure.Units.bar, kw_only=True)
    T_unit_native: Temperature.Units \
      = field(default=Temperature.Units.K, kw_only=True)

    def _P_Pa_from_K(self, 
        T_K: np.ndarray, 
        check_range: bool = True
    ) -> ArrayLike:
        # Base class checks positivity
        # Base class does range checking
        
        if np.any((T_K + self.C) == 0.0):
            raise ValueError("Antoine singularity: T_K + C = 0.")

        log10P = self.A - self.B / (T_K + self.C)
        P_native = np.power(10.0, log10P)

        # Convert native -> Pa
        if self.P_unit_native is Pressure.Units.Pa:
            return P_native

        return Pressure.convert(
            from_=(P_native, self.P_unit_native), 
            to=Pressure.Units.Pa)

    # Optional convenience (keeps method-level docs where they belong)
    def log10P_native_from_K(self, 
        T_K: ArrayLike, 
        check_range: bool = True
    ) -> ArrayLike:
        """
        T_K: ArrayLike
          temperature in Kelvin
        check_range: bool

        """
        T_K = np.asarray(T_K, dtype=float)
        self._check_temperature_K(T_K, check_range=check_range)
        if np.any((T_K + self.C) == 0.0):
            raise ValueError("Antoine singularity: T_K + C = 0.")
        return self.A - self.B / (T_K + self.C)

    def P_native_from_K(self, 
        T_K: ArrayLike, 
        check_range: bool = True
    ) -> ArrayLike:
        return np.power(10.0, self.log10P_native_from_K(T_K, check_range=check_range))
