import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import asyncio
from typing import List, Dict
import io
import re
import numpy as np


def handle_index_error(data: List, index: int):
    if len(data) <= index:
        return np.NaN
    else:
        return data[index]


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
    data = soup_obj.find("pre").text[586:]
    return data


def text_cleanup(text: str):
    text_df: List[str] = []
    # convert to list by \n
    lines: List[str] = text.split("\n")
    for line in lines:
        # replace single space with underscore
        line = re.sub(r'(?<=\S)\s(?=\S)', '_', line)
        # replace multiple space with single space
        fixed_line = " ".join(line.split())
        fixed_line = fixed_line.split()
        text_df.append({
            "Tarih - Saat": handle_index_error(data=fixed_line, index=0),
            "Enlem(N)": handle_index_error(data=fixed_line, index=1),
            "Boylam(E)": handle_index_error(data=fixed_line, index=2),
            "Derinlik(km)": handle_index_error(data=fixed_line, index=3),
            "MD": handle_index_error(data=fixed_line, index=4),
            "ML": handle_index_error(data=fixed_line, index=5),
            "MW": handle_index_error(data=fixed_line, index=6),
            "Lokasyon": handle_index_error(data=fixed_line, index=7),
            "Lokasyon": handle_index_error(data=fixed_line, index=8),
            "Son durum": handle_index_error(data=fixed_line, index=9),
        })
    text_df = pd.DataFrame(text_df)
    text_df.dropna(subset=[
        "Tarih - Saat", "Enlem(N)", "Boylam(E)", "Derinlik(km)", "MD", "ML",
        "MW", "Lokasyon", "Lokasyon", "Son durum"
    ],
                   how='all',
                   inplace=True)
    text_df.to_csv("../data/tr_earthquake.csv")
    return text_df


if __name__ == "__main__":
    data = fetch_earthquake_data(
        "http://www.koeri.boun.edu.tr/scripts/lst9.asp")
    print(text_cleanup(text=data))
