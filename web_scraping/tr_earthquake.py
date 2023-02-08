import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import asyncio
from typing import List, Dict
import io
import re
import numpy as np

BASE_LINK = "http://www.koeri.boun.edu.tr/scripts/lst9.asp"
COLUMNS: List[str] = [
    "Tarih - Saat", "Enlem(N)", "Boylam(E)", "Derinlik(km)", "MD", "ML", "MW",
    "Lokasyon", "Çözüm Niteliği", "Son durum"
]


def fetch_earthquake_data(link: str, parser="html.parser"):
    """
    Fetch parsed HTML for given link
    :param link: website address
    :return: parsed HTML
    """
    # use fake User-Agent to deal 403 Forbidden
    headers: Dict[str, str] = {
        'User-Agent':
            'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
    }
    page_content = requests.get(link, headers=headers).content
    soup_obj = BeautifulSoup(page_content, parser)
    # get table data
    table_data = soup_obj.find("pre").text[586:]
    return table_data


def prepare_df(df_data: List[str], columns: List[str]) -> pd.DataFrame:
    df = pd.DataFrame(df_data)
    df.dropna(subset=columns, how='all', inplace=True)
    df.to_csv("../data/tr_earthquake.csv")
    return df


def text_cleanup(text: str, columns: List[str]) -> List[str]:
    """
    Clean single and multiple spaces and split data by \n to map with dataframe
    :param text: _description_
    :param columns: _description_
    :return: _description_
    """
    df_data: List[str] = []
    # convert to list by splitting \n
    lines: List[str] = text.split("\n")
    for line in lines:
        # replace single space with underscore
        line = re.sub(r'(?<=\S)\s(?=\S)', '_', line)
        # replace multiple space with single space
        fixed_line = " ".join(line.split())
        # split elements by single space
        fixed_line = fixed_line.split()
        row = {}
        for i, column_name in enumerate(columns):
            try:
                row[column_name] = fixed_line[i]
            except IndexError:
                row[column_name] = np.NaN
        df_data.append(row)
    return df_data


if __name__ == "__main__":
    data = fetch_earthquake_data(link=BASE_LINK)
    text_df = text_cleanup(text=data, columns=COLUMNS)
    df = prepare_df(df_data=text_df, columns=COLUMNS)
