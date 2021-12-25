"""
You can assign functions to variables, store them in data structures,
pass them as arguments to other functions,
and even return them as values from other functions.
"""


def yell(text):
    return text.upper() + '!'


print(yell('Hello'))
# assign to a variable
"""
This line doesn’t call the function. 
It takes the function object referenced by yell and creates a second name, 
bark, that points to it.
"""
bark = yell
print(bark('woof'))

"""
You can delete the function’s original name (yell). Since
another name (bark) still points to the underlying function
"""
del yell
try:
    print(yell('Hello'))
except Exception as err:
    print('yell function is deleted')
print(bark('woof'))
# Python attaches a string identifier to every function at
# creation time for debugging purposes.
print(bark.__name__)
# Functions Can Be Stored in Data Structures
funcs = [bark, str.lower, str.capitalize]
for f in funcs:
    print(f,f('Hey there !'))

# Functions can be passed to other functions.
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)
greet(bark)
# Functions that can accept other functions as arguments are also called higher-order functions.
# map function
high_list=list(map(bark,['Hello','hey','hi']))
print(high_list)

# Functions Can Be Nested
def speak(text):
    print(text)
    # inner function
    def whisper(text):
        if text=='Hello':
            print('Hi')
        else:
            print('Hello')
    # inner function call
    whisper(text)
speak('Hi')

# Functions Can Capture Local State
def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
print(plus_3(4)) # expected -> 3 + 3