# Viscoelasticity: Executable Constitutive Models

This four-notebook series develops linear viscoelasticity for upper-undergraduate materials physics. Each notebook follows the same progression:

$$
\text{mechanical model}
\longrightarrow
\text{constitutive equation}
\longrightarrow
\text{loading protocol}
\longrightarrow
\text{response function}
\longrightarrow
\text{parameter inference}.
$$

## Notebook sequence

1. **Compliance functions and creep**
   - Step-stress experiments
   - Spring, dashpot, Kelvin--Voigt, Maxwell, and standard-linear-solid responses
   - Retardation time
   - Fitting creep-compliance data

2. **Stress relaxation**
   - Step-strain experiments
   - Maxwell and standard-linear-solid responses
   - Relaxation time
   - Generalized Maxwell and Prony-series representations
   - Fitting and comparing relaxation models

3. **Laplace transforms and oscillatory loading**
   - Constitutive differential operators
   - Transfer functions
   - Complex modulus
   - Storage modulus, loss modulus, and phase lag
   - Joint fitting of oscillatory data

4. **Time--temperature superposition**
   - Thermorheological simplicity
   - Reduced time and reduced frequency
   - Horizontal shift factors
   - WLF and Arrhenius models
   - Automated master-curve construction

## Shared notation

| Symbol | Meaning | Typical unit |
| --- | --- | --- |
| $\sigma(t)$ | Uniaxial stress | Pa or MPa |
| $\epsilon(t)$ | Uniaxial strain | dimensionless |
| $E$ | Elastic modulus | Pa or MPa |
| $\eta$ | Viscosity | Pa s or MPa s |
| $J(t)$ | Creep compliance | Pa$^{-1}$ or MPa$^{-1}$ |
| $E_r(t)$ | Relaxation modulus | Pa or MPa |
| $\tau$ | Characteristic time | s |
| $E^*(\omega)$ | Complex modulus | Pa or MPa |
| $E'(\omega)$ | Storage modulus | Pa or MPa |
| $E''(\omega)$ | Loss modulus | Pa or MPa |
| $a_T$ | Horizontal time--temperature shift factor | dimensionless |

All numerical examples use MPa, seconds, and radians per second. The notebooks require NumPy, SciPy, Matplotlib, and pandas.

## Suggested use

Run the notebooks in order. The generated datasets use fixed random seeds, so numerical results are reproducible. The data are synthetic and are labeled as such; they are designed to reproduce the structure of experimental creep, relaxation, oscillatory, and multi-temperature measurements.
