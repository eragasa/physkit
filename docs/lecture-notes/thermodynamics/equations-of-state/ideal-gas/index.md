# Ideal-gas equation of state

For amount of substance $n$, molar gas constant $R_g$, absolute temperature
$T$, volume $V$, and pressure $P$, the ideal-gas equation of state is

$$
PV=nR_gT.
$$

At fixed temperature, the pressure is

$$
P(V;T)=\frac{nR_gT}{V},
$$

which defines one pressure–volume isotherm. An ordered temperature vector
defines a corresponding family of isotherms on shared volume coordinates.

`IdealGasEquationOfState` retains the unit-bearing amount of substance. Its
`evaluate_pressure(...)` façade returns one isotherm, while
`evaluate_isotherms(...)` returns an immutable iterable in requested-temperature
order. Volumes, temperatures, and output pressures carry explicit compatible
physical units.

The [computational laboratory](../../../../../notebooks/thermal/thermo/eos/ideal_gas.ipynb)
verifies $PV/(nR_gT)=1$ after unit conversion and plots five pressure–volume
isotherms. This verifies the represented software model; it does not validate
ideal-gas behavior for a real material or state range.
