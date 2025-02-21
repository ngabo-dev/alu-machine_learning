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
            self.lambtha = float(sum(data) / len(data))

    def factorial(self, n):
        """
        Computes the factorial of n.
        """
        if n == 0 or n == 1:
            return 1
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

    def exp(self, x):
        """
        Computes e^x using a Taylor series approximation.
        """
        result = 1
        term = 1
        for i in range(1, 20):  # 20 terms for precision
            term *= x / i
            result += term
        return result

    def pmf(self, k):
        """
        Calculates the PMF for a given number of successes k.

        Args:
            k (int): Number of occurrences.

        Returns:
            float: PMF value for k.
        """
        k = int(k)
        if k < 0:
            return 0
        return (self.lambtha ** k * self.exp(-self.lambtha)) / self.factorial(k)


if __name__ == '__main__':
    # Example data (without numpy)
    data = [
        2, 5, 4, 6, 3, 4, 5, 4, 3, 2, 5, 4, 4, 3, 5, 6, 3, 4,
        2, 4, 5, 3, 4, 4, 5, 3, 4, 5, 3, 4
    ]
    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)
    print('PMF(3):', p1.pmf(3))

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)
    print('PMF(3):', p2.pmf(3))

    try:
        p3 = Poisson(lambtha=-1)
    except ValueError as e:
        print(e)

    try:
        p4 = Poisson([1])  # Test for less than 2 data points
    except ValueError as e:
        print(e)
