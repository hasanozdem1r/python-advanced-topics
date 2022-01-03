
from requests import get
from bs4 import BeautifulSoup
from pandas import DataFrame


class WorldTrends:

    def __init__(self,country_code:str)->None:
        """
        This method used to initialize bs4 object and containers will be used for further needs
        :param country_code: <str> Country code is a unique representation of country
        """
        self.link=get(f"https://www.alexa.com/topsites/countries/{country_code.upper()}").content
        self.soup_obj = BeautifulSoup(self.link, 'html.parser')
        # container to keep trend details
        self.trends_details:list=list()

    def get_trend_searches(self):
        trends=self.soup_obj.find("div", {"class": "tableContainer"}).find_all("div", {"class": "tr site-listing"})
        for trend in trends:
            trend_site_link:str=(trend.find("a").text).replace('\n','')
            trend_details=[item.text for item in trend.find_all('p')]
            daily_time_on_site:str=trend_details[1]
            daily_page_views_per_visitor: float = float(trend_details[2])
            traffic_percentage_from_search: float = float(trend_details[3].replace('%',''))
            total_sites_linking_in: int = int(trend_details[4].replace(',',''))
            self.trends_details.append(
                {
                    'trend_site_link': trend_site_link,
                    'daily_time_on_site': daily_time_on_site,
                    'daily_page_views_per_visitor': daily_page_views_per_visitor,
                    'traffic_percentage_from_search': traffic_percentage_from_search,
                    'total_sites_linking_in': total_sites_linking_in
                }
            )
        # initialize dataframe
        trends_df=DataFrame(self.trends_details)
        return trends_df

if __name__=='__main__':
    # example links -> # https://www.alexa.com/topsites/countries/RU or https://www.alexa.com/topsites/countries/TR
    world_obj=WorldTrends("Tr")
    world_obj.get_trend_searches()