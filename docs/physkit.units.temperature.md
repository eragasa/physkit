## Temperature Units and Conversions

`Temperature` provides explicit, stateless, and vectorizable temperature conversions with Kelvin (K) as the canonical base unit.

The design is intentionally minimal:
- Explicit affine conversions only  
- No unit algebra  
- No string parsing  
- No hidden state  
- NumPy-vectorizable  
- Float64-coerced inputs  

This module is meant to be a reliable numeric boundary layer for physics modeling.

## Canonical Model
All conversions are expressed as affine maps to Kelvin:
$$
T_K = a_u \, T_u + b_u
$$
where:
- $T_u$ = temperature in unit $u$  
- $a_u$ = scale factor  
- $b_u$ = offset  
- $T_K$ = temperature in Kelvin  
Kelvin is treated as the canonical representation for all temperatures
## Supported Units

| Unit         | Symbol               | Relation to K                                       |                        |
| ------------ | -------------------- | --------------------------------------------------- | ---------------------- |
| Kelvin       | $\mathrm{K}$         | $T_\mathrm{K} = T_\mathrm{K}$                       | `Temperature.Units.K`  |
| Celsius      | ${}^\circ\mathrm{C}$ | $T_\mathrm{K} = T_\mathrm{C} + 273.15$              | `Temperature.UnitsC`   |
| milli-Kelvin | $\mathrm{mK}$        | $T_\mathrm{K} = 10^{-3}\, T_\mathrm{mK}$            | `Temperature.Units.mK` |
| Fahrenheit   | ${}^\circ F$         | $T_\mathrm{K} = \frac{5}{9}(T_\mathrm{F} + 459.67)$ | `Temperature.Units.F`  |
| Rankine      | ${}^\circ R$         | $T_\mathrm{K} = \frac{5}{9} T_\mathrm{R}$           | `Temperature.Units.R`  |

---
## Core API

### `to_canonical`

```python
Temperature.to_canonical(value, unit)
````

Convert temperature to Kelvin.

**Returns:** `np.ndarray` (possibly 0-D)

---

### `from_canonical`

```python
Temperature.from_canonical(value_K, unit)
```

Convert from Kelvin to a target unit.

**Returns:** `np.ndarray` (possibly 0-D)

---

### `convert`

```python
Temperature.convert(value, units_from, units_to)
```

General unit conversion.

Equivalent to:

$$  
T_{out} = f^{-1}_{u_{to}}\bigl(f_{u_{from}}(T)\bigr)  
$$

**Example**

```python
T_K = Temperature.convert(25.0,
                          Temperature.Units.C,
                          Temperature.Units.K)
```

Vectorized usage:

```python
T_C = np.array([20,30,40])
T = Temperature.convert(
    value=T_C,
    from=Temperature.Units.C,
    to=Temperature.Units.K
)
```

---

### `check_in_range`

```python
Temperature.check_in_range(
    T_array,
    units,
    valid_range,
    inclusive=True
)
```

Validate that temperatures lie within a specified range.
- No unit conversion is performed
- `valid_range` must be expressed in `units`
- Used for parameter validity checks in correlations
    

**Example**

```python
Temperature.check_in_range(
    T_array=T,
    units=Temperature.Units.K,
    valid_range=(200.0, 400.0)
)
```

---

## Design Philosophy

### 1) Kelvin as Canonical

Thermodynamic relations require absolute temperature:

$$  
T > 0 \text{ K}  
$$

Using Kelvin internally avoids hidden offsets and mistakes.

---

### 2) Explicit Over Magic

No automatic parsing or inference:

```python
Temperature.convert(T, Units.C, Units.K)
```

is preferred over guessing units.

---

### 3) Array-First Semantics

All functions:
- Accept scalars or arrays
- Return NumPy arrays
- Preserve vectorization
This supports simulation and fitting workflows.

### 4) Numeric Discipline
Inputs are coerced to float64 via `as_f64_array`.

This ensures stable behavior for:
- regression
- exponentials

## Intended Use

This class is a low-level infrastructure component for:
- vapor-pressure correlations
- thermodynamic models
- materials simulations
- experimental data processing

It is not meant to be a full unit system.

---

## Summary

`Temperature` provides:
- Deterministic affine conversions
- Kelvin-centric canonical representation
- Vectorized numeric behavior
- Minimal, inspectable logic

It serves as a stable foundation for higher-level thermo modules in **physkit**.