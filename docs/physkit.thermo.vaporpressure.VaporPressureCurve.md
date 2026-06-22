
```python
# physkit/thermo/vapor_pressure

@runtime_checkable
class VaporPressureCurve(Protocol):
"""
Interface for equilibrium vapor-pressure models.

Implementations provide a canonical method `P_Pa(T)` returning the
equilibrium vapor pressure in Pascals. Optional metadata may describe
units, validity range, and data provenance.

Attributes
----------
P_unit : Pressure.Units
Native pressure unit associated with the correlation parameters.
Informational only; `P_Pa` always returns Pascals.

T_unit : Temperature.Units
	Temperature unit expected by the implementation. Conventions are implementation-defined.

valid_range_K : tuple[float, float] or None

Valid temperature range in Kelvin for which the correlation is valid.

source : str

Human-readable citation or provenance string.

"""

P_unit: Pressure.Units

T_unit: Temperature.Units

valid_range_K: Optional[Tuple[float, float]]

source: str

  

def P_Pa(self,

T: ArrayLike,

check_range: bool = True

) -> ArrayLike:

"""

Return equilibrium vapor pressure in Pascals.

  

Parameters

----------

T : ArrayLike

Temperature(s) in the units expected by the implementation.

check_range : bool, default=True

If True and a validity range is defined, raise an error when

temperatures are outside the stated range.

  

Returns

-------

ArrayLike

Equilibrium vapor pressure in Pascals.

"""

...
```


## Types of Curve
### Direct Vapor Pressure Curve: $P$ vs $T$
Plot saturation vapor pressure directly as a function of temperature:
$$
P = P_\text{sat}(T).
$$
Features
- Strongly nonlinear, typically exponential-like increase with $T$  
- Intersects ambient pressure at the boiling point  
- Most physically intuitive representation
Use cases
- Engineering estimates  
- Process design (e.g., evaporation, boiling)  
- Quick lookup of pressure at a given $T$

# Vapor Pressure Curves — Common Representations

Vapor pressure data describe the saturation pressure $P_\text{sat}(T)$ at which a phase is in equilibrium with its vapor. The same underlying data are often plotted in different forms depending on the goal: intuition, parameter extraction, or modeling.

---

## 1. Direct Vapor Pressure Curve: $P$ vs $T$

**Definition**

Plot saturation vapor pressure directly as a function of temperature:
$$
P = P_\text{sat}(T).
$$

**Features**

- Strongly nonlinear, typically exponential-like increase with $T$  
- Intersects ambient pressure at the boiling point  
- Most physically intuitive representation

**Use cases**

- Engineering estimates  
- Process design (e.g., evaporation, boiling)  
- Quick lookup of pressure at a given $T$

---

## 2. Clausius–Clapeyron Plot: $\ln P$ vs $1/T$

**Starting point**

For phase equilibrium,
$$
\frac{dP}{dT} = \frac{\Delta H_\text{vap}}{T \Delta V}.
$$

Assuming:
- $\Delta H_\text{vap}$ approximately constant  
- Vapor behaves ideally  
- $\Delta V \approx V_\text{vapor}$

Integration gives:
$$
\ln P = -\frac{\Delta H_\text{vap}}{R}\frac{1}{T} + C.
$$

**Features**

- Approximately linear over moderate $T$ ranges  
- Slope:
$$
m = -\frac{\Delta H_\text{vap}}{R}.
$$

**Use cases**

- Extracting enthalpy of vaporization  
- Thermodynamic analysis  
- Validating data consistency

---

## 3. Antoine-Type Plot: $\log_{10} P$ vs $T$

**Antoine equation**
$$
\log_{10} P = A - \frac{B}{T + C}.
$$

**Features**

- Empirical correlation  
- High accuracy over limited temperature ranges  
- Parameters $(A,B,C)$ tabulated for many substances

**Use cases**

- Chemical engineering calculations  
- Interpolation in databases  
- Process simulation

---

## 4. Reduced Variable (Corresponding States) Plots

**Definitions**
$$
P_r = \frac{P}{P_c}, \qquad
T_r = \frac{T}{T_c}.
$$

**Common forms**

- $P_r$ vs $T_r$  
- $\ln P_r$ vs $1/T_r$

**Features**

- Enables comparison across substances  
- Collapses behavior using critical properties

**Use cases**

- Generalized correlations  
- Equation-of-state development  
- Cross-fluid comparison

---

## 5. Multicomponent / Activity-Based Curves

For mixtures:
- Partial pressures:
$$
P_i(T,x)
$$
- Total pressure:
$$
P_\text{tot} = \sum_i P_i.
$$

**Connections**

- Raoult’s law  
- Henry’s law  
- Activity coefficient models

**Link to evaporation flux**
$$
\Gamma_i \propto
\frac{P_i}{\sqrt{2\pi m_i k_B T}}.
$$

**Use cases**

- Alloy evaporation  
- Thin-film deposition  
- Stoichiometry control

---

## Summary — When to Use Which

| Goal | Recommended Plot |
|------|------------------|
| Intuition / lookup | $P$ vs $T$ |
| $\Delta H_\text{vap}$ extraction | $\ln P$ vs $1/T$ |
| Engineering correlation | Antoine form |
| Cross-fluid comparison | Reduced-variable plots |
| Multicomponent systems | Partial-pressure curves |

---

## Minimal Conceptual Takeaway

All vapor-pressure curves encode the same equilibrium condition:
$$
\mu_\text{liquid} = \mu_\text{vapor}.
$$

Different plots simply linearize or normalize this relationship for specific analytical or practical purposes.
