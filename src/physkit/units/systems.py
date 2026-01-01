# physkit/units/systems.py
#
# Author: Eugene Joseph M. Ragasa
# Affiliation: De La Salle University
#
# Canonical unit-system views for physkit quantities.
#
# These classes provide *conventional defaults* only.
# They do NOT perform conversions and carry no state.

from .pressure import Pressure
from .length import Length
from .force import Force
from .temperature import Temperature
from .energy import Energy
from .mass import Mass

class UnitsSI:
  """
  SI unit system (absolute).

  This class defines conventional SI units for each quantity.
  """
  name = "SI"
  length = Length.Units.m
  mass = Mass.Units.kg
  force = Force.Units.N
  pressure = Pressure.Units.Pa
  temperature = Temperature.Units.K
  energy = Energy.Units.J

class UnitsCGS:
  """
  CGS unit system.

  Explicitly uses centimeter–gram–second conventions.
  """
  name = "CGS"
  length = Length.Units.cm
  mass = Mass.Units.g
  force = Force.Units.dyn
  pressure = Pressure.Units.Ba   # barye = dyn / cm^2
  temperature = Temperature.Units.K
  energy = Energy.Units.erg

class UnitsImperial:
  """
  Imperial unit system (absolute).

  Uses absolute force (lbf), not mass-based units.
  """
  length = Length.Units.ft
  mass = Mass.Units.lbm
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
