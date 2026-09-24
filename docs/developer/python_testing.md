# Python testing conventions

## Mirrored module layout

Tests mirror the implementation module as a directory. A test for one class
method uses:

```text
tests/<package>/<subpackage>/<module>/test__<ClassName>__<method>.py
```

Examples:

```text
src/physkit/units/systems.py
tests/physkit/units/systems/test__UnitSystem__energy_unit.py

src/physkit/qm/piab1d/tise_fd/solver.py
tests/physkit/qm/piab1d/tise_fd/solver/
    test__Piab1dTiseFdSolver__solve.py
```

Use `init` for constructor tests and the property name for property tests. Keep
unrelated classes and methods in separate files. Shared fixtures may live in the
mirrored module directory's `conftest.py`.

## Test scope

Each test should state one observable requirement through its name and assertions.
Verify nominal type ownership, dimensional units, immutable storage, shape
correlation, numerical values, and failure behavior where applicable.

For migrated numerical code, retain the donor's exact represented formulas and
add selected-scale checks. In particular, physical quantum tests must verify that
matrices remain in the requested numerical scale rather than merely being
dimensionally convertible through SI.

## Execution

Run the narrowest relevant test directory while developing, followed by the
connected numerical layer. Examples:

```bash
python -m pytest -q tests/physkit/qm/piab1d
python -m pytest -q tests/physkit/operators/operators_1d/fd
python -m pytest -q tests/physkit/operators/qm/qm_1d
python -m pytest -q tests/physkit/numerics/eigenproblems/real_symmetric
```

Also compile changed Python modules and run `git diff --check`.

## Deprecated tests

Tests retained specifically for `physkit.legacy` use the registered
`@pytest.mark.deprecated` marker, either directly or through module-level
`pytestmark`. Maintained implementation tests must not carry this marker or
import deprecated modules.

## Evidence boundaries

Passing tests establishes only the requirements actually asserted. Keep software
verification, numerical verification, physical validation, pedagogical
validation, and uncertainty quantification distinct. Executing a notebook or
reproducing a finite matrix identity does not by itself validate a physical
model.
