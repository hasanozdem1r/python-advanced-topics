# Best use cases for assert method
# Ref -> Python Tricks
def apply_discount(product, discount):
    price = int(product["price"] * (1.0 - discount))
    # It will guarantee that, no matter what,
    # discounted prices calculated by this function cannot be lower than 0
    assert 0 <= price <= product["price"]
    return price


shoes = {"name": "Fancy Shoes", "price": 14900}

price = apply_discount(shoes, 1.25)
print(price)
