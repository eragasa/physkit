# `MaxwellBoltzmannSpeedDistributionEvaluator` source lineage

## Internal extraction

The initial formula and examples were extracted from overlapping exploratory
notebooks formerly located at:

- `notebooks/statmech/kinetic/mb_velocity_distribution.ipynb`
- `notebooks/gas/dev_maxwell_speed_pdf.ipynb`

Git history retains both source identities. The extraction preserves their
shared SI formula while adding explicit DataObject and ActionObject ownership,
closed runtime types, invariant checks, characteristic-speed properties, and
software and numerical tests.

One source notebook described its figure as equivalent to “Ohring Fig. 2.1” but
did not provide enough bibliographic detail to verify a precise source locator.
This architecture record therefore does not attribute the software formula or a
validation claim to that incomplete reference.

The maintained derivation is in
[`docs/lecture-notes/statistical-mechanics/maxwell-boltzmann-speed/index.md`](../../../../../../../../../lecture-notes/statistical-mechanics/maxwell-boltzmann-speed/index.md).

## Navigation

- [Implementation](../index.md)
- [Mathematics](../mathematics/index.md)
- [Class contract](../../index.md)
