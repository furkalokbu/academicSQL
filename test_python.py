import unittest


def factorial(n):
            
    """ Return the factorial of n, an exact integer >=0
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(6)
    720
    """
        
    import math

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")

    result = 1
    factor = 2

    while factor <= n:
        result *= factor
        factor += 1

    return result

def test_range():
    assert [factorial(n) for n in range(6)] == [1, 1, 2, 6, 24, 120]


class TestCalculation(unittest.TestCase):
    def test_on_range(self):
        self.assertEqual([factorial(n) for n in range(6)], [1, 1, 2, 6, 24, 120])
    
    def test_on_number(self):
        self.assertEqual(factorial(6), 720) 

if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    # unittest.main()
 