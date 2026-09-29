# Thermodynamics laboratories

Maintained package-backed laboratories:

- [`eos/ideal_gas.ipynb`](eos/ideal_gas.ipynb) uses
  `projectkoios.physkit.thermal.thermo.eos.ideal_gas`, constructs an ordered
  package-owned isotherm family, and plots pressure–volume curves.
- [`mixtures/symmetric-regular-solution.ipynb`](mixtures/symmetric-regular-solution.ipynb)
  evaluates unit-aware molar mixing quantities, checks local curvature without
  making coexistence claims, and retains the mixing-quantity plot.
- [`vapor-pressure/antoine-vapor-pressure.ipynb`](vapor-pressure/antoine-vapor-pressure.ipynb)
  uses `projectkoios.physkit.thermal.thermo.vaporpressure.antoine` and retains a
  semilogarithmic vapor-pressure plot.

Passing notebook checks establish implementation conformance for the represented
examples, not scientific validation for a real material or thermodynamic range.
