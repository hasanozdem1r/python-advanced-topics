class Stack:
    def __init__(self, stack: list, capacity: int) -> None:
        """
        Initialize stack
        :param stack: <list> numbers list
        :param capacity: <int> capacity of stack
        """
        self.stack: list = stack
        self.capacity: int = capacity

    def push_item(self, item) -> str:
        """
        Add an element to the top of a stack
        :param item:<int> item you want to push to stack
        :return:
        """
        if len(self.stack) == self.capacity:
            # stack is full
            return "stack capacity is full"
        # stack is not full
        self.stack.append(item)
        return "Item added to stack"

    def pop_item(self) -> list:
        """
        Remove an element from the top of a stack
        :return: remove item and return changed stack
        """
        if len(self.stack) > 0:
            self.stack.remove(self.stack[-1])
            return [self.stack, "item is removed"]
        else:
            return [self.stack, "stack is empty"]

    def is_empty(self) -> bool:
        """
        Check if the stack is empty
        :return: <bool> empty or not
        """
        if len(self.stack) == 0:
            return True
        return False

    def is_full(self) -> bool:
        """
        Check if the stack is full
        :return: <bool> full or not
        """
        if len(self.stack) == self.capacity:
            return True
        return False
