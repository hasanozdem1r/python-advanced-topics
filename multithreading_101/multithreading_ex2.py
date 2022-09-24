from multiprocessing import Pool
import numpy
import time

if __name__ == "__main__":
    maxnum = 30
    start1 = time.perf_counter()
    pool = Pool()
    squares = pool.map(numpy.sqrt, range(maxnum))
    print(squares)
    print("Total time:{:10.8f}".format(time.perf_counter() - start1))
    start2 = time.perf_counter()
    pool = Pool()
    results = [pool.apply_async(numpy.sqrt, (x,)) for x in range(maxnum)]
    squares2 = [r.get() for r in results]
    print(squares2)
    print("Total time:{:10.8f}".format(time.perf_counter() - start2))
