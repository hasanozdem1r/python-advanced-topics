class Queue:

    def __init__(self, queue: list, capacity: int) -> None:
        """
        Initialize queue
        :param stack: <list> numbers list
        :param capacity: <int> capacity of queue
        """
        self.queue: list = queue
        self.capacity: int = capacity

    def enqueue(self, item: int) -> list:
        """
        Add an element to the end of the queue
        :param item: <int> element to add queue
        :return: add item if possible and return changed queue
        """
        if len(self.queue) < self.capacity:
            self.queue.append(item)
            return [self.queue, "Item added to queue"]

        return [self.queue, "Queue capacity is full"]

    def dequeue(self) -> list:
        """
        Remove an element from the front of the queue
        :return: <int> remove item if possible and return changed queue
        """
        if len(self.queue) > 0:
            self.queue.remove(self.queue[0])
            return [self.queue, "Item removed from queue"]
        return [self.queue, "Queue is empty"]

    def is_empty(self) -> bool:
        """
        Check if the queue is empty
        :return: queue is empty or not
        """
        if len(self.queue) == 0:
            return True
        return False

    def is_full(self):
        """
        Check if the queue is full
        :return: queue is full or not
        """
        if len(self.queue) == self.capacity:
            return True
        return False

    def get_peek(self) -> (int, str):
        """
        Get the value of the front of the queue without removing it
        :return: <int> return first item
        """
        if len(self.queue) > 0:
            return self.queue[0]
        return "Queue is empty"
