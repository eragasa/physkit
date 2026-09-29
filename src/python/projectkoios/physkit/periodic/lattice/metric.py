"""Metric geometry derived from two- and three-dimensional direct lattices."""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product

import numpy as np

from projectkoios.physkit.core.data import DataObject
from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.periodic.lattice.base import FloatArray, IntArray
from projectkoios.physkit.periodic.lattice.lattice2d import DirectLattice2D
from projectkoios.physkit.periodic.lattice.lattice3d import DirectLattice3D

type SupportedDirectLattice = DirectLattice2D | DirectLattice3D


@dataclass(frozen=True, slots=True, eq=False)
class DirectLatticeMetric(DataObject):
    r"""Own metric data derived from an ordered direct-lattice basis.

    For a direct primitive-basis matrix ``A`` whose vectors are columns, the
    covariant metric, inverse metric, and reciprocal primitive basis are

    .. math::

        g=A^{\mathsf T}A,
        \qquad
        g^{-1}=(A^{\mathsf T}A)^{-1},
        \qquad
        B=2\pi A^{-\mathsf T}.

    The record supports only the nominal two- and three-dimensional direct
    lattice types owned by :mod:`projectkoios.physkit.periodic.lattice`.
    Numerical bases carry one caller-declared consistent length convention;
    this record does not attach physical units or infer material properties.
    """

    direct_lattice: SupportedDirectLattice
    _primitive_basis: FloatArray = field(init=False, repr=False)
    _reciprocal_basis: FloatArray = field(init=False, repr=False)
    _metric_tensor: FloatArray = field(init=False, repr=False)
    _inverse_metric_tensor: FloatArray = field(init=False, repr=False)
    _reciprocal_metric_tensor: FloatArray = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Copy the nominal source lattice and derive immutable metric data."""
        if isinstance(self.direct_lattice, DirectLattice2D):
            source_basis = np.asarray(self.direct_lattice.A, dtype=np.float64)
            owned_lattice: SupportedDirectLattice = DirectLattice2D(
                a1=source_basis[:, 0],
                a2=source_basis[:, 1],
            )
            primitive_basis = np.array(owned_lattice.A, copy=True)
        elif isinstance(self.direct_lattice, DirectLattice3D):
            source_basis = np.asarray(self.direct_lattice.A, dtype=np.float64)
            owned_lattice = DirectLattice3D(
                a1=source_basis[:, 0],
                a2=source_basis[:, 1],
                a3=source_basis[:, 2],
            )
            primitive_basis = np.array(owned_lattice.A, copy=True)
        else:
            raise TypeError("direct_lattice must be DirectLattice2D or DirectLattice3D")

        metric_tensor = np.asarray(
            primitive_basis.T @ primitive_basis,
            dtype=np.float64,
        )
        try:
            np.linalg.cholesky(metric_tensor)
            inverse_metric_tensor = np.asarray(
                np.linalg.inv(metric_tensor),
                dtype=np.float64,
            )
            reciprocal_basis = np.asarray(
                2.0 * np.pi * np.linalg.inv(primitive_basis).T,
                dtype=np.float64,
            )
            reciprocal_metric_tensor = np.asarray(
                reciprocal_basis.T @ reciprocal_basis,
                dtype=np.float64,
            )
        except np.linalg.LinAlgError as error:
            raise ValueError(
                "direct lattice metric must be invertible in float64"
            ) from error
        if not all(
            np.all(np.isfinite(array))
            for array in (
                metric_tensor,
                inverse_metric_tensor,
                reciprocal_basis,
                reciprocal_metric_tensor,
            )
        ):
            raise ValueError(
                "direct lattice metric must be representable as finite float64"
            )

        for array in (
            primitive_basis,
            reciprocal_basis,
            metric_tensor,
            inverse_metric_tensor,
            reciprocal_metric_tensor,
        ):
            array.setflags(write=False)

        object.__setattr__(self, "direct_lattice", owned_lattice)
        object.__setattr__(self, "_primitive_basis", primitive_basis)
        object.__setattr__(self, "_reciprocal_basis", reciprocal_basis)
        object.__setattr__(self, "_metric_tensor", metric_tensor)
        object.__setattr__(self, "_inverse_metric_tensor", inverse_metric_tensor)
        object.__setattr__(
            self,
            "_reciprocal_metric_tensor",
            reciprocal_metric_tensor,
        )

    @property
    def dimension(self) -> int:
        """Return the direct-basis dimension, either two or three."""
        return self.primitive_basis.shape[0]

    @property
    def primitive_basis(self) -> FloatArray:
        """Return the immutable direct primitive-basis matrix ``A``."""
        return self._primitive_basis

    @property
    def reciprocal_basis(self) -> FloatArray:
        r"""Return the immutable reciprocal basis ``2\pi A^{-\mathsf T}``."""
        return self._reciprocal_basis

    @property
    def metric_tensor(self) -> FloatArray:
        r"""Return the immutable covariant metric ``A^{\mathsf T}A``."""
        return self._metric_tensor

    @property
    def inverse_metric_tensor(self) -> FloatArray:
        """Return the immutable contravariant metric ``g^{-1}``."""
        return self._inverse_metric_tensor

    @property
    def reciprocal_metric_tensor(self) -> FloatArray:
        r"""Return ``B^{\mathsf T}B=(2\pi)^2g^{-1}``."""
        return self._reciprocal_metric_tensor

    @property
    def measure(self) -> float:
        r"""Return ``abs(det(A))``, mathematically equal to ``sqrt(det(g))``.

        The owned direct lattice evaluates the determinant of ``A`` directly.
        Avoiding ``det(A.T @ A)`` prevents the Gram determinant from
        overflowing or underflowing when the represented cell measure remains
        finite.
        """
        return self.direct_lattice.measure

    def to_cartesian(self, fractional_coordinates: FloatArray) -> FloatArray:
        """Map one or more fractional-coordinate vectors into Cartesian space.

        Parameters
        ----------
        fractional_coordinates:
            Floating coordinates with shape ``(dimension,)`` or final dimension
            equal to ``dimension``.

        Returns
        -------
        FloatArray
            Cartesian vectors with the same leading shape.

        Raises
        ------
        ValueError
            If the input has the wrong final dimension or contains nonfinite
            values.
        """
        fractional = np.asarray(fractional_coordinates, dtype=np.float64)
        if fractional.ndim == 0 or fractional.shape[-1] != self.dimension:
            raise ValueError(
                f"fractional_coordinates must have final dimension {self.dimension}"
            )
        if not np.all(np.isfinite(fractional)):
            raise ValueError("fractional_coordinates must contain finite values")
        return np.asarray(fractional @ self.primitive_basis.T, dtype=np.float64)


@dataclass(frozen=True, slots=True, eq=False)
class NearestLatticeImageResult(ResultsObject):
    """Correlate a fractional displacement with its nearest periodic image."""

    metric: DirectLatticeMetric
    displacement_fractional: FloatArray
    translation_indices: IntArray
    image_fractional: FloatArray
    image_cartesian: FloatArray

    def __post_init__(self) -> None:
        """Validate, copy, and freeze the correlated image data."""
        if type(self.metric) is not DirectLatticeMetric:
            raise TypeError("metric must be DirectLatticeMetric")

        displacement = np.array(
            self.displacement_fractional,
            dtype=np.float64,
            copy=True,
        )
        translation = np.array(
            self.translation_indices,
            dtype=np.int64,
            copy=True,
        )
        image_fractional = np.array(
            self.image_fractional,
            dtype=np.float64,
            copy=True,
        )
        image_cartesian = np.array(
            self.image_cartesian,
            dtype=np.float64,
            copy=True,
        )
        expected_shape = (self.metric.dimension,)
        if any(
            array.shape != expected_shape
            for array in (
                displacement,
                translation,
                image_fractional,
                image_cartesian,
            )
        ):
            raise ValueError(
                "all displacement and translation vectors must match metric dimension"
            )
        if not all(
            np.all(np.isfinite(array))
            for array in (displacement, image_fractional, image_cartesian)
        ):
            raise ValueError("displacement vectors must contain finite values")
        if not np.array_equal(image_fractional, displacement - translation):
            raise ValueError(
                "image_fractional must equal displacement minus translation"
            )
        with np.errstate(over="ignore", invalid="ignore"):
            expected_cartesian = self.metric.to_cartesian(image_fractional)
            componentwise_mapping_magnitudes = np.abs(
                self.metric.primitive_basis
            ) @ np.abs(image_fractional)
        epsilon = np.finfo(np.float64).eps
        summation_error_factor = (
            self.metric.dimension * epsilon / (1.0 - self.metric.dimension * epsilon)
        )
        mapping_roundoff = (
            8.0 * summation_error_factor * componentwise_mapping_magnitudes
        )
        representation_spacing = 8.0 * np.abs(np.spacing(np.abs(expected_cartesian)))
        consistency_tolerance = np.maximum(
            mapping_roundoff,
            representation_spacing,
        )
        with np.errstate(over="ignore", invalid="ignore"):
            mapping_difference = np.abs(image_cartesian - expected_cartesian)
        if (
            not np.all(np.isfinite(expected_cartesian))
            or not np.all(np.isfinite(consistency_tolerance))
            or not np.all(mapping_difference <= consistency_tolerance)
        ):
            raise ValueError("image_cartesian must be the mapped fractional image")

        for array in (
            displacement,
            translation,
            image_fractional,
            image_cartesian,
        ):
            array.setflags(write=False)

        object.__setattr__(self, "displacement_fractional", displacement)
        object.__setattr__(self, "translation_indices", translation)
        object.__setattr__(self, "image_fractional", image_fractional)
        object.__setattr__(self, "image_cartesian", image_cartesian)

    @property
    def distance(self) -> float:
        """Return the Cartesian distance of the selected periodic image."""
        return float(np.linalg.norm(self.image_cartesian))


class NearestLatticeImageResolver:
    r"""Resolve the exact nearest image under a two- or three-dimensional basis.

    For fractional displacement ``s`` and integer lattice translation ``n``, the
    resolver minimizes ``||A(s-n)||``. Componentwise rounding supplies an initial
    candidate with Cartesian radius ``r``. If ``sigma_min`` is the smallest
    singular value of ``A``, every candidate no farther than ``r`` satisfies

    .. math::

        \|s-n\|_2 \leq r/\sigma_{\min}.

    Enumerating the resulting finite integer bounding box is therefore complete;
    no heuristic neighbor shell is used. Supported dimensions remain bounded to
    the nominal two- and three-dimensional lattice types accepted by
    :class:`DirectLatticeMetric`.
    """

    __slots__ = ()

    def execute(
        self,
        metric: DirectLatticeMetric,
        displacement_fractional: FloatArray,
    ) -> NearestLatticeImageResult:
        """Return the nearest periodic image of one fractional displacement."""
        if type(metric) is not DirectLatticeMetric:
            raise TypeError("metric must be DirectLatticeMetric")
        displacement = np.asarray(displacement_fractional, dtype=np.float64)
        if displacement.shape != (metric.dimension,):
            raise ValueError(
                f"displacement_fractional must have shape ({metric.dimension},)"
            )
        if not np.all(np.isfinite(displacement)):
            raise ValueError("displacement_fractional must contain finite values")

        integer_limit = float(np.nextafter(np.float64(np.iinfo(np.int64).max), 0.0))
        if np.any(np.abs(displacement) > integer_limit):
            raise ValueError(
                "displacement_fractional exceeds the supported int64 translation range"
            )

        rounded = np.rint(displacement).astype(np.int64)
        best_translation = tuple(int(value) for value in rounded)
        best_fractional = displacement - rounded
        best_cartesian = metric.to_cartesian(best_fractional)
        best_distance_squared = float(best_cartesian @ best_cartesian)

        smallest_singular_value = float(
            np.linalg.svd(metric.primitive_basis, compute_uv=False)[-1]
        )
        radius = np.sqrt(best_distance_squared) / smallest_singular_value
        radius = float(np.nextafter(radius, np.inf))
        lower_float = np.ceil(displacement - radius)
        upper_float = np.floor(displacement + radius)
        if (
            not np.isfinite(radius)
            or np.any(lower_float < -integer_limit)
            or np.any(upper_float > integer_limit)
        ):
            raise ValueError("nearest-image search bound exceeds int64 translations")
        lower = lower_float.astype(np.int64)
        upper = upper_float.astype(np.int64)
        lower = np.minimum(lower, rounded)
        upper = np.maximum(upper, rounded)

        ranges = tuple(
            range(int(first), int(last) + 1)
            for first, last in zip(lower, upper, strict=True)
        )
        for candidate in product(*ranges):
            candidate_indices = np.asarray(candidate, dtype=np.int64)
            candidate_fractional = displacement - candidate_indices
            candidate_cartesian = metric.to_cartesian(candidate_fractional)
            candidate_distance_squared = float(
                candidate_cartesian @ candidate_cartesian
            )
            if candidate_distance_squared < best_distance_squared:
                best_translation = candidate
                best_fractional = candidate_fractional
                best_cartesian = candidate_cartesian
                best_distance_squared = candidate_distance_squared

        translation = np.asarray(best_translation, dtype=np.int64)
        return NearestLatticeImageResult(
            metric=metric,
            displacement_fractional=displacement,
            translation_indices=translation,
            image_fractional=best_fractional,
            image_cartesian=best_cartesian,
        )
