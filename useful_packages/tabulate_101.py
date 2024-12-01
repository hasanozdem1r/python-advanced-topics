from tabulate import tabulate
from typing import List


"""
Supported types
list of lists or another iterable of iterables
list or another iterable of dicts (keys as columns)
dict of iterables (keys as columns)
list of dataclasses (field names as columns)
two-dimensional NumPy array
NumPy record arrays (names as columns)
pandas.DataFrame
"""

# list of list
table:List[List] = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
print(tabulate(table,headers=["Day","H2","H3"]))

# for further format take a look !
# https://github.com/astanin/python-tabulate