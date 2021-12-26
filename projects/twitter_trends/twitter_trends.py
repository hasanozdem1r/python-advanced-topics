"""
Twitter class is created to fetch Twitter Top Trends
@Hasan Özdemir 2021
"""
# import bs4 and request lib
from requests import get
from bs4 import BeautifulSoup
from pandas import DataFrame
# import helpers
from twitter_helpers import *


class Twitter:

    def __init__(self) -> None:
        """
        This constructor initialized necessary variables, containers
        """
        self.html_content = None
        self.initial_link = None
        self.content = None
        self.trends_list = list()

    def get_top_trends(self, country: str = '', limit: int = 0) -> DataFrame:
        """
        This method is used to retrieve all top trends from given query.
        param country: <str> Name of country for top trends query
        param limit: <int> fetch limit
        :return: <pd.Dataframe> return the top trends list
        """
        # if user filtered by country
        self.initial_link = filter_by_country(country)

        self.content = get(self.initial_link).content
        self.html_content = BeautifulSoup(self.content, 'html.parser')

        # filter for hourly data
        trends_hourly_data = self.html_content.find_all('div', {'class': 'trend-card'})

        # if user filtered number of query by times.
        # from last hour to till user want will fetch data
        limit = filter_by_quantity(limit, trends_hourly_data)

        for index in range(limit):
            # get the top trend time
            trend_time = str(trends_hourly_data[index].find('h5').text)
            # datetime format -> dd:mm:yyyy_hh:mm
            trend_time = format_time(trend_time)
            trends_hour = trends_hourly_data[index].find('ol', {'class': 'trend-card__list'}).find_all('li')
            # loop through top 10 for each time
            for trend in trends_hour:
                # append to the list
                self.trends_list.append(
                    {
                        f'{str(trend_time)}': str(trend.find('a').text).encode('utf-8')
                    }
                )
        # create pandas dataframe
        trends_df = DataFrame(self.trends_list)
        # return
        return trends_df


if '__main__' == __name__:
    twitter_obj = Twitter()
    twitter_obj.get_top_trends('Russia', limit=10)
