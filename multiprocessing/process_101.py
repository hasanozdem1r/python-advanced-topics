import multiprocessing

def calculate_square(numbers, result, square_sum):
    """Function to calculate square of numbers."""
    for idx, number in enumerate(numbers):
        result[idx] = number * number
    square_sum.value = sum(result)

    
# Process
if __name__ == '__main__':
    numbers = range(10)
    #  `multiprocessing.Array` and `multiprocessing.Value` 
    # to share data between the main process and the subprocess.
    result = multiprocessing.Array('i', 10)
    square_sum = multiprocessing.Value('i')

    # Process initialization
    process = multiprocessing.Process(target=calculate_square, args=(numbers, result, square_sum))

    # Start and join the process
    process.start()
    process.join()

    print(f"Squares: {list(result)}")
    print(f"Sum of squares: {square_sum.value}")
# https://superfastpython.com/multiprocessing-in-python/