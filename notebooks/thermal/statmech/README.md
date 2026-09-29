# Statistical-mechanics laboratories

Maintained package-backed laboratories:

- [`distributions/occupations/ideal-occupation-statistics.ipynb`](distributions/occupations/ideal-occupation-statistics.ipynb)
  evaluates Fermi--Dirac, Bose--Einstein, and Maxwell--Boltzmann factors from
  explicit energy, chemical-potential, and temperature quantities and retains a
  three-curve semilogarithmic plot.
- [`distributions/boltzmann-exponential-energy-distribution.ipynb`](distributions/boltzmann-exponential-energy-distribution.ipynb)
  uses a unit-aware normalized exponential energy density with an explicit
  constant-density-of-states assumption and retains a three-curve plot.
- [`transport/knudsen-number.ipynb`](transport/knudsen-number.ipynb) composes
  hard-sphere mean free paths with a unit-aware characteristic-length ratio and
  retains a logarithmic pressure plot without assigning flow-regime labels.
- [`radiation/blackbody-wavelength-spectrum.ipynb`](radiation/blackbody-wavelength-spectrum.ipynb)
  compares unit-aware Planck, Wien, and Rayleigh--Jeans spectral energy
  densities and retains exact and asymptotic plots.
- [`quantum/thermal-de-broglie-wavelength.ipynb`](quantum/thermal-de-broglie-wavelength.ipynb)
  combines an analytical derivation with independent Gaussian quadrature,
  evaluates $n\lambda_T^3$, and retains a logarithmic wavelength plot.
- [`kinetic/maxwell-boltzmann-speed-distribution.ipynb`](kinetic/maxwell-boltzmann-speed-distribution.ipynb)
  uses `projectkoios.physkit.thermal.statmech.kinetic_theory` with explicit
  temperature, molar-mass, speed, and probability-density units.
- [`kinetic/mfp.ipynb`](kinetic/mfp.ipynb) uses unit-aware hard-sphere gas state
  properties and retains a logarithmic mean-free-path plot.

The energy-density, speed-density, and mean-free-path examples establish only
their documented software and numerical checks; they are not material-specific
scientific validation.
