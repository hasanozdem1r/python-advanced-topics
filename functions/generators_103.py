"""
Differences between Generator function and Normal function
1. Generator function contains one or more yield statements.
2. When called, it returns an object (iterator) but does not start execution immediately.
3. Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
4. Once the function yields, the function is paused and the control is transferred to the caller.
5. Local variables and their states are remembered between successive calls.
6. Finally, when the function terminates, StopIteration is raised automatically on further calls.
"""


# A simple generator function
def my_gen():
    n = 1
    print("This is printed first")
    # Generator function contains yield statements
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print("This is printed at last")
    yield n


"""
a=my_gen()
next(a)
next(a)
next(a)
next(a)
"""
# Using for loop
for item in my_gen():
    print(item)
"""
They have lazy execution ( producing items only when asked for ).
For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.
"""

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)
