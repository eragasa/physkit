import numpy as np
import pytest

from .lattice import Lattice1D, Lattice2D, Lattice3D

class LatticeContract:
    """
    Shared tests for all direct Bravais lattices.
    """

    vectors = None
    index = None

    def make_lattice(self):
        raise NotImplementedError

    def test_dimension(self):
        lat = self.make_lattice()

        assert lat.dim == len(self.vectors)

    def test_A_stores_primitive_vectors_as_columns(self):
        lat = self.make_lattice()

        expected_A = np.column_stack(self.vectors)

        np.testing.assert_allclose(lat.A, expected_A)

    def test_lengths(self):
        lat = self.make_lattice()

        expected_lengths = np.array([
            np.linalg.norm(v) for v in self.vectors
        ])

        np.testing.assert_allclose(lat.lengths, expected_lengths)

    def test_omega(self):
        lat = self.make_lattice()

        expected_omega = abs(np.linalg.det(np.column_stack(self.vectors)))

        assert lat.omega == pytest.approx(expected_omega)

    def test_get_R_matches_matrix_product(self):
        lat = self.make_lattice()

        np.testing.assert_allclose(
            lat.get_R(self.index),
            lat.A @ self.index,
        )

    def test_get_R_matches_linear_combination(self):
        lat = self.make_lattice()

        expected_R = sum(
            n_i * a_i for n_i, a_i in zip(self.index, self.vectors)
        )

        np.testing.assert_allclose(lat.get_R(self.index), expected_R)

    def test_get_R_rejects_wrong_index_shape(self):
        lat = self.make_lattice()

        wrong_index = np.ones(lat.dim + 1, dtype=int)

        with pytest.raises(ValueError, match="Expected index shape"):
            lat.get_R(wrong_index)


class ReciprocalLatticeContract:
    """
    Shared tests for lattices with reciprocal-lattice support.
    """

    index = None

    def make_lattice(self):
        raise NotImplementedError

    def test_reciprocal_duality_condition(self):
        lat = self.make_lattice()

        expected = 2.0 * np.pi * np.eye(lat.dim)

        np.testing.assert_allclose(lat.A.T @ lat.B, expected)

    def test_get_G_matches_matrix_product(self):
        lat = self.make_lattice()

        np.testing.assert_allclose(
            lat.get_G(self.index),
            lat.B @ self.index,
        )

    def test_get_G_rejects_wrong_index_shape(self):
        lat = self.make_lattice()

        wrong_index = np.ones(lat.dim + 1, dtype=int)

        with pytest.raises(ValueError, match="Expected index shape"):
            lat.get_G(wrong_index)


class TestLattice1D(LatticeContract, ReciprocalLatticeContract):
    vectors = [
        np.array([2.5]),
    ]

    index = np.array([4])

    def make_lattice(self):
        return Lattice1D(a=2.5)

    def test_default_lattice(self):
        lat = Lattice1D()

        np.testing.assert_allclose(lat.a1, np.array([1.0]))
        np.testing.assert_allclose(lat.A, np.array([[1.0]]))

        assert lat.dim == 1
        assert lat.omega == pytest.approx(1.0)

    def test_a1_accessor(self):
        lat = self.make_lattice()

        np.testing.assert_allclose(lat.a1, np.array([2.5]))

    def test_a_scalar_accessor(self):
        lat = self.make_lattice()

        assert lat.a == pytest.approx(2.5)

    def test_length_cell_alias(self):
        lat = self.make_lattice()

        assert lat.length_cell == pytest.approx(lat.omega)

    def test_rejects_zero_lattice_constant(self):
        with pytest.raises(ValueError, match="nonzero|linearly dependent"):
            Lattice1D(a=0.0)


class TestLattice2D(LatticeContract, ReciprocalLatticeContract):
    vectors = [
        np.array([2.0, 1.0]),
        np.array([1.0, 3.0]),
    ]

    index = np.array([4, -2])

    def make_lattice(self):
        return Lattice2D(
            a1=self.vectors[0],
            a2=self.vectors[1],
        )

    def test_default_lattice(self):
        lat = Lattice2D()

        np.testing.assert_allclose(lat.a1, np.array([1.0, 0.0]))
        np.testing.assert_allclose(lat.a2, np.array([0.0, 1.0]))
        np.testing.assert_allclose(lat.A, np.eye(2))

        assert lat.dim == 2
        assert lat.area == pytest.approx(1.0)
        assert lat.omega == pytest.approx(1.0)

    def test_a1_accessor(self):
        lat = self.make_lattice()

        np.testing.assert_allclose(lat.a1, self.vectors[0])

    def test_a2_accessor(self):
        lat = self.make_lattice()

        np.testing.assert_allclose(lat.a2, self.vectors[1])

    def test_area_alias(self):
        lat = self.make_lattice()

        assert lat.area == pytest.approx(lat.omega)

    def test_rejects_linearly_dependent_vectors(self):
        with pytest.raises(ValueError, match="linearly dependent"):
            Lattice2D(
                a1=np.array([1.0, 0.0]),
                a2=np.array([2.0, 0.0]),
            )

    def test_rejects_wrong_a1_shape(self):
        with pytest.raises(ValueError, match="Expected vector shape"):
            Lattice2D(
                a1=np.array([1.0, 0.0, 0.0]),
                a2=np.array([0.0, 1.0]),
            )

    def test_rejects_wrong_a2_shape(self):
        with pytest.raises(ValueError, match="Expected vector shape"):
            Lattice2D(
                a1=np.array([1.0, 0.0]),
                a2=np.array([0.0, 1.0, 0.0]),
            )

class TestLattice3D(LatticeContract, ReciprocalLatticeContract):
    vectors = [
        np.array([2.0, 0.0, 0.0]),
        np.array([0.5, 3.0, 0.0]),
        np.array([1.0, 0.25, 4.0]),
    ]

    index = np.array([2, -1, 3])

    def make_lattice(self):
        return Lattice3D(
            a1=self.vectors[0],
            a2=self.vectors[1],
            a3=self.vectors[2],
        )

    def test_default_lattice(self):
        lat = Lattice3D()

        np.testing.assert_allclose(lat.a1, np.array([1.0, 0.0, 0.0]))
        np.testing.assert_allclose(lat.a2, np.array([0.0, 1.0, 0.0]))
        np.testing.assert_allclose(lat.a3, np.array([0.0, 0.0, 1.0]))
        np.testing.assert_allclose(lat.A, np.eye(3))

        assert lat.dim == 3
        assert lat.volume == pytest.approx(1.0)
        assert lat.omega == pytest.approx(1.0)

    def test_a1_accessor(self):
        lat = self.make_lattice()

        np.testing.assert_allclose(lat.a1, self.vectors[0])

    def test_a2_accessor(self):
        lat = self.make_lattice()

        np.testing.assert_allclose(lat.a2, self.vectors[1])

    def test_a3_accessor(self):
        lat = self.make_lattice()

        np.testing.assert_allclose(lat.a3, self.vectors[2])

    def test_a1_length(self):
        lat = self.make_lattice()

        assert lat.a1_length == pytest.approx(np.linalg.norm(self.vectors[0]))

    def test_a2_length(self):
        lat = self.make_lattice()

        assert lat.a2_length == pytest.approx(np.linalg.norm(self.vectors[1]))

    def test_a3_length(self):
        lat = self.make_lattice()

        assert lat.a3_length == pytest.approx(np.linalg.norm(self.vectors[2]))

    def test_volume_alias(self):
        lat = self.make_lattice()

        assert lat.volume == pytest.approx(lat.omega)

    def test_volume_matches_triple_product(self):
        lat = self.make_lattice()

        expected_volume = abs(
            np.dot(
                self.vectors[0],
                np.cross(self.vectors[1], self.vectors[2]),
            )
        )

        assert lat.volume == pytest.approx(expected_volume)
        assert lat.omega == pytest.approx(expected_volume)

    def test_get_R_for_oblique_3d_lattice(self):
        lat = self.make_lattice()

        n1, n2, n3 = self.index

        expected_R = (
            n1 * lat.a1
            + n2 * lat.a2
            + n3 * lat.a3
        )

        np.testing.assert_allclose(lat.get_R(self.index), expected_R)

    def test_rejects_linearly_dependent_vectors(self):
        with pytest.raises(ValueError, match="linearly dependent"):
            Lattice3D(
                a1=np.array([1.0, 0.0, 0.0]),
                a2=np.array([2.0, 0.0, 0.0]),
                a3=np.array([0.0, 0.0, 1.0]),
            )

    def test_rejects_zero_vector(self):
        with pytest.raises(ValueError, match="linearly dependent"):
            Lattice3D(
                a1=np.array([1.0, 0.0, 0.0]),
                a2=np.array([0.0, 1.0, 0.0]),
                a3=np.array([0.0, 0.0, 0.0]),
            )

    def test_rejects_coplanar_vectors(self):
        with pytest.raises(ValueError, match="linearly dependent"):
            Lattice3D(
                a1=np.array([1.0, 0.0, 0.0]),
                a2=np.array([0.0, 1.0, 0.0]),
                a3=np.array([1.0, 1.0, 0.0]),
            )

    def test_rejects_wrong_a1_shape(self):
        with pytest.raises(ValueError, match="Expected vector shape"):
            Lattice3D(
                a1=np.array([1.0, 0.0]),
                a2=np.array([0.0, 1.0, 0.0]),
                a3=np.array([0.0, 0.0, 1.0]),
            )

    def test_rejects_wrong_a2_shape(self):
        with pytest.raises(ValueError, match="Expected vector shape"):
            Lattice3D(
                a1=np.array([1.0, 0.0, 0.0]),
                a2=np.array([0.0, 1.0]),
                a3=np.array([0.0, 0.0, 1.0]),
            )

    def test_rejects_wrong_a3_shape(self):
        with pytest.raises(ValueError, match="Expected vector shape"):
            Lattice3D(
                a1=np.array([1.0, 0.0, 0.0]),
                a2=np.array([0.0, 1.0, 0.0]),
                a3=np.array([0.0, 0.0]),
            )