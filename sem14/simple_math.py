"""simple math module

This module provides some simple math functions

>>> add(1, 2) + subtract(1, 2)
2

"""


def add(a: float, b: float) -> float:
    """function that adds two numbers

    >>> add(1, 2)
    3

    >>> add(1.5, 2.5)
    4.0

    Args:
        a (float): first number
        b (float): second number

    Returns:
        float: result
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """function that subtracts two numbers

    >>> subtract(1, 2)
    -1

    >>> subtract(1.5, 2.5)
    -1.0

    Args:
        a (float): first number
        b (float): second number

    Returns:
        float: result
    """
    return a - b


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    print("All tests passed!")
