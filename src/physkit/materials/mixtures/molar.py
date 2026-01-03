from typing import List, Optional
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class MolarMixture():
  """
  Molar mixture defined by mole fractions.

  Parameters
  ----------
  names : list of str
      Species names.
  X_arr : np.ndarray
      Mole fractions corresponding to each species.

  Notes
  -----
  Mole fractions satisfy:
      - X_i >= 0
      - sum_i X_i = 1
  """
  names: List[str]
  X_arr: np.ndarray
  n_total: Optional[float] = None

  def __post_init__(self):
    """
    Validate mole-fraction constraints after initialization.
    """
    X = np.asarray(self.X_arr, dtype=float)
    if len(self.names) != X.size:
      raise ValueError("names and X_arr must have the same length")
    if np.any(X < 0):
      raise ValueError("Mole fractions must be non-negative")
    if not np.isclose(X.sum(), 1.0):
      raise ValueError("Mole fractions must sum to 1")
    object.__setattr__(self, "X_arr", X)

  def mole_fraction(self,name) -> float:
    """
    Return the mole fraction of a given species.

    Parameters
    ----------
    name : str
        Species name.

    Returns
    -------
    float
        Mole fraction of the specified species.

    Raises
    ------
    KeyError
        If the species is not present in the mixture.
    """
    try:
      i = self.names.index(name)
    except ValueError:
      raise KeyError(f"Species '{name}' not in mixture")

    return float(self.X_arr[i])

  @staticmethod
  def from_moles(
      names: List[str],
      n_arr: List[float] | np.ndarray
  ) -> "MolarMixture":
    """
    Construct a MolarMixture from molar amounts.

    Parameters
    ----------
    names : list of str
        Species names.
    n_arr : array-like
        Molar amounts for each species.

    Returns
    -------
    MolarMixture
        Mixture expressed in mole fractions.

    Raises
    ------
    ValueError
        If any molar amount is negative or total moles is zero.
    """
    n = np.asarray(n_arr, dtype=float)

    if np.any(n < 0):
        raise ValueError("Moles must be non-negative")

    n_total = n.sum()
    if n_total <= 0:
        raise ValueError("Total moles must be positive")

    X_arr = n / n_total
    return MolarMixture(
        names=names, 
        X_arr=X_arr, 
        n_total=n_total)
  