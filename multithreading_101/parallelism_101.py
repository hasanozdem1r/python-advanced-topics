import multiprocessing
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))



if __name__ == "__main__":
    for i in range(5):
        t = multiprocessing.Process(target=worker, args=(i,))
        t.start()
    print("All Processes are queued, let's see when they finish!")