"""Numerical verification for one-dimensional cosine-potential Bloch bands."""

import numpy as np

from projectkoios.physkit.solidstate.bloch1d.cell import BlochPrimitiveCell1D
from projectkoios.physkit.solidstate.bloch1d.cosinepotential.model import (
    CosinePotentialBloch1D,
)
from projectkoios.physkit.solidstate.bloch1d.freeelectron.finite_difference import (
    FreeElectronBloch1DFiniteDifferenceHamiltonianConstructor,
    FreeElectronBloch1DFiniteDifferenceHamiltonianRequest,
)
from projectkoios.physkit.solidstate.bloch1d.freeelectron.model import (
    FreeElectronBloch1D,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    UnitSystem,
    VectorQuantity,
)


class TestCosinePotentialBloch1D:
    """Verify represented limits, periodicity, and first-gap behavior."""

    @staticmethod
    def _cell() -> BlochPrimitiveCell1D:
        return BlochPrimitiveCell1D(
            oriented_length=ScalarQuantity(10.0, UnitSystem.METAL.length_unit),
            unit_system=UnitSystem.METAL,
        )

    @classmethod
    def _model(cls, *, amplitude: float) -> CosinePotentialBloch1D:
        return CosinePotentialBloch1D(
            cell=cls._cell(),
            amplitude=ScalarQuantity(
                amplitude,
                UnitSystem.METAL.energy_unit,
            ),
        )

    def test_zero_amplitude_matches_the_free_electron_represented_operator(
        self,
    ) -> None:
        wave_number = 0.17
        point_count = 32
        model = self._model(amplitude=0.0)

        result = model.solve_bands(
            bloch_wave_numbers=VectorQuantity(
                np.array([wave_number]),
                PhysicalUnit("1 / angstrom"),
            ),
            point_count=point_count,
            band_count=5,
        )
        free_result = (
            FreeElectronBloch1DFiniteDifferenceHamiltonianConstructor().action(
                request=FreeElectronBloch1DFiniteDifferenceHamiltonianRequest(
                    model=FreeElectronBloch1D(cell=self._cell()),
                    point_count=point_count,
                    bloch_wave_number=ScalarQuantity(
                        wave_number,
                        PhysicalUnit("1 / angstrom"),
                    ),
                )
            )
        )
        expected = np.linalg.eigvalsh(
            free_result.represented_hamiltonian.to_csr().toarray()
        )[:5]

        np.testing.assert_allclose(result.energies.magnitude[0], expected)

    def test_brillouin_zone_endpoints_have_equal_spectra(self) -> None:
        model = self._model(amplitude=0.4)
        zone_edge = np.pi / model.cell.length.magnitude

        result = model.solve_bands(
            bloch_wave_numbers=VectorQuantity(
                np.array([-zone_edge, zone_edge]),
                PhysicalUnit("1 / angstrom"),
            ),
            point_count=48,
            band_count=6,
        )

        np.testing.assert_allclose(
            result.energies.magnitude[0],
            result.energies.magnitude[1],
            rtol=2e-14,
            atol=2e-14,
        )

    def test_weak_cosine_potential_opens_the_expected_first_gap(self) -> None:
        amplitude = 0.2
        model = self._model(amplitude=amplitude)
        zone_edge = np.pi / model.cell.length.magnitude

        result = model.solve_bands(
            bloch_wave_numbers=VectorQuantity(
                np.array([zone_edge]),
                PhysicalUnit("1 / angstrom"),
            ),
            point_count=96,
            band_count=2,
        )
        gap = result.energies.magnitude[0, 1] - result.energies.magnitude[0, 0]

        np.testing.assert_allclose(gap, amplitude, rtol=0.01)

    def test_reversing_cosine_amplitude_preserves_the_spectrum(self) -> None:
        wave_numbers = VectorQuantity(
            np.array([-0.2, 0.0, 0.19]),
            PhysicalUnit("1 / angstrom"),
        )

        positive = self._model(amplitude=0.5).solve_bands(
            bloch_wave_numbers=wave_numbers,
            point_count=48,
            band_count=6,
        )
        negative = self._model(amplitude=-0.5).solve_bands(
            bloch_wave_numbers=wave_numbers,
            point_count=48,
            band_count=6,
        )

        np.testing.assert_allclose(
            positive.energies.magnitude,
            negative.energies.magnitude,
            rtol=2e-13,
            atol=2e-13,
        )
