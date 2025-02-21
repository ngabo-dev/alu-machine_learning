#!/usr/bin/env python3

"""
This module defines the Poisson distribution class.
"""


class Poisson:
    """
    Represents a Poisson distribution.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor.

        Args:
            data (list, optional): Data to estimate the distribution.
                Defaults to None.
            lambtha (float, optional): Expected number of occurrences.
                Defaults to 1.

        Raises:
            TypeError: If data is not a list.
            ValueError: If lambtha is not positive or data contains less
                than 2 points.
        """

        if data is None:
            if not isinstance(lambtha, (int, float)) or lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            total = 0
            for x in data:
                total += x
            self.lambtha = float(total / len(data))


    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of "successes".

        Args:
            k (int or float): The number of "successes".

        Returns:
            float: The PMF value for k.
        """
        if not isinstance(k, (int, float)):
          raise TypeError("k must be a number")

        k = int(k)  # Convert k to integer

        if k < 0: # Poisson distribution is for non-negative integers
            return 0

        # Calculate factorial without importing math
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        # Calculate exponential without importing math (approximation)
        exp_val = 1.0
        term = 1.0
        for i in range(1, 10):  # Adjust number of terms for accuracy
            term *= self.lambtha / i
            exp_val += term

        pmf_value = (self.lambtha**k * factorial) / exp_val

        return pmf_value
