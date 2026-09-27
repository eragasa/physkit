"""Immutable finite periodic index domains in one, two, and three dimensions.

The records in this module represent integer lattice coordinates and finite periodic
quotients of an integer index lattice. They do not represent atomic Cartesian
positions, physical crystal lattice vectors, or calculator geometry. The last axis
varies fastest in the only initially supported tensor-product ordering.

This implementation preserves the represented behavior of
``ksdft2effmass.solid_state.geometry`` at donor revision
``7bd913151f7e61ed2bdba593df920be36573b502``.

References
----------
.. [1] N. W. Ashcroft and N. D. Mermin, *Solid State Physics*, Holt,
   Rinehart and Winston (1976), ISBN 0-03-083993-9.
.. [2] M. Newman, *Integral Matrices*, Academic Press (1972),
   ISBN 978-0-12-517850-1.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, StrEnum

from physkit.core.results import ResultsObject

type LatticeIntegerComponents = tuple[int] | tuple[int, int] | tuple[int, int, int]
"""Closed integer coordinate representation for one, two, or three dimensions."""


class LatticeDimension(IntEnum):
    """Supported spatial lattice dimensions."""

    ONE = 1
    TWO = 2
    THREE = 3


class LatticeSiteOrdering(StrEnum):
    """Supported tensor-product site ordering conventions."""

    LAST_AXIS_FASTEST = "last_axis_fastest"


@dataclass(frozen=True, slots=True)
class LatticeCoordinate:
    """Represent one integer coordinate in a declared lattice dimension.

    Parameters
    ----------
    dimension
        Exact supported spatial dimension.
    components
        Tuple of exactly ``dimension`` built-in integers. Boolean and NumPy integer
        values are rejected. Components are lattice indices, not physical lengths.
    """

    dimension: LatticeDimension
    components: LatticeIntegerComponents

    def __post_init__(self) -> None:
        """Validate the closed dimensional coordinate contract."""
        if type(self.dimension) is not LatticeDimension:
            raise TypeError("dimension must be LatticeDimension")
        if type(self.components) is not tuple:
            raise TypeError("components must be a tuple")
        if len(self.components) != self.dimension.value:
            raise ValueError("coordinate component count must match dimension")
        if any(type(value) is not int for value in self.components):
            raise TypeError("coordinate components must be built-in integers")


@dataclass(frozen=True, slots=True)
class LatticeDisplacement:
    """Represent one integer lattice displacement.

    Parameters
    ----------
    dimension
        Exact supported spatial dimension.
    components
        Tuple of exactly ``dimension`` built-in integers. Components are differences
        of lattice indices and may be negative or zero.
    """

    dimension: LatticeDimension
    components: LatticeIntegerComponents

    def __post_init__(self) -> None:
        """Validate the closed dimensional displacement contract."""
        if type(self.dimension) is not LatticeDimension:
            raise TypeError("dimension must be LatticeDimension")
        if type(self.components) is not tuple:
            raise TypeError("components must be a tuple")
        if len(self.components) != self.dimension.value:
            raise ValueError("displacement component count must match dimension")
        if any(type(value) is not int for value in self.components):
            raise TypeError("displacement components must be built-in integers")

    @property
    def is_zero(self) -> bool:
        """Return whether every displacement component is exactly zero."""
        return all(value == 0 for value in self.components)


@dataclass(frozen=True, slots=True)
class FinitePeriodicDomain:
    """Represent one finite periodic tensor-product index domain.

    Parameters
    ----------
    dimension
        Exact supported spatial dimension.
    extents
        Positive built-in integer cell counts, one per axis.
    ordering
        Tensor-product ordering. Version one supports only
        :attr:`LatticeSiteOrdering.LAST_AXIS_FASTEST`.
    """

    dimension: LatticeDimension
    extents: LatticeIntegerComponents
    ordering: LatticeSiteOrdering = LatticeSiteOrdering.LAST_AXIS_FASTEST

    def __post_init__(self) -> None:
        """Validate dimension, positive extents, and ordering."""
        if type(self.dimension) is not LatticeDimension:
            raise TypeError("dimension must be LatticeDimension")
        if type(self.extents) is not tuple:
            raise TypeError("extents must be a tuple")
        if len(self.extents) != self.dimension.value:
            raise ValueError("extent count must match dimension")
        if any(type(value) is not int for value in self.extents):
            raise TypeError("extents must be built-in integers")
        if any(value <= 0 for value in self.extents):
            raise ValueError("extents must be positive")
        if type(self.ordering) is not LatticeSiteOrdering:
            raise TypeError("ordering must be LatticeSiteOrdering")
        if self.ordering is not LatticeSiteOrdering.LAST_AXIS_FASTEST:
            raise ValueError("unsupported lattice site ordering")

    @property
    def cell_count(self) -> int:
        """Return the exact number of represented lattice cells."""
        result = 1
        for extent in self.extents:
            result *= extent
        return result


class FinitePeriodicDomainIndexer:
    """Map a compatible coordinate to a last-axis-fastest linear index."""

    __slots__ = ()

    def execute(
        self, domain: FinitePeriodicDomain, coordinate: LatticeCoordinate
    ) -> int:
        """Return the zero-based linear index for ``coordinate``.

        Parameters
        ----------
        domain
            Finite periodic domain defining extents and ordering.
        coordinate
            In-domain coordinate with the same dimension as ``domain``.

        Returns
        -------
        int
            Zero-based last-axis-fastest index.

        Raises
        ------
        TypeError
            If an input has the wrong semantic type.
        ValueError
            If dimensions differ or a component lies outside the domain.
        """
        if type(domain) is not FinitePeriodicDomain:
            raise TypeError("domain must be FinitePeriodicDomain")
        if type(coordinate) is not LatticeCoordinate:
            raise TypeError("coordinate must be LatticeCoordinate")
        if domain.dimension is not coordinate.dimension:
            raise ValueError("domain and coordinate dimensions must agree")
        if any(
            component < 0 or component >= extent
            for component, extent in zip(
                coordinate.components, domain.extents, strict=True
            )
        ):
            raise ValueError("coordinate must lie within the finite periodic domain")
        result = 0
        for component, extent in zip(
            coordinate.components, domain.extents, strict=True
        ):
            result = result * extent + component
        return result


class FinitePeriodicCoordinateResolver:
    """Resolve a last-axis-fastest linear index to one lattice coordinate."""

    __slots__ = ()

    def execute(self, domain: FinitePeriodicDomain, index: int) -> LatticeCoordinate:
        """Return the coordinate represented by ``index``.

        Parameters
        ----------
        domain
            Finite periodic domain defining extents and ordering.
        index
            Built-in integer in ``[0, domain.cell_count)``. Booleans are rejected.

        Returns
        -------
        LatticeCoordinate
            Coordinate in the same dimension as ``domain``.
        """
        if type(domain) is not FinitePeriodicDomain:
            raise TypeError("domain must be FinitePeriodicDomain")
        if type(index) is not int:
            raise TypeError("index must be a built-in integer")
        if index < 0 or index >= domain.cell_count:
            raise ValueError("index must lie within the finite periodic domain")
        remainder = index
        components = [0] * domain.dimension.value
        for axis in range(domain.dimension.value - 1, -1, -1):
            extent = domain.extents[axis]
            remainder, components[axis] = divmod(remainder, extent)
        values = tuple(components)
        if domain.dimension is LatticeDimension.ONE:
            closed: LatticeIntegerComponents = (values[0],)
        elif domain.dimension is LatticeDimension.TWO:
            closed = (values[0], values[1])
        else:
            closed = (values[0], values[1], values[2])
        return LatticeCoordinate(domain.dimension, closed)


@dataclass(frozen=True, slots=True)
class PeriodicImageResult(ResultsObject):
    """Record one periodic wrap and its integer boundary-crossing quotient.

    Parameters
    ----------
    coordinate
        Wrapped coordinate inside the finite periodic domain.
    quotient
        Integer number of crossed boundaries along each axis.
    """

    coordinate: LatticeCoordinate
    quotient: LatticeDisplacement

    def __post_init__(self) -> None:
        """Require wrapped coordinate and quotient dimensions to agree."""
        if type(self.coordinate) is not LatticeCoordinate:
            raise TypeError("coordinate must be LatticeCoordinate")
        if type(self.quotient) is not LatticeDisplacement:
            raise TypeError("quotient must be LatticeDisplacement")
        if self.coordinate.dimension is not self.quotient.dimension:
            raise ValueError("coordinate and quotient dimensions must agree")


class PeriodicImageResolver:
    """Resolve any integer coordinate into a finite periodic image."""

    __slots__ = ()

    def execute(
        self, domain: FinitePeriodicDomain, coordinate: LatticeCoordinate
    ) -> PeriodicImageResult:
        """Wrap ``coordinate`` and retain Euclidean-division quotients.

        Negative coordinates use Python's Euclidean ``divmod`` semantics, so every
        remainder lies in the half-open interval for its positive extent.
        """
        if type(domain) is not FinitePeriodicDomain:
            raise TypeError("domain must be FinitePeriodicDomain")
        if type(coordinate) is not LatticeCoordinate:
            raise TypeError("coordinate must be LatticeCoordinate")
        if domain.dimension is not coordinate.dimension:
            raise ValueError("domain and coordinate dimensions must agree")
        quotient_values: list[int] = []
        wrapped_values: list[int] = []
        for component, extent in zip(
            coordinate.components, domain.extents, strict=True
        ):
            quotient, wrapped = divmod(component, extent)
            quotient_values.append(quotient)
            wrapped_values.append(wrapped)
        if domain.dimension is LatticeDimension.ONE:
            wrapped_components: LatticeIntegerComponents = (wrapped_values[0],)
            quotient_components: LatticeIntegerComponents = (quotient_values[0],)
        elif domain.dimension is LatticeDimension.TWO:
            wrapped_components = (wrapped_values[0], wrapped_values[1])
            quotient_components = (quotient_values[0], quotient_values[1])
        else:
            wrapped_components = (
                wrapped_values[0],
                wrapped_values[1],
                wrapped_values[2],
            )
            quotient_components = (
                quotient_values[0],
                quotient_values[1],
                quotient_values[2],
            )
        return PeriodicImageResult(
            LatticeCoordinate(domain.dimension, wrapped_components),
            LatticeDisplacement(domain.dimension, quotient_components),
        )
