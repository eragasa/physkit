# Lattice-Scattering Mobility

> **Definition — Lattice-limited mobility**  
> The lattice-scattering-limited mobility is defined by the power-law relation  
> $$\mu_{\text{lat}}(T)
   = \mu_{\text{lat}}(T_{\text{ref}})
     \left(\frac{T}{T_{\text{ref}}}\right)^{-\alpha_{\text{lat}}}.$$
> Here $T$ is temperature, $T_{\text{ref}}$ is a chosen reference temperature (usually $300\ \text{K}$), and $\alpha_{\text{lat}}$ is an exponent associated with acoustic-phonon scattering (typically $3/2$).

## Physical Meaning

Lattice scattering arises from thermally excited lattice vibrations (phonons).  
As temperature increases:

- phonon population increases,  
- carrier momentum-relaxation time decreases,  
- mobility decreases.

The model above captures this trend by enforcing a negative power law in temperature.

## Typical Values

- $T_{\text{ref}} = 300\ \text{K}$  
- $\alpha_{\text{lat}} \approx 3/2$ for acoustic-phonon deformation-potential scattering  
- $\mu_{\text{lat}}(300\ \text{K})$ is a material parameter (e.g., electrons in Si: $\sim 1500\ \text{cm}^2/\text{V·s}$; holes: $\sim 450\ \text{cm}^2/\text{V·s}$)

## Usage Notes

- This is a **phenomenological** model appropriate for undergraduate and early-graduate semiconductor physics.  
- The exponent $\alpha_{\text{lat}}$ may be tuned to fit measured data for specific materials or temperature ranges.  
- When combined with impurity scattering via Matthiessen’s rule, the total mobility becomes  
  $$\frac{1}{\mu_{\text{tot}}}
    = \frac{1}{\mu_{\text{lat}}}
    + \frac{1}{\mu_{\text{imp}}}.$$


