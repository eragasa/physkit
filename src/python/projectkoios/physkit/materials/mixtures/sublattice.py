r"""Immutable site-fraction compositions on finite ordered sublattices."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from projectkoios.physkit.core.actions import ActionizedDataObject
from projectkoios.physkit.core.data import DataObject
from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.units import ScalarQuantity, Unitless, VectorQuantity

_NORMALIZATION_ABSOLUTE_TOLERANCE = 1.0e-12


@dataclass(frozen=True, slots=True, kw_only=True)
class SublatticeSpecification(DataObject):
    """Identify one sublattice, its allowed species, and multiplicity."""

    name: str
    species: tuple[str, ...]
    multiplicity: ScalarQuantity

    def __post_init__(self) -> None:
        """Check every sublattice specification argument."""
        self._check_arg_name()
        self._check_arg_species()
        self._check_arg_multiplicity()

    def _check_arg_name(self) -> None:
        """Require a nonempty sublattice name."""
        if not isinstance(self.name, str):
            raise TypeError("name must be a string")
        if not self.name:
            raise ValueError("name must be nonempty")

    def _check_arg_species(self) -> None:
        """Require unique ordered nonempty species identifiers."""
        if not isinstance(self.species, tuple) or not all(
            isinstance(species_name, str) for species_name in self.species
        ):
            raise TypeError("species must be a tuple of strings")
        if not self.species or any(not name for name in self.species):
            raise ValueError("species identifiers must be nonempty")
        if len(set(self.species)) != len(self.species):
            raise ValueError("species identifiers must be unique")

    def _check_arg_multiplicity(self) -> None:
        """Require a positive unitless sites-per-formula-unit value."""
        if not isinstance(self.multiplicity, ScalarQuantity):
            raise TypeError("multiplicity must be ScalarQuantity")
        if not isinstance(self.multiplicity.unit, Unitless):
            raise ValueError("multiplicity must be unitless")
        if self.multiplicity.magnitude <= 0.0:
            raise ValueError("multiplicity must be positive")


@dataclass(frozen=True, slots=True, eq=False, kw_only=True)
class SublatticeSiteFractions(DataObject):
    """Pair one sublattice specification with a normalized fraction vector."""

    specification: SublatticeSpecification
    fractions: VectorQuantity

    def __post_init__(self) -> None:
        """Check every site-fraction record argument."""
        self._check_arg_specification()
        self._check_arg_fractions()

    def _check_arg_specification(self) -> None:
        """Require a sublattice specification."""
        if not isinstance(self.specification, SublatticeSpecification):
            raise TypeError("specification must be SublatticeSpecification")

    def _check_arg_fractions(self) -> None:
        """Require a nonnegative unitless vector normalized to one."""
        if not isinstance(self.fractions, VectorQuantity):
            raise TypeError("fractions must be VectorQuantity")
        if not isinstance(self.fractions.unit, Unitless):
            raise ValueError("fractions must be unitless")
        if self.fractions.magnitude.shape != (len(self.specification.species),):
            raise ValueError("fractions must have one value per allowed species")
        if np.any(self.fractions.magnitude < 0.0):
            raise ValueError("fractions must be nonnegative")
        if not np.isclose(
            float(np.sum(self.fractions.magnitude)),
            1.0,
            rtol=0.0,
            atol=_NORMALIZATION_ABSOLUTE_TOLERANCE,
        ):
            raise ValueError("fractions must sum to one")

    def fraction_for(self, *, species_name: str) -> ScalarQuantity:
        """Return the site fraction of one allowed species."""
        if not isinstance(species_name, str):
            raise TypeError("species_name must be a string")
        try:
            index = self.specification.species.index(species_name)
        except ValueError as error:
            raise KeyError(
                f"species {species_name!r} is not allowed on "
                f"sublattice {self.specification.name!r}"
            ) from error
        return ScalarQuantity(
            magnitude=float(self.fractions.magnitude[index]),
            unit=Unitless(),
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class SiteFractionOverallCompositionEvaluationRequest(DataObject):
    """Request an overall composition with explicit species exclusions."""

    mixture: SiteFractionMixture
    excluded_species: tuple[str, ...]

    def __post_init__(self) -> None:
        """Check every overall-composition request argument."""
        self._check_arg_mixture()
        self._check_arg_excluded_species()

    def _check_arg_mixture(self) -> None:
        """Require a site-fraction mixture."""
        if not isinstance(self.mixture, SiteFractionMixture):
            raise TypeError("mixture must be SiteFractionMixture")

    def _check_arg_excluded_species(self) -> None:
        """Require unique nonempty species identifiers present in the mixture."""
        if not isinstance(self.excluded_species, tuple) or not all(
            isinstance(name, str) for name in self.excluded_species
        ):
            raise TypeError("excluded_species must be a tuple of strings")
        if any(not name for name in self.excluded_species):
            raise ValueError("excluded species identifiers must be nonempty")
        if len(set(self.excluded_species)) != len(self.excluded_species):
            raise ValueError("excluded species identifiers must be unique")
        available = {
            species_name
            for sublattice in self.mixture.sublattices
            for species_name in sublattice.specification.species
        }
        unknown = set(self.excluded_species) - available
        if unknown:
            raise ValueError(f"excluded species are absent: {sorted(unknown)!r}")


@dataclass(frozen=True, slots=True, eq=False, kw_only=True)
class SiteFractionOverallCompositionEvaluation(ResultsObject):
    """Retain one request and its included overall composition."""

    request: SiteFractionOverallCompositionEvaluationRequest
    included_species: tuple[str, ...]
    amounts_per_formula_unit: VectorQuantity
    mole_fractions: VectorQuantity

    def __post_init__(self) -> None:
        """Check every overall-composition response argument."""
        self._check_arg_request()
        self._check_arg_included_species()
        self._check_arg_amounts_per_formula_unit()
        self._check_arg_mole_fractions()

    def _check_arg_request(self) -> None:
        """Require the complete evaluation request."""
        if not isinstance(
            self.request,
            SiteFractionOverallCompositionEvaluationRequest,
        ):
            raise TypeError(
                "request must be SiteFractionOverallCompositionEvaluationRequest"
            )

    def _check_arg_included_species(self) -> None:
        """Require unique ordered included species identifiers."""
        if not isinstance(self.included_species, tuple) or not all(
            isinstance(name, str) for name in self.included_species
        ):
            raise TypeError("included_species must be a tuple of strings")
        if not self.included_species:
            raise ValueError("included_species must be nonempty")
        if len(set(self.included_species)) != len(self.included_species):
            raise ValueError("included_species must be unique")

    def _check_arg_amounts_per_formula_unit(self) -> None:
        """Require nonnegative unitless amounts for included species."""
        if not isinstance(self.amounts_per_formula_unit, VectorQuantity):
            raise TypeError("amounts_per_formula_unit must be VectorQuantity")
        if not isinstance(self.amounts_per_formula_unit.unit, Unitless):
            raise ValueError("amounts_per_formula_unit must be unitless")
        if self.amounts_per_formula_unit.magnitude.shape != (
            len(self.included_species),
        ):
            raise ValueError(
                "amounts_per_formula_unit must have one value per included species"
            )
        if np.any(self.amounts_per_formula_unit.magnitude < 0.0):
            raise ValueError("amounts_per_formula_unit must be nonnegative")
        if float(np.sum(self.amounts_per_formula_unit.magnitude)) <= 0.0:
            raise ValueError("total included amount must be positive")

    def _check_arg_mole_fractions(self) -> None:
        """Require normalized unitless fractions for included species."""
        if not isinstance(self.mole_fractions, VectorQuantity):
            raise TypeError("mole_fractions must be VectorQuantity")
        if not isinstance(self.mole_fractions.unit, Unitless):
            raise ValueError("mole_fractions must be unitless")
        if self.mole_fractions.magnitude.shape != (len(self.included_species),):
            raise ValueError("mole_fractions must have one value per included species")
        if np.any(self.mole_fractions.magnitude < 0.0):
            raise ValueError("mole_fractions must be nonnegative")
        if not np.isclose(
            float(np.sum(self.mole_fractions.magnitude)),
            1.0,
            rtol=0.0,
            atol=_NORMALIZATION_ABSOLUTE_TOLERANCE,
        ):
            raise ValueError("mole_fractions must sum to one")


@dataclass(frozen=True, slots=True)
class SiteFractionOverallCompositionEvaluator:
    """Aggregate multiplicity-weighted site fractions by species."""

    def action(
        self,
        *,
        request: SiteFractionOverallCompositionEvaluationRequest,
    ) -> SiteFractionOverallCompositionEvaluation:
        """Evaluate the included overall amounts and normalized fractions."""
        if not isinstance(
            request,
            SiteFractionOverallCompositionEvaluationRequest,
        ):
            raise TypeError(
                "request must be SiteFractionOverallCompositionEvaluationRequest"
            )
        ordered_species: list[str] = []
        ordered_amounts: list[float] = []
        excluded = set(request.excluded_species)
        for sublattice in request.mixture.sublattices:
            specification = sublattice.specification
            for species_name, fraction in zip(
                specification.species,
                sublattice.fractions.magnitude,
                strict=True,
            ):
                if species_name in excluded:
                    continue
                contribution = specification.multiplicity.magnitude * float(fraction)
                if species_name in ordered_species:
                    index = ordered_species.index(species_name)
                    ordered_amounts[index] += contribution
                else:
                    ordered_species.append(species_name)
                    ordered_amounts.append(contribution)
        amounts = np.asarray(ordered_amounts, dtype=np.float64)
        total = float(np.sum(amounts))
        if total <= 0.0:
            raise ValueError("total included amount must be positive")
        return SiteFractionOverallCompositionEvaluation(
            request=request,
            included_species=tuple(ordered_species),
            amounts_per_formula_unit=VectorQuantity(
                magnitude=amounts,
                unit=Unitless(),
            ),
            mole_fractions=VectorQuantity(
                magnitude=np.asarray(amounts / total, dtype=np.float64),
                unit=Unitless(),
            ),
        )


@dataclass(frozen=True, slots=True, eq=False, kw_only=True)
class SiteFractionMixture(
    ActionizedDataObject[
        SiteFractionOverallCompositionEvaluationRequest,
        SiteFractionOverallCompositionEvaluation,
    ]
):
    """Represent one normalized site-fraction vector per named sublattice."""

    sublattices: tuple[SublatticeSiteFractions, ...]
    actionizer: SiteFractionOverallCompositionEvaluator = field(
        default_factory=SiteFractionOverallCompositionEvaluator,
        init=False,
        repr=False,
        compare=False,
    )

    def __post_init__(self) -> None:
        """Check the complete ordered sublattice collection."""
        self._check_arg_sublattices()

    def _check_arg_sublattices(self) -> None:
        """Require a nonempty tuple with unique sublattice names."""
        if not isinstance(self.sublattices, tuple) or not all(
            isinstance(sublattice, SublatticeSiteFractions)
            for sublattice in self.sublattices
        ):
            raise TypeError("sublattices must be a tuple of SublatticeSiteFractions")
        if not self.sublattices:
            raise ValueError("sublattices must be nonempty")
        names = tuple(sublattice.specification.name for sublattice in self.sublattices)
        if len(set(names)) != len(names):
            raise ValueError("sublattice names must be unique")

    def sublattice(self, *, name: str) -> SublatticeSiteFractions:
        """Return one named sublattice record."""
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        for sublattice in self.sublattices:
            if sublattice.specification.name == name:
                return sublattice
        raise KeyError(f"sublattice {name!r} is absent")

    def evaluate_overall_composition(
        self,
        *,
        excluded_species: tuple[str, ...] = (),
    ) -> SiteFractionOverallCompositionEvaluation:
        """Evaluate multiplicity-weighted composition with explicit exclusions."""
        return self._respond(
            request=SiteFractionOverallCompositionEvaluationRequest(
                mixture=self,
                excluded_species=excluded_species,
            )
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class SiteCountMixtureNormalizationRequest(DataObject):
    """Request conversion of ordered site counts into site fractions."""

    specifications: tuple[SublatticeSpecification, ...]
    site_counts: tuple[VectorQuantity, ...]

    def __post_init__(self) -> None:
        """Check every site-count normalization request argument."""
        self._check_arg_specifications()
        self._check_arg_site_counts()

    def _check_arg_specifications(self) -> None:
        """Require nonempty uniquely named sublattice specifications."""
        if not isinstance(self.specifications, tuple) or not all(
            isinstance(specification, SublatticeSpecification)
            for specification in self.specifications
        ):
            raise TypeError("specifications must be a tuple of SublatticeSpecification")
        if not self.specifications:
            raise ValueError("specifications must be nonempty")
        names = tuple(specification.name for specification in self.specifications)
        if len(set(names)) != len(names):
            raise ValueError("specification names must be unique")

    def _check_arg_site_counts(self) -> None:
        """Require aligned positive-total unitless count vectors."""
        if not isinstance(self.site_counts, tuple) or not all(
            isinstance(counts, VectorQuantity) for counts in self.site_counts
        ):
            raise TypeError("site_counts must be a tuple of VectorQuantity")
        if len(self.site_counts) != len(self.specifications):
            raise ValueError("site_counts must align with specifications")
        for specification, counts in zip(
            self.specifications,
            self.site_counts,
            strict=True,
        ):
            if not isinstance(counts.unit, Unitless):
                raise ValueError("site counts must be unitless")
            if counts.magnitude.shape != (len(specification.species),):
                raise ValueError(
                    f"site counts for {specification.name!r} must align with species"
                )
            if np.any(counts.magnitude < 0.0):
                raise ValueError("site counts must be nonnegative")
            if float(np.sum(counts.magnitude)) <= 0.0:
                raise ValueError("each sublattice site-count total must be positive")


@dataclass(frozen=True, slots=True, eq=False, kw_only=True)
class SiteCountMixtureNormalization(ResultsObject):
    """Retain one count-normalization request and its site-fraction mixture."""

    request: SiteCountMixtureNormalizationRequest
    mixture: SiteFractionMixture

    def __post_init__(self) -> None:
        """Check every count-normalization response argument."""
        self._check_arg_request()
        self._check_arg_mixture()

    def _check_arg_request(self) -> None:
        """Require the complete normalization request."""
        if not isinstance(self.request, SiteCountMixtureNormalizationRequest):
            raise TypeError("request must be SiteCountMixtureNormalizationRequest")

    def _check_arg_mixture(self) -> None:
        """Require one resulting site-fraction mixture."""
        if not isinstance(self.mixture, SiteFractionMixture):
            raise TypeError("mixture must be SiteFractionMixture")


@dataclass(frozen=True, slots=True)
class SiteCountMixtureNormalizer:
    """Normalize ordered nonnegative site counts per sublattice."""

    def action(
        self,
        *,
        request: SiteCountMixtureNormalizationRequest,
    ) -> SiteCountMixtureNormalization:
        """Construct one site-fraction mixture from aligned count vectors."""
        if not isinstance(request, SiteCountMixtureNormalizationRequest):
            raise TypeError("request must be SiteCountMixtureNormalizationRequest")
        sublattices = tuple(
            SublatticeSiteFractions(
                specification=specification,
                fractions=VectorQuantity(
                    magnitude=np.asarray(
                        counts.magnitude / float(np.sum(counts.magnitude)),
                        dtype=np.float64,
                    ),
                    unit=Unitless(),
                ),
            )
            for specification, counts in zip(
                request.specifications,
                request.site_counts,
                strict=True,
            )
        )
        return SiteCountMixtureNormalization(
            request=request,
            mixture=SiteFractionMixture(sublattices=sublattices),
        )
