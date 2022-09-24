"""
This script is used to show difference between is and == operator
@Hasan Ozdemir 05-13-2022
"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]
# let's inspect these variables
print(type(a), a)
print(type(b), b)
# The == operator compares by checking for equality
print(a == b)
print(a == c)
# The is operator, compares identities
print(a is b)
print(a is c)
