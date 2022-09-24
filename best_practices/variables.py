"""
When it comes to variable and method names, the single underscore prefix has a meaning by convention only
This convention is defined in PEP 8, the most commonly used Python code style guide.
The underscore prefix is meant as a hint to tell another programmer
that a variable or method starting with a single underscore is intended
for internal use.
"""


class Variables:

    def __init__(self):
        self.dollar = 18
        self._euro = 19  # for internal use


def _internal_func():
    return "I am internal func"


"""
Now, if you use a wildcard import to import all the names from the
module, Python will not import names with a leading underscore (unless the module defines an __all__ list that overrides this behavior
"""

# if you import like from variables import *  you cannot reach _internal_func
# you must do like from variables import _internal_func

# Single Trailing Underscore (var_)
# if you want to create some variable which is already used or keyword you can use trailing underscore


def make_object(name, class_):
    print("I am making a class")


# single underscore
"""
Per convention, a single stand-alone underscore is sometimes used as
a name to indicate that a variable is temporary or insignificant
"""
for _ in range(1, 10):
    print(_)
