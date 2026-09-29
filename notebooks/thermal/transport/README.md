# Thermal-transport laboratories

Maintained package-backed laboratories:

- [`phase-change/aluminum-evaporation-legacy-coefficients.ipynb`](phase-change/aluminum-evaporation-legacy-coefficients.ipynb)
  preserves explicitly unverified legacy aluminum coefficients while using the
  maintained Antoine and planar three-dimensional flux APIs; its plots are
  provisional illustrations rather than literature validation.
- [`phase-change/hertz-knudsen-net-flux.ipynb`](phase-change/hertz-knudsen-net-flux.ipynb)
  derives the planar three-dimensional one-way flux from the Maxwell velocity
  distribution, verifies it with numerical quadrature, composes a synthetic
  Antoine pressure, and retains separate and signed flux plots.

The exercise establishes implementation and numerical agreement with the stated
classical ideal-gas model. It does not validate transfer coefficients or a real
material process.
