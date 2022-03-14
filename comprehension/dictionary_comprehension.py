"""
This script is used to show dict comprehension
"""

state = ["Ankara", "Warsaw", "Prague"]
capital = ["Turkey", "Poland", "Czechia"]
output_dict = {}

# Using loop for constructing output dictionary
for (key, value) in zip(state, capital):
    output_dict[key] = value

print("Output Dictionary using for loop:", output_dict)

# with comprehension
dict_using_comp = {key: value for (key, value) in zip(state, capital)}

print("Output Dictionary using dictionary comprehensions:", dict_using_comp)
