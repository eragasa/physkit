# physkit/solidstate/lattice.py
# Eugene Joseph M. Ragasa, 2026

import numpy as np
from dataclasses import dataclass
from typing import TypeAlias
Array3D: TypeAlias = np.ndarray
ColumnVector3D: TypeAlias = np.ndarray
RowVector3D: TypeAlias = np.ndarray
Array2D: TypeAlias = np.ndarray

def is_Array2D(r: np.ndarray) -> bool:
    try:
        np.asarray(r, dtype=float).reshape(2,)
        return True
    except Exception:
        return False

def to_Array2D(r: np.ndarray) -> Array2D:
    try:
        return np.asarray(r, dtype=float).reshape(2,)
    except Exception as e:
        raise e

def is_Array3D(r: np.ndarray) -> bool:
    try:
        np.asarray(r, dtype=float).reshape(3,)
        return True
    except Exception:
        return False

def to_Array3D(r: np.ndarray) -> Array3D:
    try:
        return np.asarray(r, dtype=float).reshape(3,)
    except Exception as e:
        raise e

def is_ColumnVector3D(r: np.ndarray) -> bool:
    return True if r.shape==(3,1) else False    

def to_ColumnVector3D(r: np.ndarray) -> ColumnVector3D:
    try:
        return np.asarray(r, dtype=float).reshape(3,1)
    except Exception as e:
        raise e

def is_RowVector3D(r: np.ndarray) -> bool:
    return True if r.shape==(1,3) else True

def to_RowVector3D(r: np.ndarray) -> RowVector3D:
    try:
        return np.asarray(r, dtype=float).reshape(1,3)
    except Exception as e:
        raise e

@dataclass(frozen=True, slots=True)
class DirectLattice2D():
    a1: np.ndarray
    a2: np.ndarray

    def _post_init_(self):
        self.a1 = to_Array2D(self.a1)
        self.a2 = to_Array2D(self.a2)

        object._setattr_(self, "a1", self.a1.copy())
        object._setattr_(self, "a2", self.a2.copy())

    @property
    def A(self) -> np.ndarray:
        """
        Column matrix A = [a1 a2 a3], so that R = A @ n for integer vector n.
        Shape: (3, 3).
        """
        a1 = self.a1
        a2 = self.a2
        return np.column_stack([a1, a2])
    
    @staticmethod
    def from_A(A: np.ndarray) -> "DirectLattice2D":
        return DirectLattice2D(
            a1 = A[0,:],
            a2 = A[1,:]
        )

    def generate(self, 
        nx_min: int, nx_max: int,
        ny_min: int, ny_max: int,
        r: np.ndarray = np.array([0,0]),
        *,
        endpoints: bool = False
    ) -> np.ndarray:
        # 
        # local variables references from class variables
        a1 = self.a1
        a2 = self.a2

        # change loop behavior depending on desired endpoints
        ix_max = nx_max + 1 if endpoints else nx_max
        iy_max = ny_max + 1 if endpoints else ny_max

        R_array = []
        for i in range(nx_min, ix_max):
            for j in range(ny_min, iy_max):
                    R = r + i*a1 + j*a2
                    R_array.append(R)
        return np.asarray(R_array)
        

@dataclass(frozen=True, slots=True)
class DirectLattice():
    a1: np.ndarray
    a2: np.ndarray
    a3: np.ndarray

    def __post_init__(self):
      self.a1 = to_Array3D(self.a1)
      self.a2 = to_Array3D(self.a2)
      self.a3 = to_Array3D(self.a3)

      #copy into the frozen dataclass safely
      object.__setattr__(self, "a1", a1.copy())
      object.__setattr__(self, "a2", a2.copy())
      object.__setattr__(self, "a3", a3.copy())

    @staticmethod
    def from_A(A: np.ndarray) -> "DirectLattice":
        return DirectLattice(
            a1 = A[0,:],
            a2 = A[1,:],
            a3 = A[2,:]
        )
  
    @property
    def A(self) -> np.ndarray:
        """
        Column matrix A = [a1 a2 a3], so that R = A @ n for integer vector n.
        Shape: (3, 3).
        """
        a1 = self.a1
        a2 = self.a2
        a3 = self.a3
        return np.column_stack([a1, a2, a3])

    def generate(self,
        nx_min: int, nx_max: int,
        ny_min: int, ny_max: int,
        nz_min: int, nz_max: int,
        r: np.ndarray = np.array([0,0,0]),
        *,
        endpoints: bool = False
    ) -> np.ndarray:
        # 
        # local variables references from class variables
        a1 = self.a1
        a2 = self.a2
        a3 = self.a3

        # change loop behavior depending on desired endpoints
        ix_max = nx_max + 1 if endpoints else nx_max
        iy_max = ny_max + 1 if endpoints else ny_max
        iz_max = nz_max + 1 if endpoints else nz_max

        R_array = []
        for i in range(nx_min, ix_max):
            for j in range(ny_min, iy_max):
                for k in range(nz_min, iz_max):
                    R = r + i*a1 + j*a2 + k*a3
                    R_array.append(R)
        return np.asarray(R_array)

    @property
    def volume(self):
        a1 = self.a1
        a2 = self.a2
        a3 = self.a3
        return abs(np.dot(a1, np.cross(a2, a3)))

@dataclass(frozen=True, slots=True)
class ReciprocalLattice2D():
    b1: np.ndarray
    b2: np.ndarray

    def _post_init_(self):
        self.b1 = to_Array2D(self.b1)
        self.b2 = to_Array2D(self.b2)

        object._setattr_(self, "b1", self.b1.copy())
        object._setattr_(self, "b2", self.b2.copy())

    @property
    def B(self) -> np.ndarray:
        """
        Column matrix A = [a1 a2 a3], so that R = A @ n for integer vector n.
        Shape: (3, 3).
        """
        b1 = self.b1
        b2 = self.b2
        return np.column_stack([b1, b2])
    
    @staticmethod
    def from_B(B: np.ndarray) -> "ReciprocalLattice2D":
        return ReciprocalLattice2D(
            b1 = B[0,:],
            b2 = B[1,:]
        )
    
    @staticmethod
    def from_DirectLattice(lattice: DirectLattice2D) -> "DirectLattice2D":
        A = lattice.A
        detA = float(np.linalg.det(A))
        if abs(detA) == 0:
            raise ValueError("lattice.A is singular. lattice.a1 and lattice.a2 are linearly dependent")
        
        B = 2.0 * np.pi * np.linalg.inv(A).T
        return ReciprocalLattice2D.from_B(B)
    

    def generate(self, 
        nx_min: int, nx_max: int,
        ny_min: int, ny_max: int,
        r: np.ndarray = np.array([0,0]),
        *,
        endpoints: bool = False
    ) -> np.ndarray:
        # 
        # local variables references from class variables
        b1 = self.b1
        b2 = self.b2

        # change loop behavior depending on desired endpoints
        ix_max = nx_max + 1 if endpoints else nx_max
        iy_max = ny_max + 1 if endpoints else ny_max

        R_array = []
        for i in range(nx_min, ix_max):
            for j in range(ny_min, iy_max):
                    R = r + i*b1 + j*b2
                    R_array.append(R)
        return np.asarray(R_array)
        