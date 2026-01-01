# physkit/units/mass.py
# Author: Eugene Joseph M. Ragasa
"""
Mass units and conversions

Implementation is intentionally minimal and explicit

- Canonical base unit: kilogram (kg)
"""
from enum import IntEnum


class Mass:
  """
  Mass quantity.

  Canonical unit: kilogram (kg)
  """

  class Units(IntEnum):
    # SI
    kg   = 0
    g    = 1
    mg   = 2
    t    = 3   # metric tonne

    # Imperial / USCS
    lbm   = 4   # pound-mass
    oz   = 5   # ounce-mass

  _TO_KG = (
    1.0,                # kg
    1.0e-3,             # g
    1.0e-6,             # mg
    1.0e3,              # t
    0.45359237,         # lb
    0.028349523125,    # oz
  )

  # ------------------------------------------------------------------
  # Core conversion
  # ------------------------------------------------------------------
  @staticmethod
  def convert(*, from_, to: "Mass.Units"):
    """
    Convert mass values between units.
    """
    value, unit_from = from_

    value_kg = Mass._to_canonical(value, unit_from)
    return Mass._from_canonical(value_kg, to)

  # ------------------------------------------------------------------
  # Internal canonical helpers
  # ------------------------------------------------------------------
  @staticmethod
  def _to_canonical(value, unit: "Mass.Units"):
    """Convert value to canonical unit (kg)."""
    return value * Mass._TO_KG[int(unit)]

  @staticmethod
  def _from_canonical(value_kg, unit: "Mass.Units"):
    """Convert value from canonical unit (kg)."""
    return value_kg / Mass._TO_KG[int(unit)]
