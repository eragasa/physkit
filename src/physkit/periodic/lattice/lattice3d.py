"""Concrete three-dimensional Bravais-lattice geometry."""

from __future__ import annotations
from typing import Self
import numpy as np
from scipy.spatial import ConvexHull, HalfspaceIntersection

from physkit.periodic.lattice.base import (
    FloatArray,
    IntArray,
)

from physkit.periodic.lattice.base import (
    DirectLattice,
    ReciprocalLattice,
    WignerSeitzCell,
    FirstBrillouinZone,
)


class DirectLattice3D(DirectLattice):
    """Three-dimensional direct Bravais lattice."""
    dimension=3

    def __init__(
        self,
        a1: FloatArray,
        a2: FloatArray,
        a3: FloatArray,
    ) -> None:
        a1_array = np.array(a1, dtype=np.float64, copy=True)
        a2_array = np.array(a2, dtype=np.float64, copy=True)
        a3_array = np.array(a3, dtype=np.float64, copy=True)

        self.check_primitive_vector(a1_array)
        self.check_primitive_vector(a2_array)
        self.check_primitive_vector(a3_array)
        self.check_primitive_vector_linearly_independent(
            a1_array, a2_array, a3_array
        )

        self.A: FloatArray = np.column_stack(
            (a1_array, a2_array, a3_array)
        )

    @property
    def a1(self) -> FloatArray:
        return self.A[:,0]

    @property
    def a2(self) -> FloatArray:
        return self.A[:,1]

    @property
    def a3(self) -> FloatArray:
        return self.A[:,2]

    def check_primitive_vector(self, vector: FloatArray) -> None:
        if vector.shape != (3,):
            raise ValueError("a must each have shape (3,).")
        if not np.all(np.isfinite(vector)):
            raise ValueError("primitive vectors must contain finite values.")

    def check_primitive_vector_linearly_independent(self,
        a1: FloatArray,
        a2: FloatArray,
        a3: FloatArray
    ) -> None:
        """Validate the three primitive vectors."""

        A = np.column_stack((a1, a2, a3))
        if np.isclose(np.linalg.det(A), 0.0):
            raise ValueError("a1, a2, and a3 must be linearly independent.")

    @property
    def measure(self) -> float:
        """Return the primitive-cell volume ``|det(A)|``."""
        return float(abs(np.linalg.det(self.A)))

    def vector(self, indices: IntArray) -> FloatArray:
        """Construct direct-lattice vectors from integer modes."""
        mode_array = np.asarray(indices, dtype=np.int64)
        if mode_array.shape[-1:] != (3,):
            raise ValueError("modes must have final dimension 3.")
        return np.asarray(mode_array @ self.A.T, dtype=np.float64)

class ReciprocalLattice3D(ReciprocalLattice):
    """Three-dimensional reciprocal Bravais lattice."""

    dimension = 3

    def __init__(
        self,
        b1: FloatArray,
        b2: FloatArray,
        b3: FloatArray,
    ) -> None:
        # Normalize the constructor arguments into independent float arrays.
        b1_array = np.array(b1, dtype=np.float64, copy=True)
        b2_array = np.array(b2, dtype=np.float64, copy=True)
        b3_array = np.array(b3, dtype=np.float64, copy=True)

        # Validate the normalized arrays before assigning instance state.
        self.check_primitive_vector(b1_array)
        self.check_primitive_vector(b2_array)
        self.check_primitive_vector(b3_array)
        self.check_primitive_vectors_linearly_independent(
            b1_array, b2_array, b3_array,
        )

        # Store the reciprocal primitive vectors as the columns of
        #     B = [b1  b2  b3].

        # Commit the completely validated state to the instance.
        self.B: FloatArray = np.column_stack(
            (b1_array, b2_array, b3_array)
        )

    @property
    def b1(self) -> FloatArray:
        return self.B[:,0]

    @property
    def b2(self) -> FloatArray:
        return self.B[:,1]

    @property
    def b3(self) -> FloatArray:
        return self.B[:,2]

    @staticmethod
    def check_primitive_vector(
        vector: FloatArray,
    ) -> None:
        """
        Validate one reciprocal primitive vector.

        Parameters
        ----------
        vector:
            Reciprocal primitive vector to validate.

        Raises
        ------
        ValueError
            If ``vector`` does not have shape ``(3,)`` or contains
            non-finite values.
        """
        if vector.shape != (3,):
            raise ValueError(
                "Each reciprocal primitive vector must have shape (3,)."
            )

        if not np.all(np.isfinite(vector)):
            raise ValueError(
                "Reciprocal primitive vectors must contain only "
                "finite values."
            )

    @staticmethod
    def check_primitive_vectors_linearly_independent(
        b1: FloatArray,
        b2: FloatArray,
        b3: FloatArray,
    ) -> None:
        """
        Validate that the reciprocal primitive vectors are independent.

        Parameters
        ----------
        b1:
            First reciprocal primitive vector.
        b2:
            Second reciprocal primitive vector.
        b3:
            Third reciprocal primitive vector.

        Raises
        ------
        ValueError
            If the reciprocal primitive vectors are linearly dependent.
        """
        B = np.column_stack((b1, b2, b3))

        if np.linalg.matrix_rank(B) < 3:
            raise ValueError(
                "b1, b2, and b3 must be linearly independent."
            )

    @classmethod
    def from_direct_lattice(
        cls,
        direct_lattice: DirectLattice3D,
    ) -> Self:
        """
        Construct a reciprocal lattice from a direct lattice.

        The direct and reciprocal primitive-basis matrices satisfy

        .. math::

            A^{\\mathsf T}B = 2\\pi I.

        Therefore,

        .. math::

            B = 2\\pi A^{-\\mathsf T}.

        Parameters
        ----------
        direct_lattice:
            Three-dimensional direct Bravais lattice.

        Returns
        -------
        Self
            Reciprocal lattice associated with ``direct_lattice``.

        Raises
        ------
        TypeError
            If ``direct_lattice`` is not a ``DirectLattice3D``.
        """
        if not isinstance(direct_lattice, DirectLattice3D):
            raise TypeError(
                "direct_lattice must be a DirectLattice3D instance."
            )

        # Compute the reciprocal primitive-basis matrix
        #
        #     B = 2π A^(-T).
        A = direct_lattice.A
        B = (2.0 * np.pi * np.linalg.inv(A).T)

        # Delegate validation and immutable storage to the primary
        # constructor.
        return cls(
            b1=B[:, 0],
            b2=B[:, 1],
            b3=B[:, 2],
        )

    @property
    def measure(self) -> float:
        """
        Return the reciprocal fundamental-region volume.

        Returns
        -------
        float
            Reciprocal-space volume :math:`|\\det B|`.
        """
        return float(
            abs(
                np.linalg.det(self.B)
            )
        )

    def vector(
        self,
        indices: IntArray,
    ) -> FloatArray:
        """
        Construct reciprocal-lattice vectors from integer indices.

        A reciprocal-lattice vector is

        .. math::

            \\mathbf G_{\\mathbf m}
            =
            m_1\\mathbf b_1
            +
            m_2\\mathbf b_2
            +
            m_3\\mathbf b_3.

        Parameters
        ----------
        indices:
            Integer reciprocal-lattice indices with shape ``(3,)`` or
            ``(..., 3)``.

        Returns
        -------
        FloatArray
            Reciprocal-lattice vectors with the same leading dimensions
            as ``indices``.

        Raises
        ------
        ValueError
            If the final dimension of ``indices`` is not three.
        """
        index_array = np.asarray(
            indices,
            dtype=np.int64,
        )

        if index_array.shape[-1:] != (3,):
            raise ValueError(
                "indices must have shape (3,) or (..., 3)."
            )

        return np.asarray(
            index_array @ self.B.T,
            dtype=np.float64,
        )



class WignerSeitzCell3D(WignerSeitzCell):
    """Wigner--Seitz polyhedron of a three-dimensional direct lattice."""

    def __init__(self, lattice: DirectLattice3D, *, neighbor_shell: int = 2) -> None:
        if not isinstance(lattice, DirectLattice3D):
            raise TypeError("lattice must be a DirectLattice3D instance.")
        if neighbor_shell < 1:
            raise ValueError("neighbor_shell must be at least 1.")
        self._lattice = lattice
        self.neighbor_shell = int(neighbor_shell)
        self.halfspaces: FloatArray = self.construct_halfspaces()
        self.vertices: FloatArray = self.construct_vertices()
        self._hull = ConvexHull(self.vertices)

    @property
    def lattice(self) -> DirectLattice3D:
        """Return the source direct lattice."""
        return self._lattice

    @property
    def measure(self) -> float:
        """Return the Wigner--Seitz-cell volume."""
        return float(self._hull.volume)

    @property
    def faces(self) -> IntArray:
        """Return triangular boundary faces as vertex-index triplets."""
        return np.asarray(self._hull.simplices, dtype=np.int64)

    def construct_halfspaces(self) -> FloatArray:
        """Construct lattice-neighbor half-space inequalities."""
        shell = self.neighbor_shell
        modes = np.array(
            [
                (m1, m2, m3)
                for m1 in range(-shell, shell + 1)
                for m2 in range(-shell, shell + 1)
                for m3 in range(-shell, shell + 1)
                if (m1, m2, m3) != (0, 0, 0)
            ],
            dtype=np.int64,
        )
        vectors = self.lattice.vector(modes)
        offsets = -0.5 * np.sum(vectors**2, axis=1)
        return np.column_stack((vectors, offsets))

    def construct_vertices(self) -> FloatArray:
        """Intersect the half-spaces and return polyhedron vertices."""
        intersection = HalfspaceIntersection(
            self.halfspaces,
            np.zeros(3, dtype=np.float64),
        )
        return np.asarray(intersection.intersections, dtype=np.float64)

    def contains(self, point: FloatArray) -> bool:
        """Return whether a point lies inside the closed polyhedron."""
        point_array = np.asarray(point, dtype=np.float64)
        if point_array.shape != (3,):
            raise ValueError("point must have shape (3,).")
        return bool(np.all(self.halfspaces[:, :3] @ point_array + self.halfspaces[:, 3] <= 1.0e-12))


class FirstBrillouinZone3D(WignerSeitzCell3D, FirstBrillouinZone):
    """First Brillouin-zone polyhedron of a reciprocal lattice."""

    def __init__(
        self,
        reciprocal_lattice: ReciprocalLattice3D,
        *,
        neighbor_shell: int = 2,
    ) -> None:
        if not isinstance(reciprocal_lattice, ReciprocalLattice3D):
            raise TypeError(
                "reciprocal_lattice must be a ReciprocalLattice3D instance."
            )
        self._reciprocal_lattice = reciprocal_lattice
        self._lattice = reciprocal_lattice
        self.neighbor_shell = int(neighbor_shell)
        self.halfspaces = self.construct_halfspaces()
        self.vertices = self.construct_vertices()
        self._hull = ConvexHull(self.vertices)

    @property
    def reciprocal_lattice(self) -> ReciprocalLattice3D:
        """Return the reciprocal lattice that generates the zone."""
        return self._reciprocal_lattice

    def reduce(self, wavevector: FloatArray) -> FloatArray:
        """Reduce one wavevector to the nearest reciprocal-lattice image."""
        k = np.asarray(wavevector, dtype=np.float64)
        if k.shape != (3,):
            raise ValueError("wavevector must have shape (3,).")
        fractional = np.linalg.solve(self.reciprocal_lattice.primitive_basis, k)
        center = np.rint(fractional).astype(np.int64)
        offsets = np.array(
            [
                (i, j, ell)
                for i in range(-2, 3)
                for j in range(-2, 3)
                for ell in range(-2, 3)
            ],
            dtype=np.int64,
        )
        reciprocal_vectors = self.reciprocal_lattice.vector(center + offsets)
        candidates = k[None, :] - reciprocal_vectors
        return candidates[np.argmin(np.sum(candidates**2, axis=1))]
