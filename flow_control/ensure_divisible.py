def ensure_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    else:  # no break
        items.append(divisor)
        return divisor


items = [1, 23, 24, 51, 52, 15, 12, 5, 1, 12, 24, 36]
divisor = 12
dividend = ensure_divisible(items, divisor)
print(f"{items} contains {dividend} which is multiple of {divisor}".format(**locals()))
