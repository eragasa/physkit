[[physkit.thermo.__init__]]
[[physkit.thermo.protocols.VaporPressureCurve]]
[[physkit.thermo.protocols.VaporPressureCurveBase]]
[[physkit.thermo.protocols.VaporPressureCurveAntoine]]


[[physkit.thermo.vaporpressure.VaporPressureCurve]]


##### Antoine Equation
Antoine (1888) proposed
$$
  \log_{10} P = A - \frac{B}{T+C-273.15}
$$
where
- $A$, $B$, $C$: parameters of the model
- $P$: vapor pressure

For the limit, $C \to 0$, the Antoine equation reverts to the Clapeyron equation.   Simple rules have been proposed (Fishtine, 1963; Thompson, 1959) to relate C to the normal boiling point for certain classes of materials, but these rulesare not reliable and the only reliable way to obtain values of the constants A , B ,and C is to regress experimental data.

