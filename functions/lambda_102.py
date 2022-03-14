"""
This script is created to understand difference between regular functions and lambda functions
Hasan Özdemir 01/07/2021
"""
add = lambda x, y: x + y
print(add(5, 3))
"""
Why the big fuss about lambdas? Conceptually, the lambda expression lambda x, y: x + y is the same as declaring a 
function with def, but just written inline. The key difference here is that I didn’t have to bind the function object 
to a name before I used it. I simply stated the expression I wanted to compute as part of a lambda, 
and then immediately evaluated it by calling the lambda expression like a regular function. """
print((lambda x, y: x + y)(5, 3))
"""
There’s another syntactic difference between lambdas and regular function definitions. 
Lambda functions are restricted to a single expression. 
This means a lambda function can’t use statements or annotations—not even a return statement.
Executing a lambda function evaluates its expression and then automatically returns
the expression’s result, so there’s always an implicit return statement.
"""
tuples = [(1, "d"), (2, "b"), (4, "a"), (3, "c")]
print(sorted(tuples, key=lambda x: x[0]))
