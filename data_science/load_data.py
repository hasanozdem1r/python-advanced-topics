import os
import csv
from typing import List
import pandas as pd
from dask import dataframe as dd
import polars as pl

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = f"{CURRENT_DIR}/../data/traffic_crashes.csv"


# with csv core package
def read_csv_1(
    file_path: str,
    chunk_size: int = None,
    mode: str = "r",
    delimiter: str = ";",
    encoding: str = "utf-8",
) -> List[List[str]]:
    """
    Reads a CSV file and returns its content as a list of lists, where each list corresponds to a row in the file.

    :param file_path: The path of the CSV file to read.
    :param chunk_size: The number of rows to read at a time. If None, the entire file will be read at once.
    :param mode: The mode to open the file in ('r' for read, 'w' for write, etc.).
    :param delimiter: The delimiter character used in the CSV file.
    :param encoding: The encoding of the CSV file.
    :return: A list of lists representing the content of the CSV file.
    """
    rows = []
    with open(file_path, mode=mode, encoding=encoding, newline="") as file:
        reader = csv.reader(file, delimiter=delimiter)
        if chunk_size is not None:
            while True:
                chunk = [row for i, row in enumerate(reader) if i < chunk_size]
                if not chunk:
                    break
                rows.extend(chunk)
        else:
            rows = [row for row in reader]
    return rows


# with pandas
def read_csv_2(file_path: str,
               chunk_size: int = None,
               delimiter: str = ";",
               encoding: str = "utf8") -> pd.DataFrame:
    """
    Read a CSV file into a Pandas DataFrame.

    :param file_path: The path to the CSV file.
    :param chunk_size: The number of rows to read per chunk. If None, the entire file is read at once., defaults to None
    :param delimiter: The delimiter used in the CSV file., defaults to ';'
    :param encoding: The encoding used to read the CSV file., defaults to 'utf8'
    :return: A Pandas DataFrame containing the data from the CSV file.
    """
    if chunk_size is not None:
        chunks = []
        for chunk in pd.read_csv(
                filepath_or_buffer=file_path,
                chunksize=chunk_size,
                delimiter=delimiter,
                encoding=encoding,
        ):
            chunks.append(chunk)
        df = pd.concat(chunks)
    else:
        df = pd.read_csv(filepath_or_buffer=file_path,
                         delimiter=delimiter,
                         encoding=encoding)
    return df


# with dask
def read_csv_3(file_path: str,
               chunk_size: int = None,
               delimiter: str = ";",
               encoding: str = "utf8"):
    if chunk_size is not None:
        df = dd.read_csv(file_path,
                         chunksize=chunk_size,
                         delimiter=delimiter,
                         encoding=encoding)
    else:
        df = dd.read_csv(file_path, delimiter=delimiter, encoding=encoding)
    return df


# with polars
def read_csv_4(file_path: str,
               chunk_size: int = None,
               delimiter: str = ";",
               encoding: str = "utf8"):
    if chunk_size is not None:
        chunks = []
        for df in pl.read_csv(
                source=file_path,
                batch_size=chunk_size,
                separator=delimiter,
                encoding=encoding,
        ):
            chunks.append(df)
        return pl.concat(chunks)
    else:
        return pl.read_csv(file_path, delimiter=delimiter, encoding=encoding)


if __name__ == "__main__":
    read_csv_1(file_path=DATA_PATH, chunk_size=1000)
    read_csv_2(file_path=DATA_PATH, chunk_size=1000)
    read_csv_3(file_path=DATA_PATH, chunk_size=1000)
    read_csv_4(file_path=DATA_PATH, chunk_size=1000)
