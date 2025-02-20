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
            if not isinstance(lambtha, (int, float)) or lambtha <= 0:  # Check type and positivity
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)  # Ensure lambtha is a float
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))  # Calculate lambtha from data


if __name__ == '__main__':  # This part is for testing, not part of the class itself.
    import numpy as np

    np.random.seed(0)
    data = np.random.poisson(5., 100).tolist()
    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)
