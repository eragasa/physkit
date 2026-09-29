# Townsend avalanche and secondary-emission current

## Model

This note introduces the equations used by the
[Townsend-current computational laboratory](../../../../notebooks/plasma-physics/gas-discharge/townsend-current.ipynb).
A primary current $i_0$ crosses a gap of length $d$ with a constant first
Townsend coefficient $\alpha$. The avalanche gain is

$$
M=\exp(\!\alpha d).
$$

A dimensionless secondary-emission coefficient $\gamma_e$ produces the feedback
factor

$$
r=\gamma_e(M-1).
$$

| Symbol | Meaning | SI unit |
| --- | --- | --- |
| $i_0$ | Primary current | A |
| $\alpha$ | First Townsend ionization coefficient | 1/m |
| $d$ | Discharge-gap length | m |
| $\gamma_e$ | Secondary-emission coefficient | dimensionless |
| $M$ | Avalanche gain | dimensionless |
| $r$ | Feedback factor | dimensionless |

## Generational series

The primary avalanche contributes $i_0M$. Each secondary generation contributes
an additional factor of $r$, giving

$$
i=i_0M\left(1+r+r^2+\cdots\right).
$$

For $r<1$, the geometric series has the closed form

$$
i=\frac{i_0M}{1-r}
=\frac{i_0\exp(\!\alpha d)}
{1-\gamma_e\left[\exp(\!\alpha d)-1\right]}.
$$

The represented threshold is

$$
r=\gamma_e(M-1)=1.
$$

At or above this threshold, the package evaluators return an infinite current
with `converged=False`.

## Calculation routes

`TownsendClosedFormCurrentEvaluator` evaluates the geometric-series result
directly. `TownsendGenerationalCurrentEvaluator` accumulates individual
secondary generations and can add the analytic remaining tail after its stopping
rule is satisfied. `TownsendFixedPointCurrentEvaluator` iterates

$$
i_{k+1}=i_0M+ri_k.
$$

All routes return `TownsendCurrentResult`, which correlates current, gain,
feedback factor, term count, and convergence status.

## Numerical behavior

`TownsendDischargeState` accepts nonnegative finite built-in floats. The gain
property returns positive infinity if evaluating $\exp(\!\alpha d)$ overflows.
The iterative evaluators expose their tolerance and iteration limit as explicit
configuration.

## Exercises

1. Derive the closed form from the generational series.
2. Find the threshold $\gamma_e$ for a selected value of $\alpha d$.
3. Compare term counts as $r$ approaches one from below.
4. Run the model with $\gamma_e=0$ and interpret the resulting current ratio.
