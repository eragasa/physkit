import numpy as np
import pytest

from .lattice import Lattice2D


def test_lattice2d_default_basis_is_unit_square():
    lat = Lattice2D()

    np.testing.assert_allclose(lat.a1, np.array([1.0, 0.0]))
    np.testing.assert_allclose(lat.a2, np.array([0.0, 1.0]))

    expected_A = np.array([
        [1.0, 0.0],
        [0.0, 1.0],
    ])

    np.testing.assert_allclose(lat.A, expected_A)


def test_lattice2d_dimension_is_two():
    lat = Lattice2D()

    assert lat.dim == 2


def test_lattice2d_vectors_are_float_arrays():
    lat = Lattice2D(
        a1=np.array([2, 0]),
        a2=np.array([0, 3]),
    )

    assert lat.a1.dtype == float
    assert lat.a2.dtype == float

    np.testing.assert_allclose(lat.a1, np.array([2.0, 0.0]))
    np.testing.assert_allclose(lat.a2, np.array([0.0, 3.0]))


def test_lattice2d_A_stores_primitive_vectors_as_columns():
    a1 = np.array([2.0, 1.0])
    a2 = np.array([0.5, 3.0])

    lat = Lattice2D(a1=a1, a2=a2)

    expected_A = np.column_stack([a1, a2])

    np.testing.assert_allclose(lat.A, expected_A)
    np.testing.assert_allclose(lat.A[:, 0], lat.a1)
    np.testing.assert_allclose(lat.A[:, 1], lat.a2)


def test_lattice2d_rejects_wrong_a1_shape():
    with pytest.raises(ValueError, match="Expected vector shape"):
        Lattice2D(
            a1=np.array([1.0, 0.0, 0.0]),
            a2=np.array([0.0, 1.0]),
        )


def test_lattice2d_rejects_wrong_a2_shape():
    with pytest.raises(ValueError, match="Expected vector shape"):
        Lattice2D(
            a1=np.array([1.0, 0.0]),
            a2=np.array([0.0, 1.0, 0.0]),
        )


def test_lattice2d_rejects_scalar_a1():
    with pytest.raises(ValueError, match="Expected vector shape"):
        Lattice2D(
            a1=np.array(1.0),
            a2=np.array([0.0, 1.0]),
        )


def test_lattice2d_rejects_scalar_a2():
    with pytest.raises(ValueError, match="Expected vector shape"):
        Lattice2D(
            a1=np.array([1.0, 0.0]),
            a2=np.array(1.0),
        )


def test_lattice2d_rejects_linearly_dependent_vectors():
    with pytest.raises(ValueError, match="linearly dependent"):
        Lattice2D(
            a1=np.array([1.0, 0.0]),
            a2=np.array([2.0, 0.0]),
        )


def test_lattice2d_rejects_zero_vector():
    with pytest.raises(ValueError, match="linearly dependent"):
        Lattice2D(
            a1=np.array([1.0, 0.0]),
            a2=np.array([0.0, 0.0]),
        )


def test_lattice2d_lengths_for_unit_square_lattice():
    lat = Lattice2D()

    assert lat.a1_length == pytest.approx(1.0)
    assert lat.a2_length == pytest.approx(1.0)

    np.testing.assert_allclose(lat.lengths, np.array([1.0, 1.0]))


def test_lattice2d_lengths_for_rectangular_lattice():
    lat = Lattice2D(
        a1=np.array([2.0, 0.0]),
        a2=np.array([0.0, 3.0]),
    )

    assert lat.a1_length == pytest.approx(2.0)
    assert lat.a2_length == pytest.approx(3.0)

    np.testing.assert_allclose(lat.lengths, np.array([2.0, 3.0]))


def test_lattice2d_lengths_for_oblique_lattice():
    lat = Lattice2D(
        a1=np.array([3.0, 4.0]),
        a2=np.array([1.0, 2.0]),
    )

    assert lat.a1_length == pytest.approx(5.0)
    assert lat.a2_length == pytest.approx(np.sqrt(5.0))

    np.testing.assert_allclose(
        lat.lengths,
        np.array([5.0, np.sqrt(5.0)]),
    )


def test_lattice2d_area_for_unit_square_lattice():
    lat = Lattice2D()

    assert lat.area == pytest.approx(1.0)
    assert lat.omega == pytest.approx(1.0)


def test_lattice2d_area_for_rectangular_lattice():
    lat = Lattice2D(
        a1=np.array([2.0, 0.0]),
        a2=np.array([0.0, 3.0]),
    )

    assert lat.area == pytest.approx(6.0)
    assert lat.omega == pytest.approx(6.0)


def test_lattice2d_area_for_oblique_lattice():
    a1 = np.array([2.0, 1.0])
    a2 = np.array([1.0, 3.0])

    lat = Lattice2D(a1=a1, a2=a2)

    expected_area = abs(np.linalg.det(np.column_stack([a1, a2])))

    assert lat.area == pytest.approx(expected_area)
    assert lat.omega == pytest.approx(expected_area)


def test_lattice2d_area_is_positive_for_left_handed_basis():
    lat = Lattice2D(
        a1=np.array([0.0, 1.0]),
        a2=np.array([1.0, 0.0]),
    )

    assert np.linalg.det(lat.A) < 0.0
    assert lat.area == pytest.approx(1.0)
    assert lat.omega == pytest.approx(1.0)


def test_lattice2d_get_R_for_unit_square_lattice():
    lat = Lattice2D()

    R = lat.get_R(np.array([2, 3]))

    np.testing.assert_allclose(R, np.array([2.0, 3.0]))


def test_lattice2d_get_R_for_rectangular_lattice():
    lat = Lattice2D(
        a1=np.array([2.0, 0.0]),
        a2=np.array([0.0, 3.0]),
    )

    R = lat.get_R(np.array([2, 3]))

    expected_R = 2 * lat.a1 + 3 * lat.a2

    np.testing.assert_allclose(R, expected_R)
    np.testing.assert_allclose(R, np.array([4.0, 9.0]))


def test_lattice2d_get_R_for_oblique_lattice():
    lat = Lattice2D(
        a1=np.array([2.0, 1.0]),
        a2=np.array([1.0, 3.0]),
    )

    n = np.array([4, -2])

    R = lat.get_R(n)

    expected_R = 4 * lat.a1 - 2 * lat.a2

    np.testing.assert_allclose(R, expected_R)


def test_lattice2d_get_R_accepts_list_input():
    lat = Lattice2D()

    R = lat.get_R([3, -1])

    np.testing.assert_allclose(R, np.array([3.0, -1.0]))


def test_lattice2d_get_R_matches_matrix_product():
    lat = Lattice2D(
        a1=np.array([2.0, 1.0]),
        a2=np.array([1.0, 3.0]),
    )

    n = np.array([5, -2])

    R = lat.get_R(n)

    np.testing.assert_allclose(R, lat.A @ n)


def test_lattice2d_get_R_rejects_wrong_index_shape():
    lat = Lattice2D()

    with pytest.raises(ValueError, match="Expected index shape"):
        lat.get_R(np.array([1, 2, 3]))


def test_lattice2d_get_R_rejects_scalar_index():
    lat = Lattice2D()

    with pytest.raises(ValueError, match="Expected index shape"):
        lat.get_R(np.array(1))


def test_lattice2d_input_arrays_are_defensively_copied():
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.0, 1.0])

    lat = Lattice2D(a1=a1, a2=a2)

    a1[0] = 100.0
    a2[1] = 200.0

    np.testing.assert_allclose(lat.a1, np.array([1.0, 0.0]))
    np.testing.assert_allclose(lat.a2, np.array([0.0, 1.0]))


def test_lattice2d_internal_vectors_are_consistent_with_A():
    lat = Lattice2D(
        a1=np.array([2.0, 1.0]),
        a2=np.array([1.0, 3.0]),
    )

    np.testing.assert_allclose(lat.vectors[0], lat.a1)
    np.testing.assert_allclose(lat.vectors[1], lat.a2)

    np.testing.assert_allclose(lat.A[:, 0], lat.a1)
    np.testing.assert_allclose(lat.A[:, 1], lat.a2)