"""Simple math operations with doctests.

Functions:
- add(x, y): return x + y
- mul(x, y): return x * y

Doctests run with:  python -m doctest -v math_ops.py

Examples
--------
>>> add(2, 3)
5
>>> add(-1, 1)
0
>>> mul(2, 3)
6
>>> mul(-4, -2)
8
>>> mul(7, 0)
0
"""

def add(x, y):
    """Return the sum of x and y.

    >>> add(10, 5)
    15
    >>> add(0, 0)
    0
    """
    return x + y


def mul(x, y):
    """Return the product of x and y.

    >>> mul(3, 4)
    12
    >>> mul(-1, 5)
    -5
    """
    return x * y
