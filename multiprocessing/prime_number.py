import random
from multiprocessing import Process, Pool
import math
from typing import List
import time
import functools


def measure_time(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        # Execute the original function
        result = func(*args, **kwargs)
        finish_time = time.perf_counter()
        total_time = finish_time - start_time
        print(
            f"Function '{func.__name__}' took {total_time:.4f} seconds to execute"
        )
        return result

    return wrapper


def is_prime(number: int) -> bool:
    root_square = int(math.sqrt(number))
    for i in range(2, root_square):
        if number % i == 0:
            return False
    return True


@measure_time
def process_example(numbers: List[int]) -> None:
    # process class
    process = Process(target=is_prime, args=(random.choice(numbers),))
    process.start()  # start child process
    process.join()  # wait until child process done!


@measure_time
def pool_example(numbers: List[int]) -> None:
    # Pool
    # The pool class creates by default one process per CPU core
    # computation will be distributed across 50 parallel processes, which can significantly speed up CPU-bound tasks.
    with Pool(processes=50) as pool:
        pool.map(func=is_prime, iterable=numbers)


@measure_time
def serial_example(numbers: List[int]) -> None:
    for i in numbers:
        is_prime(number=i)


if __name__ == "__main__":
    sample = [random.randint(a=i - 10, b=i + 10) for i in range(100, 1000000)]
    process_example(numbers=sample)
    pool_example(numbers=sample)
    serial_example(numbers=sample)
