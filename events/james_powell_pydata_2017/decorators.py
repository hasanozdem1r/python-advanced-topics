# intro to decorators
# Decorators allow developers add extra ability to functions
# without actually changing the function
from time import time


def timer(func):

    def f(x, y):
        b = time()
        rv = func(x, y)
        a = time()
        print(f"Elapsed:{a-b}")
        return rv

    return f


# higher order decorators
def n_times(n):

    def inner(f):

        def wrapper(*args, **kwargs):
            for _ in range(n):
                print("Running {.__name__}".format(f))
                rv = f(*args, **kwargs)
            return rv

        return wrapper

    return inner


@timer
def add(x, y):
    return x + y


@n_times(3)
def sub(x, y):
    return x - y


print("Addition", add(10, 20))
print("Substraction", sub(10, 20))
"""
How to call
python -i decorators.py

"""

# continue from 1.06
