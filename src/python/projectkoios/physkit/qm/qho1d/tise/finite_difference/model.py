r"""Dimensionless finite-difference stationary quantum harmonic oscillator."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.linalg import eigh

from projectkoios.physkit.core.actions import ActionizedDataObject
from projectkoios.physkit.core.data import DataObject
from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.units import (
    MatrixQuantity,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionlessQho1DTiseFdSolveRequest(DataObject):
    """Request one bounded finite-difference representation of a QHO1D."""

    model: DimensionlessQho1D
    lower_bound: ScalarQuantity
    upper_bound: ScalarQuantity
    point_count: int

    def __post_init__(self) -> None:
        """Check every finite-difference solve request argument."""
        self._check_arg_model()
        self._check_arg_lower_bound()
        self._check_arg_upper_bound()
        self._check_arg_point_count()
        if self.upper_bound.magnitude <= self.lower_bound.magnitude:
            raise ValueError("upper_bound must be greater than lower_bound")

    def _check_arg_model(self) -> None:
        """Require the dimensionless QHO1D model."""
        if not isinstance(self.model, DimensionlessQho1D):
            raise TypeError("model must be DimensionlessQho1D")

    def _check_arg_lower_bound(self) -> None:
        """Require a unitless lower coordinate."""
        self._check_unitless_coordinate(
            coordinate=self.lower_bound,
            argument_name="lower_bound",
        )

    def _check_arg_upper_bound(self) -> None:
        """Require a unitless upper coordinate."""
        self._check_unitless_coordinate(
            coordinate=self.upper_bound,
            argument_name="upper_bound",
        )

    @staticmethod
    def _check_unitless_coordinate(
        *,
        coordinate: ScalarQuantity,
        argument_name: str,
    ) -> None:
        """Apply repeated mechanical reduced-coordinate checks."""
        if not isinstance(coordinate, ScalarQuantity):
            raise TypeError(f"{argument_name} must be ScalarQuantity")
        if not isinstance(coordinate.unit, Unitless):
            raise ValueError(f"{argument_name} must be unitless")

    def _check_arg_point_count(self) -> None:
        """Require enough built-in integer points for an interior operator."""
        if type(self.point_count) is not int:
            raise TypeError("point_count must be a built-in int")
        if self.point_count < 5:
            raise ValueError("point_count must be at least five")


@dataclass(frozen=True, slots=True, eq=False, kw_only=True)
class DimensionlessQho1DTiseFdSolution(ResultsObject):
    """Retain a finite QHO1D representation and its complete eigensystem."""

    request: DimensionlessQho1DTiseFdSolveRequest
    coordinates: VectorQuantity
    energies: VectorQuantity
    eigenfunctions: MatrixQuantity
    potential_energy: VectorQuantity
    hamiltonian: MatrixQuantity

    def __post_init__(self) -> None:
        """Check every finite-difference solution argument."""
        self._check_arg_request()
        self._check_arg_coordinates()
        self._check_arg_energies()
        self._check_arg_eigenfunctions()
        self._check_arg_potential_energy()
        self._check_arg_hamiltonian()

    @property
    def interior_point_count(self) -> int:
        """Return the represented coordinate-space dimension."""
        return self.request.point_count - 2

    @property
    def grid_spacing(self) -> ScalarQuantity:
        """Return the uniform reduced spacing including boundary intervals."""
        return ScalarQuantity(
            magnitude=(
                self.request.upper_bound.magnitude - self.request.lower_bound.magnitude
            )
            / (self.request.point_count - 1),
            unit=Unitless(),
        )

    def _check_arg_request(self) -> None:
        """Require the complete solve request."""
        if not isinstance(self.request, DimensionlessQho1DTiseFdSolveRequest):
            raise TypeError("request must be DimensionlessQho1DTiseFdSolveRequest")

    def _check_arg_coordinates(self) -> None:
        """Require one unitless coordinate per interior point."""
        self._check_vector(
            vector=self.coordinates,
            argument_name="coordinates",
        )

    def _check_arg_energies(self) -> None:
        """Require one ordered unitless energy per represented state."""
        self._check_vector(vector=self.energies, argument_name="energies")
        if np.any(self.energies.magnitude[1:] < self.energies.magnitude[:-1]):
            raise ValueError("energies must be nondecreasing")

    def _check_arg_eigenfunctions(self) -> None:
        """Require square unitless eigenfunction columns on the interior grid."""
        if not isinstance(self.eigenfunctions, MatrixQuantity):
            raise TypeError("eigenfunctions must be MatrixQuantity")
        if not isinstance(self.eigenfunctions.unit, Unitless):
            raise ValueError("eigenfunctions must be unitless")
        expected = (self.interior_point_count, self.interior_point_count)
        if self.eigenfunctions.magnitude.shape != expected:
            raise ValueError("eigenfunctions must match the interior dimension")

    def _check_arg_potential_energy(self) -> None:
        """Require one unitless potential value per interior point."""
        self._check_vector(
            vector=self.potential_energy,
            argument_name="potential_energy",
        )

    def _check_arg_hamiltonian(self) -> None:
        """Require a square unitless Hamiltonian on the interior grid."""
        if not isinstance(self.hamiltonian, MatrixQuantity):
            raise TypeError("hamiltonian must be MatrixQuantity")
        if not isinstance(self.hamiltonian.unit, Unitless):
            raise ValueError("hamiltonian must be unitless")
        expected = (self.interior_point_count, self.interior_point_count)
        if self.hamiltonian.magnitude.shape != expected:
            raise ValueError("hamiltonian must match the interior dimension")

    def _check_vector(
        self,
        *,
        vector: VectorQuantity,
        argument_name: str,
    ) -> None:
        """Apply repeated mechanical represented-vector checks."""
        if not isinstance(vector, VectorQuantity):
            raise TypeError(f"{argument_name} must be VectorQuantity")
        if not isinstance(vector.unit, Unitless):
            raise ValueError(f"{argument_name} must be unitless")
        if vector.magnitude.shape != (self.interior_point_count,):
            raise ValueError(f"{argument_name} must match the interior dimension")


@dataclass(frozen=True, slots=True)
class DimensionlessQho1DTiseFdSolver:
    """Build and diagonalize a centered-difference QHO1D Hamiltonian."""

    def action(
        self,
        *,
        request: DimensionlessQho1DTiseFdSolveRequest,
    ) -> DimensionlessQho1DTiseFdSolution:
        """Solve the bounded homogeneous-Dirichlet matrix eigenproblem."""
        if not isinstance(request, DimensionlessQho1DTiseFdSolveRequest):
            raise TypeError("request must be DimensionlessQho1DTiseFdSolveRequest")
        full_coordinates = np.linspace(
            request.lower_bound.magnitude,
            request.upper_bound.magnitude,
            request.point_count,
            dtype=np.float64,
        )
        coordinates = full_coordinates[1:-1]
        spacing = full_coordinates[1] - full_coordinates[0]
        interior_point_count = coordinates.size
        main_diagonal = -2.0 * np.ones(interior_point_count, dtype=np.float64)
        off_diagonal = np.ones(interior_point_count - 1, dtype=np.float64)
        laplacian = (
            np.diag(main_diagonal)
            + np.diag(off_diagonal, k=1)
            + np.diag(off_diagonal, k=-1)
        ) / spacing**2
        kinetic_energy = (
            -(request.model.hbar.magnitude**2)
            / (2.0 * request.model.mass.magnitude)
            * laplacian
        )
        potential_energy = (
            0.5
            * request.model.mass.magnitude
            * request.model.angular_frequency.magnitude**2
            * coordinates**2
        )
        hamiltonian = kinetic_energy + np.diag(potential_energy)
        energies, eigenvectors = eigh(hamiltonian)
        eigenfunctions = np.asarray(
            eigenvectors / np.sqrt(spacing),
            dtype=np.float64,
        )
        return DimensionlessQho1DTiseFdSolution(
            request=request,
            coordinates=VectorQuantity(
                magnitude=coordinates,
                unit=Unitless(),
            ),
            energies=VectorQuantity(magnitude=energies, unit=Unitless()),
            eigenfunctions=MatrixQuantity(
                magnitude=eigenfunctions,
                unit=Unitless(),
            ),
            potential_energy=VectorQuantity(
                magnitude=potential_energy,
                unit=Unitless(),
            ),
            hamiltonian=MatrixQuantity(
                magnitude=hamiltonian,
                unit=Unitless(),
            ),
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionlessQho1D(
    ActionizedDataObject[
        DimensionlessQho1DTiseFdSolveRequest,
        DimensionlessQho1DTiseFdSolution,
    ]
):
    """Represent a reduced one-dimensional quantum harmonic oscillator."""

    mass: ScalarQuantity
    angular_frequency: ScalarQuantity
    hbar: ScalarQuantity
    actionizer: DimensionlessQho1DTiseFdSolver = field(
        default_factory=DimensionlessQho1DTiseFdSolver,
        init=False,
        repr=False,
        compare=False,
    )

    def __post_init__(self) -> None:
        """Check every reduced physical parameter."""
        self._check_arg_mass()
        self._check_arg_angular_frequency()
        self._check_arg_hbar()

    def _check_arg_mass(self) -> None:
        """Require a positive unitless reduced mass."""
        self._check_positive_unitless_parameter(
            parameter=self.mass,
            argument_name="mass",
        )

    def _check_arg_angular_frequency(self) -> None:
        """Require a positive unitless reduced angular frequency."""
        self._check_positive_unitless_parameter(
            parameter=self.angular_frequency,
            argument_name="angular_frequency",
        )

    def _check_arg_hbar(self) -> None:
        """Require a positive unitless reduced Planck constant."""
        self._check_positive_unitless_parameter(
            parameter=self.hbar,
            argument_name="hbar",
        )

    @staticmethod
    def _check_positive_unitless_parameter(
        *,
        parameter: ScalarQuantity,
        argument_name: str,
    ) -> None:
        """Apply repeated mechanical reduced-parameter checks."""
        if not isinstance(parameter, ScalarQuantity):
            raise TypeError(f"{argument_name} must be ScalarQuantity")
        if not isinstance(parameter.unit, Unitless):
            raise ValueError(f"{argument_name} must be unitless")
        if parameter.magnitude <= 0.0:
            raise ValueError(f"{argument_name} must be positive")

    def analytical_energies(self, *, count: int) -> VectorQuantity:
        """Return the first exact reduced harmonic-oscillator energies."""
        if type(count) is not int:
            raise TypeError("count must be a built-in int")
        if count <= 0:
            raise ValueError("count must be positive")
        quantum_numbers = np.arange(count, dtype=np.float64)
        return VectorQuantity(
            magnitude=(
                self.hbar.magnitude
                * self.angular_frequency.magnitude
                * (quantum_numbers + 0.5)
            ),
            unit=Unitless(),
        )

    def solve_tise_finite_difference(
        self,
        *,
        lower_bound: ScalarQuantity,
        upper_bound: ScalarQuantity,
        point_count: int,
    ) -> DimensionlessQho1DTiseFdSolution:
        """Solve one bounded finite-difference representation."""
        return self._respond(
            request=DimensionlessQho1DTiseFdSolveRequest(
                model=self,
                lower_bound=lower_bound,
                upper_bound=upper_bound,
                point_count=point_count,
            )
        )
