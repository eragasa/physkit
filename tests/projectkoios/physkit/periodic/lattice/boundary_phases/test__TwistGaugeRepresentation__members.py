"""Tests for finite-lattice twist gauges."""

from projectkoios.physkit.periodic.lattice.boundary_phases import (
    TwistGaugeRepresentation,
)


def test_declares_uniform_link_and_quotient_seam_gauges() -> None:
    assert tuple(TwistGaugeRepresentation) == (
        TwistGaugeRepresentation.CENTERED_UNIFORM_LINK,
        TwistGaugeRepresentation.QUOTIENT_SEAM,
    )
