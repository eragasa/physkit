import numpy as np
import pytest

from .lattice import Lattice1D

def test_lattice1d_default_basis():
    lat = Lattice1D()

    np.testing.assert_allclose(lat.a1, np.array([1.0]))
    np.testing.assert_allclose(lat.A, np.array([[1.0]]))


def test_lattice1d_dimension_is_one():
    lat = Lattice1D()

    assert lat.dim == 1


def test_lattice1d_basis_is_float_array():
    lat = Lattice1D(a=2)

    assert lat.a1.dtype == float
    np.testing.assert_allclose(lat.a1, np.array([2.0]))


def test_lattice1d_A_stores_primitive_vector_as_column():
    lat = Lattice1D(a=3.5)

    expected_A = np.array([[3.5]])

    np.testing.assert_allclose(lat.A, expected_A)
    np.testing.assert_allclose(lat.A[:, 0], lat.a1)


def test_lattice1d_a_property_returns_scalar_lattice_constant():
    lat = Lattice1D(a=2.5)

    assert lat.a == pytest.approx(2.5)


def test_lattice1d_negative_a_is_allowed_but_length_is_positive():
    lat = Lattice1D(a=-2.0)

    np.testing.assert_allclose(lat.a1, np.array([-2.0]))

    assert lat.a == pytest.approx(-2.0)
    assert lat.a1_length == pytest.approx(2.0)
    assert lat.omega == pytest.approx(2.0)


def test_lattice1d_rejects_zero_lattice_constant():
    with pytest.raises(ValueError, match="nonzero|linearly dependent"):
        Lattice1D(a=0.0)


def test_lattice1d_length_for_unit_lattice():
    lat = Lattice1D()

    assert lat.a1_length == pytest.approx(1.0)
    np.testing.assert_allclose(lat.lengths, np.array([1.0]))


def test_lattice1d_length_for_nonunit_lattice():
    lat = Lattice1D(a=4.25)

    assert lat.a1_length == pytest.approx(4.25)
    np.testing.assert_allclose(lat.lengths, np.array([4.25]))


def test_lattice1d_omega_is_unit_cell_length():
    lat = Lattice1D(a=3.0)

    assert lat.omega == pytest.approx(3.0)


def test_lattice1d_length_cell_alias_matches_omega():
    lat = Lattice1D(a=3.0)

    assert lat.length_cell == pytest.approx(lat.omega)
    assert lat.length_cell == pytest.approx(3.0)


def test_lattice1d_get_R_for_unit_lattice():
    lat = Lattice1D()

    R = lat.get_R(np.array([5]))

    np.testing.assert_allclose(R, np.array([5.0]))


def test_lattice1d_get_R_for_nonunit_lattice():
    lat = Lattice1D(a=2.5)

    R = lat.get_R(np.array([4]))

    np.testing.assert_allclose(R, np.array([10.0]))


def test_lattice1d_get_R_for_negative_index():
    lat = Lattice1D(a=2.5)

    R = lat.get_R(np.array([-3]))

    np.testing.assert_allclose(R, np.array([-7.5]))


def test_lattice1d_get_R_matches_matrix_product():
    lat = Lattice1D(a=2.5)

    n = np.array([6])
    R = lat.get_R(n)

    np.testing.assert_allclose(R, lat.A @ n)


def test_lattice1d_get_R_accepts_list_input():
    lat = Lattice1D(a=3.0)

    R = lat.get_R([2])

    np.testing.assert_allclose(R, np.array([6.0]))


def test_lattice1d_get_R_rejects_scalar_index():
    lat = Lattice1D()

    with pytest.raises(ValueError, match="Expected index shape"):
        lat.get_R(np.array(1))


def test_lattice1d_get_R_rejects_wrong_index_shape():
    lat = Lattice1D()

    with pytest.raises(ValueError, match="Expected index shape"):
        lat.get_R(np.array([1, 2]))


def test_lattice1d_internal_vectors_are_consistent_with_A():
    lat = Lattice1D(a=2.5)

    np.testing.assert_allclose(lat.vectors[0], lat.a1)
    np.testing.assert_allclose(lat.A[:, 0], lat.a1)


def test_lattice1d_contract_R_equals_A_n():
    lat = Lattice1D(a=1.75)

    for n_value in [-3, -1, 0, 1, 4]:
        n = np.array([n_value])
        R = lat.get_R(n)

        expected_R = np.array([lat.a * n_value])

        np.testing.assert_allclose(R, expected_R)
        np.testing.assert_allclose(R, lat.A @ n)