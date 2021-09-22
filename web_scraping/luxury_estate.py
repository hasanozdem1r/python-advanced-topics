import re
import requests
from bs4 import BeautifulSoup





class ScrapeRealEstate:

    def __init__(self,country:str):
        self.link = f'https://www.luxuryestate.com/{country}'

    def scrape_data(self)->list:
        page_content = requests.get(self.link).content
        soup_obj = BeautifulSoup(page_content, 'html.parser')
        estates=soup_obj.find("ul", {"class":"search-list"}).find_all("li",limit=100)
        estates_list=[]
        estate_id=1
        for estate in estates:
            estate_title = self.scrape_estate_title(estate)

            estate_cost = self.scrape_estate_cost(estate)

            estate_m2 = self.scrape_area_house(estate)

            estate_bathroom = self.scrape_estate_bathroom(estate)

            estate_bedroom = self.scrape_estate_bedroom(estate)

            estates_list.append(
                {
                    'estate_title':estate_title,
                    'estate_cost':estate_cost,
                    'estate_m2':estate_m2,
                    'estate_bathroom':estate_bathroom,
                    'estate_baedroom':estate_bedroom
                }
            )
            estate_id += 1

        return estates_list

    def scrape_estate_bedroom(self, estate):
        estate_bedroom = estate.find("div", {"class": "specs"}).find("span", {"aria-label": "Bedrooms"}).text
        estate_bedroom = estate_bedroom.encode('utf-8').decode("utf-8")
        estate_bedroom = re.findall('[0-9]+', estate_bedroom)[0]
        return estate_bedroom

    def scrape_estate_bathroom(self, estate):
        estate_bathroom = estate.find("div", {"class": "specs"}).find("span", {"aria-label": "Bathrooms"}).text
        estate_bathroom = estate_bathroom.encode('utf-8').decode("utf-8")
        estate_bathroom = re.findall('[0-9]+', estate_bathroom)[0]
        return estate_bathroom

    def scrape_estate_cost(self, estate):
        estate_cost = str(estate.find("div", {"class": "price serif-base"}).text)
        estate_cost = re.findall('[0-9,]*', estate_cost)
        estate_cost = int([item for item in estate_cost if item != ''][0].replace(',', ''))
        return estate_cost

    def scrape_estate_title(self, estate):
        estate_title = estate.find("div", {"class": "details_title"}).find("a", {"class": "js_clickable"}).text
        estate_title = estate_title.encode('UTF-8').lower()
        return estate_title

    def scrape_area_house(self, estate):
        estate_m2 = estate.find("div", {"class": "specs"}).find("span", {"aria-label": "Internal Surface"}).text
        estate_m2 = re.findall('[0-9]*', estate_m2)
        estate_m2 = int([item for item in estate_m2 if item != ''][0])
        return estate_m2


a=ScrapeRealEstate('germany')
a.scrape_data()
