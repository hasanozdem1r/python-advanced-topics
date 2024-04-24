class Counter:

    def __init__(self, start, end) -> None:
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            result = self.current
            self.current += 1
            return result


if __name__ == '__main__':
    for _ in Counter(1, 10):
        print(_)
