"""Finite-difference TISE solution of the one-dimensional particle in a box.

The represented grid, Hamiltonian, discrete spectrum, and evaluation behavior
are adapted from ``ksdft2effmass`` particle-in-box model and evaluation modules
at commit ``7bd913151f7e61ed2bdba593df920be36573b502``.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from physkit.core.results import ResultsObject
from physkit.discretization.boundary_conditions import DirichletBoundaryCondition
from physkit.discretization.cartesian_grids import UniformCartesianGrid1D
from physkit.discretization.intervals import DirichletInterval
from physkit.numerics.eigenproblems.real_symmetric import (
    RealSymmetricEigenpairResult,
    RealSymmetricEigenpairSolver,
)
from physkit.operators.operators_1d import (
    SecondOrderCentralDifferenceLaplacian1D,
)
from physkit.operators.qm import (
    FiniteDifferenceHamiltonian1D,
    SampledPotential1D,
    TiseKineticEnergy1D,
)
from physkit.units import (
    MODEL_SYSTEM_UNIT_CONVERTER,
    MatrixQuantity,
    PhysicalUnit,
    ScalarQuantity,
    SparseMatrixQuantity,
    Unitless,
    VectorQuantity,
)

from ..base import Piab1D


@dataclass(frozen=True, slots=True, eq=False)
class Piab1dTiseFdResults(ResultsObject):
    """Retain one correlated PIAB1D finite-difference solution."""

    model: Piab1D
    interval: DirichletInterval
    hamiltonian: SparseMatrixQuantity
    eigenpairs: RealSymmetricEigenpairResult

    def __post_init__(self) -> None:
        if not isinstance(self.model, Piab1D):
            raise TypeError("model must be Piab1D")
        if not isinstance(self.interval, DirichletInterval):
            raise TypeError("interval must be DirichletInterval")
        if not isinstance(self.hamiltonian, SparseMatrixQuantity):
            raise TypeError("hamiltonian must be SparseMatrixQuantity")
        if not isinstance(self.eigenpairs, RealSymmetricEigenpairResult):
            raise TypeError(
                "eigenpairs must be RealSymmetricEigenpairResult"
            )
        points = self.interval.interior_points
        if self.hamiltonian.shape != (points, points):
            raise ValueError("hamiltonian must match the interval dimension")
        if self.hamiltonian.unit != self.model.unit_system.energy_unit:
            raise ValueError("hamiltonian must use the model energy unit")
        if self.eigenpairs.eigenvalues.shape != (points,):
            raise ValueError("eigenvalues must match the Hamiltonian dimension")
        if self.eigenpairs.eigenvectors.shape != (points, points):
            raise ValueError("eigenvectors must match the Hamiltonian dimension")

    @property
    def interior_points(self) -> int:
        """Return the finite coordinate-space dimension."""
        return self.interval.interior_points

    @property
    def grid_spacing(self) -> ScalarQuantity:
        """Return the spacing in the selected length unit."""
        return self.interval.grid.spacing

    @property
    def energies(self) -> VectorQuantity:
        """Return the ordered finite-difference energy eigenvalues."""
        return VectorQuantity(
            self.eigenpairs.eigenvalues,
            self.model.unit_system.energy_unit,
        )

    @property
    def eigenvectors(self) -> MatrixQuantity:
        """Return the ordered column eigenvectors."""
        return MatrixQuantity(self.eigenpairs.eigenvectors, Unitless())

    def closed_form_discrete_energies(self) -> VectorQuantity:
        """Return the exact spectrum of the represented tridiagonal matrix."""
        points = self.interior_points
        indices = np.arange(1, points + 1, dtype=np.float64)
        hbar = self.model.hbar_quantity
        mass = self.model.mass_quantity
        spacing = self.grid_spacing
        energies = (
            2.0
            * hbar.magnitude**2
            / (mass.magnitude * spacing.magnitude**2)
            * np.sin(indices * np.pi / (2.0 * (points + 1))) ** 2
        )
        if isinstance(self.model.unit_system.energy_unit, Unitless):
            energy_unit: PhysicalUnit | Unitless = Unitless()
        else:
            if not isinstance(hbar.unit, PhysicalUnit):
                raise TypeError("physical model requires physical action units")
            if not isinstance(mass.unit, PhysicalUnit):
                raise TypeError("physical model requires physical mass units")
            if not isinstance(spacing.unit, PhysicalUnit):
                raise TypeError("physical model requires physical length units")
            source_unit = PhysicalUnit(
                f"({hbar.unit.expression}) ** 2 / "
                f"({mass.unit.expression}) / "
                f"({spacing.unit.expression}) ** 2"
            )
            energy_unit = self.model.unit_system.energy_unit
            energies *= MODEL_SYSTEM_UNIT_CONVERTER.conversion_factor(
                source_unit,
                energy_unit,
            )
        return VectorQuantity(energies, energy_unit)


class Piab1dTiseFdSolver:
    """Solve the ``Piab1D`` TISE with finite-difference machinery."""

    __slots__ = ("eigenpair_solver",)

    def __init__(
        self,
        eigenpair_solver: RealSymmetricEigenpairSolver | None = None,
    ) -> None:
        if eigenpair_solver is not None and not isinstance(
            eigenpair_solver,
            RealSymmetricEigenpairSolver,
        ):
            raise TypeError(
                "eigenpair_solver must be "
                "RealSymmetricEigenpairSolver or None"
            )
        self.eigenpair_solver = (
            eigenpair_solver or RealSymmetricEigenpairSolver()
        )

    def solve(
        self,
        model: Piab1D,
        interior_points: int,
    ) -> Piab1dTiseFdResults:
        """Construct and solve one selected-scale finite representation."""
        if not isinstance(model, Piab1D):
            raise TypeError("model must be Piab1D")
        if type(interior_points) is not int:
            raise TypeError("interior_points must be a built-in int")
        if interior_points <= 0:
            raise ValueError("interior_points must be positive")
        length = model.length_quantity
        spacing = ScalarQuantity(
            length.magnitude / (interior_points + 1),
            length.unit,
        )
        grid = UniformCartesianGrid1D(
            ScalarQuantity(0.0, length.unit),
            length,
            spacing,
        )
        if isinstance(length.unit, Unitless):
            boundary_unit: PhysicalUnit | Unitless = Unitless()
        else:
            boundary_unit = PhysicalUnit(
                f"({length.unit.expression}) ** -0.5"
            )
        interval = DirichletInterval(
            grid,
            DirichletBoundaryCondition(
                ScalarQuantity(0.0, boundary_unit)
            ),
        )
        laplacian = SecondOrderCentralDifferenceLaplacian1D(interval)
        kinetic = TiseKineticEnergy1D(
            laplacian=laplacian,
            hbar=model.hbar_quantity,
            mass=model.mass_quantity,
            energy_unit=model.unit_system.energy_unit,
        )
        potential = SampledPotential1D(
            grid=grid,
            values=VectorQuantity(
                np.zeros(interior_points, dtype=np.float64),
                model.unit_system.energy_unit,
            ),
        )
        hamiltonian = FiniteDifferenceHamiltonian1D(
            kinetic,
            potential,
        ).matrix()
        eigenpairs = self.eigenpair_solver.execute(hamiltonian.to_csr())
        return Piab1dTiseFdResults(
            model=model,
            interval=interval,
            hamiltonian=hamiltonian,
            eigenpairs=eigenpairs,
        )
