# imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

class Twitter:

    def __init__(self)->None:
        # global class variables
        self.initial_link="https://trends24.in/"
        self.content=requests.get(self.initial_link).content
        self.html_content=BeautifulSoup(self.content,'html.parser')
        self.trends_list=list()


    def get_top_trends(self,country:str='',limit:int=None)->pd.DataFrame:
        """
        This method is used to retrieve all top trends from given query.
        param country: <str> Name of country for top trends query
        :return: <pd.Dataframe> return the top trends list
        """
        # if user filtered by country
        if country != '':
            country = country.lower()
            self.initial_link = self.initial_link + f'/{country}/'
        # filter for hourly data
        trends_hourly_data=self.html_content.find_all('div',{'class':'trend-card'})
        for trend_hour in trends_hourly_data:
            # get the top trend time
            trend_time=str(trend_hour.find('h5').text)
            # datetime format -> dd:mm:yyyy_hh:mm
            trend_time=trend_time.replace(' ','_')[:-3]
            trends_hour=trend_hour.find('ol',{'class':'trend-card__list'}).find_all('li')
            # loop through top 10 for each time
            for trend in trends_hour:
                # append to the list
                self.trends_list.append(
                    {
                        f'{str(trend_time)}': str(trend.find('a').text).encode('utf-8')
                    }
                )
        # create pandas dataframe
        trends_df = pd.DataFrame(self.trends_list)
        # return
        return trends_df

twitter_obj=Twitter()
twitter_obj.get_top_trends('Russia')