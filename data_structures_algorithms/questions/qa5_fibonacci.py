"""
0,1,1,2,3,5,8,13,21
"""


def fibonacci(n):
    """Generate the Fibonacci sequence up to n"""
    # First two terms
    a, b = 0, 1
    # Check if n is valid
    if n < 0:
        raise ValueError("Input must be non-negative")
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    # Generate the sequence
    fib = [0, 1]
    while b <= n:
        a, b = b, a + b
        fib.append(b)
    return fib[:-1]  # remove the last element, which exceeds n


def fibonacci_recursive(n: int):
    """Generate the Fibonacci sequence up to n using recursion"""
    # Check if n is valid
    if n < 0:
        raise ValueError("Input must be non-negative")
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    # Recursively generate the sequence
    else:
        fib = fibonacci_recursive(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib


if __name__ == "__main__":
    print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8]
    print(fibonacci(0))  # []
    print(fibonacci(1))  # [0]
    print(fibonacci_recursive(10))  # [0, 1, 1, 2, 3, 5, 8]
    print(fibonacci_recursive(0))  # []
    print(fibonacci_recursive(1))  # [0]
