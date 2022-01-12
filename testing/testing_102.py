"""
This script is created to show fundamental of testing and Monkey Patch
@Hasan Özdemir 01/13/2022
"""

"""
A monkey patch is code that modifies or replaces other existing code at runtime.
Example 
from math import pi
print(pi) # 3.141592653589793
pi=3.2 # monkey-patch the value of Pi in the math module
print(pi) # 3.2
"""

"""
1.Use Mock if you want to replace some interface elements(passing args) of the object under test
2.Use patch if you want to replace internal call to some objects and imported modules of the object under test
3.Always provide spec from the object you are mocking
    - With patch you can always provide autospec
    - With Mock you can provide spec
    - Instead of Mock, you can use create_autospec, which intended to create Mock objects with specification.
"""

#TODO CODE EXAMPLES TO BE DONE