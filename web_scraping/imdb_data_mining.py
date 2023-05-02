import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import asyncio
from typing import List, Dict


def get_page_content(link: str, parser="html.parser"):
    """
    Fetch parsed HTML for given link
    :param link: website address
    :return: parsed HTML
    """
    # use fake User-Agent to deal 403 Forbidden
    headers: Dict[str, str] = {
        "User-Agent":
            "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    }
    page_content = requests.get(link, headers=headers).content
    soup_obj = BeautifulSoup(page_content, parser)
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


def get_movie_detail(links: List[str]):
    movie_details: List = []
    for link in links:
        soup_obj = get_page_content(link=link)
        # get description
        description = soup_obj.find("span", {"class": "sc-16ede01-0"}).text
        soup_obj = get_page_content(link=link, parser="lxml")
        # get director with xpath
        director = soup_obj.find(
            xpath=
            '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/ul/li[1]/div/ul/li/a'
        ).text
        print(director)
        movie_details.append({
            "link": link,
            "description": description,
        })


if __name__ == "__main__":
    # get_top_250(link="https://www.imdb.com/chart/top/")
    get_movie_detail(["https://www.imdb.com/title/tt0068646/"])
