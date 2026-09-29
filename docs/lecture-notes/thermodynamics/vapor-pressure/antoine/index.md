# Antoine vapor-pressure correlation

## Represented correlation

An Antoine coefficient set represents

$$
\log_{10}P_{\mathrm{native}}
=A-\frac{B}{T_{\mathrm{native}}+C}.
$$

The coefficient table determines the numerical temperature unit of
$T_{\mathrm{native}}$, $B$, and $C$, and the pressure unit of
$P_{\mathrm{native}}$. Those conventions are part of the coefficient model;
they cannot be inferred from $A$, $B$, and $C$ alone.

`AntoineVaporPressureModel` retains `A` as a unitless scalar, `B` and `C` as
unit-bearing temperature scalars, the coefficient-native pressure unit, an
optional unit-aware `AntoineTemperatureRange`, and a nonempty provenance
description.

## Evaluation

`AntoineVaporPressureModel.evaluate(...)` receives temperatures as a
`VectorQuantity` in any compatible physical temperature unit and requires the
output pressure unit explicitly. For each temperature, the internal ActionObject:

1. converts to kelvin to verify positive absolute temperature;
2. optionally enforces the inclusive physical validity interval;
3. converts to the coefficient table's temperature convention;
4. evaluates the base-10 correlation;
5. converts coefficient-native pressure to the requested pressure unit; and
6. returns an `AntoineVaporPressureEvaluation` retaining the complete request
   and pressure vector.

Evaluation rejects nonphysical temperatures, incompatible units, a zero
denominator $T_{\mathrm{native}}+C$, and nonfinite pressure, including numerical
overflow.

## Coefficient provenance

An Antoine coefficient set is meaningful only with its source and native-unit
convention. A validity interval states where that source parameterization is
intended to apply. Disabling range enforcement performs an extrapolation; it
does not extend the documented validity of the coefficient set.

The
[computational laboratory](../../../../../notebooks/thermal/thermo/vapor-pressure/antoine-vapor-pressure.ipynb)
uses synthetic instructional coefficients so its numerical output is not a
literature value or fitted material result.

## Exercises

1. Explain why a coefficient table in degrees Celsius cannot be evaluated by
   substituting kelvin values directly.
2. Derive the multiplicative pressure conversion after evaluating the base-10
   expression.
3. Identify the denominator singularity for a selected value of $C$.
4. Compare range enforcement with explicit extrapolation outside the declared
   interval.
