# intro to decorators
# Decorators allow developers add extra ability to functions 
# without actually changing the function
from time import time

def timer(func):
    def f(x,y):
        b=time()
        rv=func(x,y)
        a=time()
        print(f'Elapsed:{a-b}')
        return rv
    return f

@timer
def add(x,y):
    return x+y

@timer
def sub(x,y):
    return x-y

print('Addition',add(10,20))
print('Substraction',sub(10,20))

"""
How to call
python -i decorators.py

"""