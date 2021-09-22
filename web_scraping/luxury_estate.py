import re
import requests
from bs4 import BeautifulSoup

PAGE='https://www.luxuryestate.com/germany'


page_content=requests.get(PAGE).content

soup_obj=BeautifulSoup(page_content,'html.parser')
estates=soup_obj.find("ul", {"class":"search-list"}).find_all("li",limit=100)
estates_list=[]
estate_id=1
for estate in estates:
    estate_title = estate.find("div", {"class": "details_title"}).find("a",{"class": "js_clickable"}).text
    print(estate_title.encode('UTF-8').lower())

    estate_cost=str(estate.find("div", {"class": "price serif-base"}).text)
    #estate_cost = estate_cost.encode('utf-8').decode("utf-8")
    estate_cost=re.findall('[0-9,]*',estate_cost)
    estate_cost=int([item for item in estate_cost if item!=''][0].replace(',',''))
    print(estate_cost)

    estate_m2=estate.find("div", {"class": "specs"}).find("span", {"aria-label": "Internal Surface"}).text
    estate_m2 = re.findall('[0-9]*', estate_m2)
    estate_m2 = int([item for item in estate_m2 if item != ''][0])
    print(estate_m2)

    estate_bathroom=estate.find("div", {"class": "specs"}).find("span", {"aria-label": "Bathrooms"}).text
    estate_bathroom=estate_bathroom.encode('utf-8').decode("utf-8")
    estate_bathroom=re.findall('[0-9]+',estate_bathroom)
    print(estate_bathroom[0])

    estate_bedroom=estate.find("div", {"class": "specs"}).find("span", {"aria-label": "Bedrooms"}).text
    estate_bedroom=estate_bedroom.encode('utf-8').decode("utf-8")
    estate_bedroom=re.findall('[0-9]+',estate_bedroom)
    print(estate_bedroom[0])


    estates_list.append(
        {
            'estate_title':estate_title,
            'estate_cost':estate_cost,
            'estate_m2':estate_m2,
            'estate_bathroom':estate_bathroom
        }
    )
    estate_id += 1
    
print(estates_list)