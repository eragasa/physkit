"""Software verification for normalization of sublattice site counts."""

import numpy as np

from projectkoios.physkit.materials.mixtures.sublattice import (
    SiteCountMixtureNormalizationRequest,
    SiteCountMixtureNormalizer,
    SublatticeSpecification,
)
from projectkoios.physkit.units import ScalarQuantity, Unitless, VectorQuantity


class TestSiteCountMixtureNormalizer:
    """Verify conversion of ordered counts to immutable site fractions."""

    def test_action_normalizes_each_sublattice_independently(self) -> None:
        """Each sublattice is one simplex rather than one global simplex."""
        specifications = (
            SublatticeSpecification(
                name="alpha",
                species=("A", "B"),
                multiplicity=ScalarQuantity(magnitude=1.0, unit=Unitless()),
            ),
            SublatticeSpecification(
                name="beta",
                species=("A", "B"),
                multiplicity=ScalarQuantity(magnitude=2.0, unit=Unitless()),
            ),
        )
        request = SiteCountMixtureNormalizationRequest(
            specifications=specifications,
            site_counts=(
                VectorQuantity(
                    magnitude=np.asarray([3.0, 1.0], dtype=np.float64),
                    unit=Unitless(),
                ),
                VectorQuantity(
                    magnitude=np.asarray([2.0, 6.0], dtype=np.float64),
                    unit=Unitless(),
                ),
            ),
        )

        result = SiteCountMixtureNormalizer().action(request=request)

        assert np.array_equal(
            result.mixture.sublattices[0].fractions.magnitude,
            np.asarray([0.75, 0.25], dtype=np.float64),
        )
        assert np.array_equal(
            result.mixture.sublattices[1].fractions.magnitude,
            np.asarray([0.25, 0.75], dtype=np.float64),
        )
        assert result.request is request
