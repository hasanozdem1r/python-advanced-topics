import sys

# iterators an object that enables a programmer to traverse a container, particularly lists.
# generators a routine that can be used to control the iteration behaviour of a loop. Generator is a very similar to a function that returns a array.

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # list

y = range(0, 10)  # iterator

print(sys.getsizeof(x))  # 136
print(sys.getsizeof(y))  # 48

# Iterator allows us loop through and doesn't store in memory so iterator has only 48 of bytes and list already kept all values has 136 bytes

z = map(lambda i: i**2, x)

for i in z:
    print(i)

print(sys.getsizeof(z))  # 48
