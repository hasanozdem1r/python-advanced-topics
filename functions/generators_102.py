def function_counter():
    num = 0

    def count():
        nonlocal num
        num += 1
        return num

    return count


def generator_counter():
    num = 0
    while True:
        num += 1
        yield num


function = function_counter()
generator = generator_counter()

print(function())
print(function())
print(function())
print(function())
print("----------")
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


def basic_generator():
    yield "First"
    yield "Second"
    yield "Third"


gen_101 = basic_generator()
print(next(gen_101))
print(next(gen_101))
print(next(gen_101))
print(next(gen_101))
