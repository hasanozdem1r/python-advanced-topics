# A common use case of generators is to work with data streams or large files, like CSV files.


def csv_reader(file_name: str):
    for row in open(file=file_name, mode='r'):
        yield row


if __name__ == '__main__':
    for _ in csv_reader('lyrics.txt'):
        print(_)

# yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.
# Instead, the state of the function is remembered. That way, when next() is
# called on a generator object (either explicitly or implicitly within a for loop), the previously yielded variable num is incremented, and then yielded again.
