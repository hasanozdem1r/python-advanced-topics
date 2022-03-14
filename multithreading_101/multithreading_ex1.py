import threading
from queue import Queue
import time

"""
Each pastry after finish task will pick new task from queee and continue to prepare. 
They don't need to wait each other.
"""
lock = threading.Lock()  # block conflict


def make_cake(cake):
    time.sleep(1)
    with lock:  # block conflict while you printing
        print(threading.current_thread().name, cake)


# Each pastry picks order from queee and prepare
def pastry():
    while True:
        cake = queee.get()
        make_cake(cake)
        queee.task_done()


queee = Queue()
for item in range(4):
    thread = threading.Thread(name="Pastry-" + str(item + 1), target=pastry)
    thread.daemon = True  # main thread wait for all threads to finish
    thread.start()

start = time.perf_counter()
for pasta in range(20):
    queee.put(pasta)
queee.join()  # till task finish queee will stay active
print("Pasta total preparation time:", time.perf_counter() - start)
