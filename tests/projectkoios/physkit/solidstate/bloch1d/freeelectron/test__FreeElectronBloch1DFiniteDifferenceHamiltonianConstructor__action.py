"""Verification for represented free-electron Bloch Hamiltonians."""

import numpy as np

from projectkoios.physkit.solidstate.bloch1d.cell import (
    BlochPrimitiveCell1D,
)
from projectkoios.physkit.solidstate.bloch1d.freeelectron.finite_difference import (
    FreeElectronBloch1DFiniteDifferenceHamiltonianConstructor,
    FreeElectronBloch1DFiniteDifferenceHamiltonianRequest,
)
from projectkoios.physkit.solidstate.bloch1d.freeelectron.model import (
    FreeElectronBloch1D,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, UnitSystem


class TestFreeElectronBloch1DFiniteDifferenceHamiltonianConstructor:
    """Verify Hermiticity, units, and continuum convergence."""

    @staticmethod
    def _model() -> FreeElectronBloch1D:
        return FreeElectronBloch1D(
            cell=BlochPrimitiveCell1D(
                oriented_length=ScalarQuantity(
                    5.4,
                    UnitSystem.METAL.length_unit,
                ),
                unit_system=UnitSystem.METAL,
            )
        )

    @classmethod
    def _lowest_energy(cls, *, point_count: int, wave_number: float) -> float:
        result = FreeElectronBloch1DFiniteDifferenceHamiltonianConstructor().action(
            request=FreeElectronBloch1DFiniteDifferenceHamiltonianRequest(
                model=cls._model(),
                point_count=point_count,
                bloch_wave_number=ScalarQuantity(
                    wave_number,
                    PhysicalUnit("1 / angstrom"),
                ),
            )
        )
        matrix = result.represented_hamiltonian.to_csr().toarray()
        return float(np.linalg.eigvalsh(matrix)[0])

    def test_represented_hamiltonian_is_hermitian_and_uses_electron_volts(
        self,
    ) -> None:
        result = FreeElectronBloch1DFiniteDifferenceHamiltonianConstructor().action(
            request=FreeElectronBloch1DFiniteDifferenceHamiltonianRequest(
                model=self._model(),
                point_count=24,
                bloch_wave_number=ScalarQuantity(
                    0.17,
                    PhysicalUnit("1 / angstrom"),
                ),
            )
        )
        matrix = result.represented_hamiltonian.to_csr().toarray()

        np.testing.assert_allclose(matrix, matrix.conjugate().T)
        assert result.represented_hamiltonian.unit == PhysicalUnit("electron_volt")

    def test_lowest_band_converges_quadratically_to_exact_bloch_energy(self) -> None:
        wave_number = 0.17
        model = self._model()
        exact = model.evaluate_modes(
            mode_indices=((0,),),
            bloch_wave_number=ScalarQuantity(
                wave_number,
                PhysicalUnit("1 / angstrom"),
            ),
        ).energies.magnitude[0]

        coarse_error = abs(
            self._lowest_energy(point_count=24, wave_number=wave_number) - exact
        )
        fine_error = abs(
            self._lowest_energy(point_count=48, wave_number=wave_number) - exact
        )

        assert fine_error < coarse_error
        np.testing.assert_allclose(coarse_error / fine_error, 4.0, rtol=0.02)
