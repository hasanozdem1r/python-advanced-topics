import pandas as pd
import requests
from bs4 import BeautifulSoup


PAGE='https://www.imdb.com/chart/top/'

page_content=requests.get(PAGE).content

soup_obj=BeautifulSoup(page_content,'html.parser')

movies=soup_obj.find("tbody", {"class":"lister-list"}).find_all("tr",limit=250)

movies_list=[]
movie_order = 1

for movie in movies:
    movie_title = movie.find("td",{"class":"titleColumn"}).find("a").text
    release_year: object = movie.find("span",{"class":"secondaryInfo"}).text.strip("()")
    rating = movie.find("td",{"class":"ratingColumn"}).find("strong").text
    movie_order += 1
    movies_list.append(
        {
            'movie_order':movie_order,
            'movie_title':movie_title,
            'movie_release_year':release_year,
            'movie_rating':rating
        }
    )
movies_df= pd.DataFrame(movies_list)
print(movies_df)


