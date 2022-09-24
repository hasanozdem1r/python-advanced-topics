"""
The Iterator Pattern proposes that the details about how a data structure is traversed
should be moved into an “iterator” object that, from the outside, simply yields one item
after another without exposing the internals of how the data structure is designed.
"""

elements = [("H", 1.008), ("He", 4.003), ("Li", 6.94)]

# You’re not limited to a single name like “tup”...
for tup in elements:
    symbol, weight = tup
    print(symbol, weight)

# ...instead, unpack right inside the "for" statement
for symbol, weight in elements:
    print(symbol, weight)

d = {"H": 1.008, "He": 4.003, "Li": 6.94}

# You don’t need to...
for symbol in d.keys():
    weight = d[symbol]
    print(symbol, weight)

# ...instead, you can simply:
for symbol, weight in d.items():
    print(symbol, weight)
