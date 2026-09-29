# `TwistGaugeBridgeConstructor` references

## Implementation provenance

The exact implementation basis is the Apache-2.0-licensed donor module recorded
below. The physics publications provide boundary-twist context; this page does
not attribute the destination's exact software formula or sign convention to an
unlocated equation in either publication.

| Claim | Source | Version | Locator | License | Role | Basis | Deviation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EQ-TWIST-GAUGE-BRIDGE` and `EQ-TWIST-GAUGE-DIRECTION` | `ksdft2effmass` | `a3a569064033cfa508d4f9ccbb0509f64745f8d6` | `python/src/ksdft2effmass/solid_state/gauge_bridges.py::TwistGaugeBridgeConstructor.execute` | Apache-2.0 | Extracted implementation lineage | Preserves the site phase and declared matrix direction | Import namespace and owner changed; issue identity uses `DOMAIN` |
| Boundary-twist context | Niu, Thouless, and Wu, *Physical Review B* 31, 3372–3377 | 1985 | `https://doi.org/10.1103/PhysRevB.31.3372` | Publisher terms | Context | Supports the use of twisted boundary conditions in periodic quantum systems | No exact destination equation is claimed from this citation |
| Twist-averaging context | Lin, Zong, and Ceperley, *Physical Review E* 64, 016702 | 2001 | `https://doi.org/10.1103/PhysRevE.64.016702` | Publisher terms | Context | Supports twist-angle boundary-condition terminology | No exact destination equation is claimed from this citation |

## Interpretation

The donor source identity establishes implementation lineage, not scientific
validation. The journal references establish only the stated physical context.
The destination software contract is governed by its current architecture page,
source, and tests.

## Navigation

- [Implementation](../index.md)
- [Class contract](../../index.md)
- [Mathematics](../mathematics/index.md)
- [Repository provenance](../../../../../../../../../provenance/finite-periodic-lattice-source-mapping.md)
