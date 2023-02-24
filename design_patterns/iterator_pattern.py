"""
FURTHER READING
1. https://refactoring.guru/design-patterns/iterator
2. https://www.toptal.com/python/python-design-patterns#:~:text=groups%20are%20not.-,ITERATOR,-Iterators%20are%20built
"""
from collections.abc import Iterator


class ListIterator(Iterator):
    """
    Iterator Pattern example
    """

    def __init__(self):
        self.items = []
        self.index = 0

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    # Example usage:
    eg_list = ListIterator()
    eg_list.add_item("apple")
    eg_list.add_item("banana")
    eg_list.add_item("cherry")

    for item in eg_list:
        print(item)
