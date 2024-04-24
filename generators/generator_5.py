def chunked_file_reader(filename, chunk_size=1024):
    """Generator to read a text file in chunks.

    Args:
        filename (str): The path to the text file.
        chunk_size (int): The desired size of each chunk (in bytes).
    """
    with open(filename, 'r') as file:
        while True:
            data = file.read(chunk_size)
            if not data:  # End of file
                break
            yield data


if __name__ == '__main__':
    for _ in chunked_file_reader('lyrics.txt', chunk_size=10):
        print(f'Chunk --> {_}')
