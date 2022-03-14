"""
This script is used to show list comprehension
"""

# create a number list with odd numbers > normal way
list_normal = list()
for item in range(1, 25):
    if item % 2 == 1:
        list_normal.append(item)

# create a number list with odd number > comprehension way
list_comprehension = [item for item in range(1, 25) if item % 2 == 1]
print("Normal", list_normal)
print("Comprehension", list_comprehension)
