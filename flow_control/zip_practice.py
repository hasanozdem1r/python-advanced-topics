"""
This script used to understand fundamentals of ZIP function
@ Hasan Ozdemir 2021
"""
"""
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

"""
from string import ascii_lowercase, ascii_uppercase

letters_lower = list(ascii_lowercase)
letters_upper = list(ascii_uppercase)
print(letters_upper)
for letters_lower, letters_upper in zip(letters_lower, letters_upper):
    print(letters_lower, letters_upper)
