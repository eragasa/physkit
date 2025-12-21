# physkit/units/systems.py
#
# Author: Eugene Joseph M. Ragasa
# Affiliation: De La Salle University
#
# Canonical unit-system views for physkit quantities.
#
# These classes provide *conventional defaults* only.
# They do NOT perform conversions and carry no state.

from physkit.units.pressure import Pressure
from physkit.units.length import Length
from physkit.units.force import Force
from physkit.units.temperature import Temperature

class UnitsSI:
  """
  SI unit system (absolute).

  This class defines conventional SI units for each quantity.
  """
  length = Length.Units.m
  force = Force.Units.N
  pressure = Pressure.Units.Pa
  temperature = Temperature.Units.K

class UnitsCGS:
  """
  CGS unit system.

  Explicitly uses centimeter–gram–second conventions.
  """
  length = Length.Units.cm
  force = Force.Units.dyn
  pressure = Pressure.Units.Ba   # barye = dyn / cm^2
  temperature = Temperature.Units.K

class UnitsImperial:
  """
  Imperial unit system (absolute).

  Uses absolute force (lbf), not mass-based units.
  """
  length = Length.Units.ft
  force = Force.Units.lbf
  pressure = Pressure.Units.psi
  temperature = Temperature.Units.R

class UnitsUSCS:
  """
  US Customary System (engineering, absolute)
  """
  length = Length.Units.ft
  force = Force.Units.lbf
  pressure = Pressure.Units.psi
  temperature = Temperature.Units.R
