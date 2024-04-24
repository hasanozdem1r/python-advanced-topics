import time


def get_runtime(func, *args, **kwargs):

    def wrapper(func, *args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time: {end-start}')
        return value

    return wrapper


def get_sum_of_args(*args):
    return sum(args)


if __name__ == '__main__':
    print(get_sum_of_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
