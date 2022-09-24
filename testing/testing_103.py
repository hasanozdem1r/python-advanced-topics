"""
This script is created to show fundamental of testing and doctest
@Hasan Özdemir 01/13/2022
"""
"""
The doctest module searches for pieces of text that look like interactive Python ses‐
sions in docstrings, and then executes those sessions to verify that they work exactly
as shown
"""


def square(x):
    """Squares x.
    >>> square(2)
    4
    >>> square(-2)
    4
    >>> square(-3)
    9
    """
    return x * x


def triple(x):
    """Triples x.
    >>> triple(3)
    9
    >>> triple(4)
    12
    >>> triple(-3)
    -9
    """
    return x * 3


"""
Doctests serve a different purpose than proper unit tests. They are usually less
detailed and don’t catch special cases or obscure regression bugs. They are useful for happy path.
"""

if __name__ == "__main__":
    import doctest

    doctest.testmod()
