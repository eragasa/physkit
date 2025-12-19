# physkit/units/pressure.py
# Author: Eugene Joseph M. Ragasa
"""
Pressure units and conversions.

Implementation is intentionally minimal and explicity

- Canonical base unit: Pascal (Pa)
- Units represented via fixed lookup table (tuple)
- Stateless, vectorizable
- No unit algebra
- No parsing
- Explicit
"""

from enum import IntEnum


class Pressure:
  """
  Pressure quantity.

  Canonical base unit: Pa (Pascal)
  """

  class Units(IntEnum):
    # SI-common
    Pa    = 0
    kPa   = 1
    MPa   = 2
    GPa   = 3

    # SI-adjacent
    bar   = 4
    atm   = 5
    mbar  = 6
    hPa   = 7

    # Vacuum units
    Torr  = 8
    mmHg  = 9

    # Imperial / USCS (absolute)
    psi   = 10

    # CGS
    Ba    = 11   # barye = dyne / cm^2

    # Column-based (conventional)
    cmH2O = 12

  # Conversion factors TO Pa (index matches Units enum)
  _TO_PA = (
    1.0,                 # Pa
    1.0e3,               # kPa
    1.0e6,               # MPa
    1.0e9,               # GPa
    1.0e5,               # bar
    101_325.0,           # atm
    100.0,               # mbar
    100.0,               # hPa
    101_325.0 / 760.0,   # Torr (by convention)
    101_325.0 / 760.0,   # mmHg (treated as Torr)
    6894.757293168,      # psi
    0.1,                 # Ba (barye)
    98.0665,             # cmH2O
  )

  @staticmethod
  def convert(*, from_, to: "Pressure.Units"):
    """
    Convert pressure.

    Parameters
    ----------
    from_ : [value, unit_from]
      value : float or numpy.ndarray
      unit_from : Pressure.Units
    to : Pressure.Units

    Returns
    -------
    float or numpy.ndarray
    """
    value, unit_from = from_
    return value * (
      Pressure._TO_PA[int(unit_from)] /
      Pressure._TO_PA[int(to)]
    )

  # ------------------------------------------------------------------
  # Explicit base helpers
  # ------------------------------------------------------------------
  @staticmethod
  def to_canonical(value, unit: "Pressure.Units"):
    """Convert to base unit (Pa)."""
    return value * Pressure._TO_PA[int(unit)]

  @staticmethod
  def from_canonical(value_pa, unit: "Pressure.Units"):
    """Convert from base unit (Pa)."""
    return value_pa / Pressure._TO_PA[int(unit)]

