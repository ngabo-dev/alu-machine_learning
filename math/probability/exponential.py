#!/usr/bin/env python3
"""
This module defines the Exponential distribution class.

The Exponential class represents an exponential distribution and provides
methods for computing the Probability Density Function (PDF) and the
Cumulative Distribution Function (CDF).

Class Constructor:
    - __init__(self, data=None, lambtha=1.0):
        - data: A list of data points used to estimate the distribution.
        - lambtha: The expected number of occurrences in a given time frame.
        - If data is not provided, lambtha is used.
        - Raises a ValueError if lambtha is not a positive value.
        - If data is provided, calculates lambtha from data.
        - Raises a TypeError if data is not a list.
        - Raises a ValueError if data contains fewer than two points.
"""


class Exponential:
    """
    A class that represents an exponential distribution.
    """

    def __init__(self, data=None, lambtha=1.0):
        """
        Initialize the Exponential distribution.
        Args:
            data: List of data points used to estimate the distribution.
            lambtha: Expected number of occurrences in a given time frame.

        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data) / len(data))

    def pdf(self, x):
        """
        Calculate the Probability Density Function (PDF) for a given x.

        Args:
            x

        Returns:
            float
        """
        if x < 0:
            return 0
        return self.lambtha * self.e ** (-self.lambtha * x)

    def cdf(self, x):
        """
        Calculate the Cumulative Distribution Function (CDF) for a given x.

        Args:
            x

        Returns:
            float
        """
        if x < 0:
            return 0
        return 1 - self.e ** (-self.lambtha * x)

    @property
    def e(self):
        """Approximation of the mathematical constant e."""
        return 2.7182818285
