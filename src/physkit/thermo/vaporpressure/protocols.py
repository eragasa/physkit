# physkit.thermo.vaporpressure.protocols.py
# Eugene Joseph M. Ragasa 2026

from __future__ import annotations

from typing import (
    Protocol,
    Optional,
    Tuple,
    runtime_checkable
)

from physkit.units import Temperature, Pressure
from physkit.types import ArrayLike


@runtime_checkable
class VaporPressureCurve(Protocol):
    """
    Minimal interface for a saturation vapor-pressure correlation.

    Many published/tabulated vapor-pressure correlations are parameterized in
    non-SI units (e.g., torr, mmHg, bar; °C rather than K). This protocol allows
    implementations to *store* their native parameterization in the source's
    units while guaranteeing a single canonical output:

        P_Pa(T) -> saturation vapor pressure in Pascals.

    Temperature input follows the implementation's declared `T_unit` convention.
    The attributes are metadata for documentation/provenance; correctness is
    enforced by the required canonical method `P_Pa`.

    Attributes
    ----------
    param_P_unit : str
        Native pressure unit of the correlation parameters (informational).
        `P_Pa` must still return Pascals.
    param_T_unit : str
        Native temperature unit expected by the correlation parameters
        (informational).
    param_T_valid_range : tuple[float, float] | None
        Valid temperature range expressed in `T_unit` (informational).
    source : str
        Provenance string (e.g., handbook/table + page, DOI).

    Notes
    -----
    Implementations should perform any needed unit conversions internally in
    `pressure_Pa`, and should accept NumPy arrays for vectorized evaluation.
    """

    param_P_unit: Pressure.Units
    param_T_unit: Temperature.Units
    param_T_valid_range: Optional[Tuple[float, float]]
    source: str

    def pressure_Pa(self, 
                    T_K: ArrayLike) -> ArrayLike: ...

    def pressure(self, 
        T: ArrayLike, 
        T_units: Temperature.Units = Temperature.Units.K,
        P_units: Pressure.Units = Pressure.Units.Pa
    ) -> ArrayLike:
        """
        Return saturation vapor pressure in requested units.

        Parameters
        ----------
        T : float or ndarray
            Temperature values in `T_unit`.
        T_units : Temperature.Units
            Unit for the input temperature.
        P_units : Pressure.Units
            Desired output pressure unit.

        Returns
        -------
        float or ndarray
            Saturation vapor pressure in `P_unit`.
        """
        ...
