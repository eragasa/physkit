from __future__ import annotations

import math

import numpy as np
import pytest

from physkit.periodic.lattice.lattice3d import DirectLattice3D


def test_constructs_orthogonal_lattice() -> None:
    lattice = DirectLattice3D.from_lattice_parameters(
        a=2.0,
        b=3.0,
        c=4.0,
        alpha_degrees=90.0,
        beta_degrees=90.0,
        gamma_degrees=90.0,
    )

    np.testing.assert_allclose(
        lattice.A,
        np.diag((2.0, 3.0, 4.0)),
        atol=1.0e-15,
    )
    assert lattice.is_right_handed


def test_constructs_tiny_orthogonal_lattice() -> None:
    scale = 1.0e-200

    lattice = DirectLattice3D.from_lattice_parameters(
        a=scale,
        b=scale,
        c=scale,
        alpha_degrees=90.0,
        beta_degrees=90.0,
        gamma_degrees=90.0,
    )

    np.testing.assert_allclose(
        lattice.A / scale,
        np.eye(3),
        rtol=0.0,
        atol=1.0e-15,
    )


@pytest.mark.parametrize(
    "requested_angles",
    [
        (1.0e-6, 90.0, 90.0),
        (90.0, 1.0e-6, 90.0),
        (90.0, 90.0, 1.0e-6),
    ],
)
def test_preserves_metric_when_any_angle_is_near_independence_tolerance(
    requested_angles: tuple[float, float, float],
) -> None:
    alpha, beta, gamma = requested_angles

    lattice = DirectLattice3D.from_lattice_parameters(
        a=1.0,
        b=1.0,
        c=1.0,
        alpha_degrees=alpha,
        beta_degrees=beta,
        gamma_degrees=gamma,
    )

    vectors = (lattice.a1, lattice.a2, lattice.a3)
    lengths = np.array([np.linalg.norm(vector) for vector in vectors])
    actual_angles = np.array(
        [
            _angle_degrees(lattice.a2, lattice.a3),
            _angle_degrees(lattice.a1, lattice.a3),
            _angle_degrees(lattice.a1, lattice.a2),
        ]
    )
    np.testing.assert_allclose(lengths, np.ones(3), rtol=0.0, atol=1.0e-15)
    np.testing.assert_allclose(
        actual_angles,
        requested_angles,
        rtol=1.0e-12,
        atol=1.0e-15,
    )


@pytest.mark.parametrize(
    "requested_angles",
    [
        (5.0e-7, 90.0, 90.0),
        (90.0, 5.0e-7, 90.0),
        (90.0, 90.0, 5.0e-7),
    ],
)
def test_rejects_any_angle_below_the_independence_tolerance(
    requested_angles: tuple[float, float, float],
) -> None:
    alpha, beta, gamma = requested_angles

    with pytest.raises(ValueError, match="must be linearly independent"):
        DirectLattice3D.from_lattice_parameters(
            a=1.0,
            b=1.0,
            c=1.0,
            alpha_degrees=alpha,
            beta_degrees=beta,
            gamma_degrees=gamma,
        )


def test_constructs_hexagonal_lattice() -> None:
    lattice = DirectLattice3D.from_lattice_parameters(
        a=1.0,
        b=1.0,
        c=2.0,
        alpha_degrees=90.0,
        beta_degrees=90.0,
        gamma_degrees=120.0,
    )

    np.testing.assert_allclose(
        lattice.A,
        np.array(
            [
                [1.0, -0.5, 0.0],
                [0.0, math.sqrt(3.0) / 2.0, 0.0],
                [0.0, 0.0, 2.0],
            ]
        ),
        atol=1.0e-15,
    )
    assert lattice.is_right_handed


def test_constructs_monoclinic_lattice() -> None:
    beta = math.radians(110.0)

    lattice = DirectLattice3D.from_lattice_parameters(
        a=2.0,
        b=3.0,
        c=4.0,
        alpha_degrees=90.0,
        beta_degrees=110.0,
        gamma_degrees=90.0,
    )

    np.testing.assert_allclose(
        lattice.A,
        np.array(
            [
                [2.0, 0.0, 4.0 * math.cos(beta)],
                [0.0, 3.0, 0.0],
                [0.0, 0.0, 4.0 * math.sin(beta)],
            ]
        ),
        atol=1.0e-15,
    )


def test_constructs_triclinic_lattice_with_requested_metric() -> None:
    a, b, c = 2.0, 3.0, 4.0
    alpha = math.radians(75.0)
    beta = math.radians(80.0)
    gamma = math.radians(65.0)

    lattice = DirectLattice3D.from_lattice_parameters(
        a=a,
        b=b,
        c=c,
        alpha_degrees=75.0,
        beta_degrees=80.0,
        gamma_degrees=65.0,
    )

    expected_metric = np.array(
        [
            [a * a, a * b * math.cos(gamma), a * c * math.cos(beta)],
            [a * b * math.cos(gamma), b * b, b * c * math.cos(alpha)],
            [a * c * math.cos(beta), b * c * math.cos(alpha), c * c],
        ]
    )
    np.testing.assert_allclose(lattice.A.T @ lattice.A, expected_metric)
    assert lattice.is_right_handed


@pytest.mark.parametrize(
    "argument",
    ["a", "b", "c", "alpha_degrees", "beta_degrees", "gamma_degrees"],
)
def test_requires_exact_builtin_float_arguments(argument: str) -> None:
    parameters: dict[str, object] = {
        "a": 1.0,
        "b": 1.0,
        "c": 1.0,
        "alpha_degrees": 90.0,
        "beta_degrees": 90.0,
        "gamma_degrees": 90.0,
    }
    parameters[argument] = np.float64(parameters[argument])

    with pytest.raises(TypeError, match=rf"{argument} must be a float"):
        DirectLattice3D.from_lattice_parameters(**parameters)  # type: ignore[arg-type]


@pytest.mark.parametrize("argument", ["a", "b", "c"])
@pytest.mark.parametrize("value", [0.0, -1.0, math.inf, math.nan])
def test_rejects_nonpositive_or_nonfinite_lengths(
    argument: str,
    value: float,
) -> None:
    parameters = {
        "a": 1.0,
        "b": 1.0,
        "c": 1.0,
        "alpha_degrees": 90.0,
        "beta_degrees": 90.0,
        "gamma_degrees": 90.0,
    }
    parameters[argument] = value

    with pytest.raises(ValueError, match=rf"{argument} must be a positive"):
        DirectLattice3D.from_lattice_parameters(**parameters)


@pytest.mark.parametrize(
    "argument",
    ["alpha_degrees", "beta_degrees", "gamma_degrees"],
)
@pytest.mark.parametrize("value", [0.0, 180.0, -1.0, math.inf, math.nan])
def test_rejects_angles_outside_the_open_finite_interval(
    argument: str,
    value: float,
) -> None:
    parameters = {
        "a": 1.0,
        "b": 1.0,
        "c": 1.0,
        "alpha_degrees": 90.0,
        "beta_degrees": 90.0,
        "gamma_degrees": 90.0,
    }
    parameters[argument] = value

    with pytest.raises(ValueError, match=rf"{argument} must be a finite float"):
        DirectLattice3D.from_lattice_parameters(**parameters)


def test_rejects_gamma_whose_sine_underflows_to_zero() -> None:
    smallest_positive_float = float.fromhex("0x0.0000000000001p-1022")

    with pytest.raises(ValueError, match="gamma_degrees must have nonzero sine"):
        DirectLattice3D.from_lattice_parameters(
            a=1.0,
            b=1.0,
            c=1.0,
            alpha_degrees=90.0,
            beta_degrees=90.0,
            gamma_degrees=smallest_positive_float,
        )


@pytest.mark.parametrize(
    ("alpha_degrees", "beta_degrees", "gamma_degrees"),
    [(60.0, 60.0, 120.0), (10.0, 10.0, 30.0)],
)
def test_rejects_nonpositive_volume_metrics(
    alpha_degrees: float,
    beta_degrees: float,
    gamma_degrees: float,
) -> None:
    with pytest.raises(ValueError, match="must define positive volume"):
        DirectLattice3D.from_lattice_parameters(
            a=1.0,
            b=1.0,
            c=1.0,
            alpha_degrees=alpha_degrees,
            beta_degrees=beta_degrees,
            gamma_degrees=gamma_degrees,
        )


def test_owns_independent_immutable_basis_storage() -> None:
    first = DirectLattice3D.from_lattice_parameters(
        a=1.0,
        b=2.0,
        c=3.0,
        alpha_degrees=70.0,
        beta_degrees=80.0,
        gamma_degrees=75.0,
    )
    second = DirectLattice3D.from_lattice_parameters(
        a=1.0,
        b=2.0,
        c=3.0,
        alpha_degrees=70.0,
        beta_degrees=80.0,
        gamma_degrees=75.0,
    )

    assert first.A.flags.writeable is False
    assert second.A.flags.writeable is False
    assert not np.shares_memory(first.A, second.A)
    with pytest.raises(ValueError, match="read-only"):
        first.a1[0] = 2.0


def _angle_degrees(left: np.ndarray, right: np.ndarray) -> float:
    cross_magnitude = np.linalg.norm(np.cross(left, right))
    dot_product = np.dot(left, right)
    return math.degrees(math.atan2(float(cross_magnitude), float(dot_product)))
