"""
This script is aiming to show argument unpacking
@Hasan Özdemir 05-13-2022
"""
from typing import Generator


def print_vector(x, y, z):
    print("<%s, %s, %s>" % (x, y, z))


# * operator for unpacking keyword arguments for any iterable including generators
generator_xpr: Generator = (x * x for x in range(3))
print_vector(*generator_xpr)

# ** operator for unpacking keyword arguments from dictionaries
dict_vec = {"y": 0, "z": 1, "x": 1}
print_vector(**dict_vec)
