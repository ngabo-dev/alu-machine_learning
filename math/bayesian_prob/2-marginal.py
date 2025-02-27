#!/usr/bin/env python3
"""
2-marginal.py
Calculates the marginal probability of obtaining the data based on 1-intersection.py.
"""
import numpy as np
from scipy.special import comb

def likelihood(x, n, P):
    """Calculates the likelihood of obtaining the data given P."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")
    return comb(n, x) * (P ** x) * ((1 - P) ** (n - x))

def intersection(x, n, P, Pr):
    """Calculates the intersection of obtaining x and n with each probability in P."""
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any((Pr < 0) | (Pr > 1)):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(Pr.sum(), 1):
        raise ValueError("Pr must sum to 1")
    return likelihood(x, n, P) * Pr

def marginal(x, n, P, Pr):
    """Calculates the marginal probability of obtaining x and n."""
    return np.sum(intersection(x, n, P, Pr))
