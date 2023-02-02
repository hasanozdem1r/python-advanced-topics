import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import asyncio


def get_page_content(link: str):
    """
    Fetch parsed HTML for given link
    :param link: website address
    :return: parsed HTML
    """
    page_content = requests.get(link).content
    soup_obj = BeautifulSoup(page_content, "html.parser")
    return soup_obj


def get_top_250(link: str = "https://www.imdb.com/chart/top/") -> pd.DataFrame:
    """
    Get IMDB top 250 movies and metadata
    :param page_content: bs4 object
    :return:
    """
    soup_obj = get_page_content(link=link)

    movies = soup_obj.find("tbody", {
        "class": "lister-list"
    }).find_all("tr", limit=250)

    movies_list = []

    for movie in movies:
        title = movie.find("td", {"class": "titleColumn"}).find("a").text
        link = f'https://www.imdb.com{str(movie.find("td",{"class": "titleColumn"}).find("a").get("href"))}'
        main_characters = str(
            movie.find("td", {
                "class": "titleColumn"
            }).find("a").get("title"))
        release_year: object = movie.find("span", {
            "class": "secondaryInfo"
        }).text.strip("()")
        rating = movie.find("td", {"class": "ratingColumn"}).find("strong").text
        movies_list.append({
            "title": title,
            "link": link,
            "main_characters": main_characters,
            "release_year": release_year,
            "rating": rating,
        })
    movies_df = pd.DataFrame(movies_list)
    # write to csv file
    movies_df.to_csv("../data/imdb_250.csv")
    print(movies_df)


if __name__ == "__main__":
    get_top_250(link="https://www.imdb.com/chart/top/")
