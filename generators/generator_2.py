# next function()

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # list

y = range(0, 10)  # iterator

z = map(lambda i: i**2, x)  # iterator

# print('next',next(z))

# print('next',next(z))

# print('next',next(z))

# print('__next__', z.__next__())

# print('__next__', z.__next__())

# for i in z:
#     print('Loop',i)

while True:
    try:
        value = next(z)
        print(value)
    except StopIteration:
        print('Done')
        break

a = range(0, 11)

print(next(iter(a)))
