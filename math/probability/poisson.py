#!/usr/bin/env python3

class Poisson:
    """
    Represents a Poisson distribution.
    """
    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor.

        Args:
            data (list, optional): Data to estimate the distribution. Defaults to None.
            lambtha (float, optional): Expected number of occurrences. Defaults to 1.

        Raises:
            TypeError: If data is not a list.
            ValueError: If lambtha is not positive or data contains less than 2 points.
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

            # Calculate mean without numpy
            total = 0
            for x in data:
              total += x
            self.lambtha = float(total / len(data))


# Test cases (without numpy)
if __name__ == '__main__':
    # Simulate Poisson data (without numpy) - Example data
    data = [2, 5, 4, 6, 3, 4, 5, 4, 3, 2, 5, 4, 4, 3, 5, 6, 3, 4, 2, 4, 5, 3, 4, 4, 5, 3, 4, 5, 3, 4] # Example data
    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)

    try:
        p3 = Poisson(lambtha=-1)
    except ValueError as e:
        print(e)

    try:
      p4 = Poisson([1]) # Test for less than 2 data points
    except ValueError as e:
        print(e)
