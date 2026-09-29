"""Shared dimensionless parameters for periodic Cahn--Hilliard models."""

from dataclasses import dataclass

from projectkoios.physkit.core.data import DataObject
from projectkoios.physkit.units import ScalarQuantity, Unitless


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionlessCahnHilliardParameters(DataObject):
    """Represent positive reduced mobility, gradient penalty, and time step."""

    mobility: ScalarQuantity
    gradient_penalty: ScalarQuantity
    time_step: ScalarQuantity

    def __post_init__(self) -> None:
        """Check every dimensionless Cahn--Hilliard parameter."""
        self._check_arg_mobility()
        self._check_arg_gradient_penalty()
        self._check_arg_time_step()

    def _check_arg_mobility(self) -> None:
        """Require a positive unitless mobility."""
        self._check_positive_unitless(
            quantity=self.mobility,
            argument_name="mobility",
        )

    def _check_arg_gradient_penalty(self) -> None:
        """Require a positive unitless gradient penalty."""
        self._check_positive_unitless(
            quantity=self.gradient_penalty,
            argument_name="gradient_penalty",
        )

    def _check_arg_time_step(self) -> None:
        """Require a positive unitless time step."""
        self._check_positive_unitless(
            quantity=self.time_step,
            argument_name="time_step",
        )

    @staticmethod
    def _check_positive_unitless(
        *,
        quantity: ScalarQuantity,
        argument_name: str,
    ) -> None:
        """Apply repeated mechanical reduced-parameter checks."""
        if not isinstance(quantity, ScalarQuantity):
            raise TypeError(f"{argument_name} must be ScalarQuantity")
        if not isinstance(quantity.unit, Unitless):
            raise ValueError(f"{argument_name} must be unitless")
        if quantity.magnitude <= 0.0:
            raise ValueError(f"{argument_name} must be positive")
