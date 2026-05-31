import numpy as np
import pytest

from physkit.core.grids import CartesianAxis, CartesianGrid2D


def test__init__stores_axis_objects():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=-1.0,
        y_max=1.0,
        Ny=3,
        endpoint_x=True,
        endpoint_y=True,
    )

    assert isinstance(grid.x_axis, CartesianAxis)
    assert isinstance(grid.y_axis, CartesianAxis)


def test__init__stores_constructor_arguments():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=-1.0,
        y_max=1.0,
        Ny=3,
        endpoint_x=True,
        endpoint_y=False,
    )

    assert grid.x_min == 0.0
    assert grid.x_max == 1.0
    assert grid.Nx == 5
    assert grid.endpoint_x is True

    assert grid.y_min == -1.0
    assert grid.y_max == 1.0
    assert grid.Ny == 3
    assert grid.endpoint_y is False


def test__init__builds_x_axis_values_with_endpoint():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=0.0,
        y_max=1.0,
        Ny=3,
        endpoint_x=True,
    )

    expected = np.array([0.0, 0.25, 0.50, 0.75, 1.0])

    np.testing.assert_allclose(grid.x, expected)


def test__init__builds_x_axis_values_without_endpoint():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=0.0,
        y_max=1.0,
        Ny=3,
        endpoint_x=False,
    )

    expected = np.array([0.0, 0.2, 0.4, 0.6, 0.8])

    np.testing.assert_allclose(grid.x, expected)


def test__init__builds_y_axis_values_with_endpoint():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=-1.0,
        y_max=1.0,
        Ny=5,
        endpoint_y=True,
    )

    expected = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])

    np.testing.assert_allclose(grid.y, expected)


def test__init__builds_y_axis_values_without_endpoint():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=-1.0,
        y_max=1.0,
        Ny=5,
        endpoint_y=False,
    )

    expected = np.array([-1.0, -0.6, -0.2, 0.2, 0.6])

    np.testing.assert_allclose(grid.y, expected)


def test__init__computes_domain_lengths():
    grid = CartesianGrid2D(
        x_min=-2.0,
        x_max=3.0,
        Nx=6,
        y_min=-1.0,
        y_max=2.0,
        Ny=4,
    )

    assert grid.Lx == pytest.approx(5.0)
    assert grid.Ly == pytest.approx(3.0)


def test__init__computes_spacing_with_endpoints():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=0.0,
        y_max=2.0,
        Ny=5,
        endpoint_x=True,
        endpoint_y=True,
    )

    assert grid.dx == pytest.approx(0.25)
    assert grid.dy == pytest.approx(0.50)


def test__init__computes_spacing_without_endpoints():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=0.0,
        y_max=2.0,
        Ny=5,
        endpoint_x=False,
        endpoint_y=False,
    )

    assert grid.dx == pytest.approx(0.20)
    assert grid.dy == pytest.approx(0.40)


def test__init__sets_shape():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=0.0,
        y_max=2.0,
        Ny=7,
    )

    assert grid.shape == (5, 7)


def test__init__sets_size():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=0.0,
        y_max=2.0,
        Ny=7,
    )

    assert grid.size == 35


def test__init__axes_are_float64():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=0.0,
        y_max=2.0,
        Ny=7,
    )

    assert grid.x.dtype == np.float64
    assert grid.y.dtype == np.float64


def test__init__axes_are_read_only():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=0.0,
        y_max=2.0,
        Ny=7,
    )

    assert grid.x.flags.writeable is False
    assert grid.y.flags.writeable is False

    with pytest.raises(ValueError):
        grid.x[0] = 10.0

    with pytest.raises(ValueError):
        grid.y[0] = 10.0


def test__init__axes_reference_axis_values():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=0.0,
        y_max=2.0,
        Ny=7,
    )

    assert grid.x is grid.x_axis.values
    assert grid.y is grid.y_axis.values


def test__mesh__returns_coordinate_mesh_with_indexing_ij():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=3,
        y_min=10.0,
        y_max=20.0,
        Ny=2,
    )

    X, Y = grid.mesh

    expected_X = np.array(
        [
            [0.0, 0.0],
            [0.5, 0.5],
            [1.0, 1.0],
        ]
    )

    expected_Y = np.array(
        [
            [10.0, 20.0],
            [10.0, 20.0],
            [10.0, 20.0],
        ]
    )

    assert X.shape == (3, 2)
    assert Y.shape == (3, 2)

    np.testing.assert_allclose(X, expected_X)
    np.testing.assert_allclose(Y, expected_Y)


def test__points__returns_flattened_coordinate_pairs():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=3,
        y_min=10.0,
        y_max=20.0,
        Ny=2,
    )

    expected = np.array(
        [
            [0.0, 10.0],
            [0.0, 20.0],
            [0.5, 10.0],
            [0.5, 20.0],
            [1.0, 10.0],
            [1.0, 20.0],
        ]
    )

    assert grid.points.shape == (6, 2)
    np.testing.assert_allclose(grid.points, expected)


@pytest.mark.parametrize("bad_x_min", [np.nan, np.inf, -np.inf])
def test__init__rejects_nonfinite_x_min(bad_x_min):
    with pytest.raises(ValueError, match="x_min must be finite"):
        CartesianGrid2D(
            x_min=bad_x_min,
            x_max=1.0,
            Nx=5,
            y_min=0.0,
            y_max=1.0,
            Ny=5,
        )


@pytest.mark.parametrize("bad_x_max", [np.nan, np.inf, -np.inf])
def test__init__rejects_nonfinite_x_max(bad_x_max):
    with pytest.raises(ValueError, match="x_max must be finite"):
        CartesianGrid2D(
            x_min=0.0,
            x_max=bad_x_max,
            Nx=5,
            y_min=0.0,
            y_max=1.0,
            Ny=5,
        )


@pytest.mark.parametrize(
    "x_min, x_max",
    [
        (1.0, 1.0),
        (2.0, 1.0),
    ],
)
def test__init__rejects_invalid_x_bounds(x_min, x_max):
    with pytest.raises(ValueError, match="x_max must be greater than x_min"):
        CartesianGrid2D(
            x_min=x_min,
            x_max=x_max,
            Nx=5,
            y_min=0.0,
            y_max=1.0,
            Ny=5,
        )


@pytest.mark.parametrize("bad_Nx", [5.0, "5", None])
def test__init__rejects_noninteger_Nx(bad_Nx):
    with pytest.raises(TypeError, match="Nx must be an integer"):
        CartesianGrid2D(
            x_min=0.0,
            x_max=1.0,
            Nx=bad_Nx,
            y_min=0.0,
            y_max=1.0,
            Ny=5,
        )


@pytest.mark.parametrize("bad_Nx", [-1, 0, 1])
def test__init__rejects_too_few_x_points(bad_Nx):
    with pytest.raises(ValueError, match="Nx must be at least 2"):
        CartesianGrid2D(
            x_min=0.0,
            x_max=1.0,
            Nx=bad_Nx,
            y_min=0.0,
            y_max=1.0,
            Ny=5,
        )


@pytest.mark.parametrize("bad_y_min", [np.nan, np.inf, -np.inf])
def test__init__rejects_nonfinite_y_min(bad_y_min):
    with pytest.raises(ValueError, match="y_min must be finite"):
        CartesianGrid2D(
            x_min=0.0,
            x_max=1.0,
            Nx=5,
            y_min=bad_y_min,
            y_max=1.0,
            Ny=5,
        )


@pytest.mark.parametrize("bad_y_max", [np.nan, np.inf, -np.inf])
def test__init__rejects_nonfinite_y_max(bad_y_max):
    with pytest.raises(ValueError, match="y_max must be finite"):
        CartesianGrid2D(
            x_min=0.0,
            x_max=1.0,
            Nx=5,
            y_min=0.0,
            y_max=bad_y_max,
            Ny=5,
        )


@pytest.mark.parametrize(
    "y_min, y_max",
    [
        (1.0, 1.0),
        (2.0, 1.0),
    ],
)
def test__init__rejects_invalid_y_bounds(y_min, y_max):
    with pytest.raises(ValueError, match="y_max must be greater than y_min"):
        CartesianGrid2D(
            x_min=0.0,
            x_max=1.0,
            Nx=5,
            y_min=y_min,
            y_max=y_max,
            Ny=5,
        )


@pytest.mark.parametrize("bad_Ny", [5.0, "5", None])
def test__init__rejects_noninteger_Ny(bad_Ny):
    with pytest.raises(TypeError, match="Ny must be an integer"):
        CartesianGrid2D(
            x_min=0.0,
            x_max=1.0,
            Nx=5,
            y_min=0.0,
            y_max=1.0,
            Ny=bad_Ny,
        )


@pytest.mark.parametrize("bad_Ny", [-1, 0, 1])
def test__init__rejects_too_few_y_points(bad_Ny):
    with pytest.raises(ValueError, match="Ny must be at least 2"):
        CartesianGrid2D(
            x_min=0.0,
            x_max=1.0,
            Nx=5,
            y_min=0.0,
            y_max=1.0,
            Ny=bad_Ny,
        )


@pytest.mark.parametrize("bad_endpoint_x", [0, 1, "True", None])
def test__init__rejects_nonbool_endpoint_x(bad_endpoint_x):
    with pytest.raises(TypeError, match="endpoint_x must be a bool"):
        CartesianGrid2D(
            x_min=0.0,
            x_max=1.0,
            Nx=5,
            y_min=0.0,
            y_max=1.0,
            Ny=5,
            endpoint_x=bad_endpoint_x,
        )


@pytest.mark.parametrize("bad_endpoint_y", [0, 1, "True", None])
def test__init__rejects_nonbool_endpoint_y(bad_endpoint_y):
    with pytest.raises(TypeError, match="endpoint_y must be a bool"):
        CartesianGrid2D(
            x_min=0.0,
            x_max=1.0,
            Nx=5,
            y_min=0.0,
            y_max=1.0,
            Ny=5,
            endpoint_y=bad_endpoint_y,
        )


def test__repr__returns_expected_string():
    grid = CartesianGrid2D(
        x_min=0.0,
        x_max=1.0,
        Nx=5,
        y_min=-1.0,
        y_max=1.0,
        Ny=3,
        endpoint_x=True,
        endpoint_y=False,
    )

    expected = (
        "CartesianGrid2D("
        "x_min=0.0, "
        "x_max=1.0, "
        "Nx=5, "
        "y_min=-1.0, "
        "y_max=1.0, "
        "Ny=3, "
        "endpoint_x=True, "
        "endpoint_y=False)"
    )

    assert repr(grid) == expected
