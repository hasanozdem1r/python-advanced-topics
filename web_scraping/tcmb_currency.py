import requests
from bs4 import BeautifulSoup
from time import sleep

initial_link = 'https://www.dunya.com/finans/doviz/banka-gise-fiyatlari'
page_content = requests.get(initial_link).content
soup_obj = BeautifulSoup(page_content, 'html.parser')
currencies = soup_obj.find("tbody").find_all("tr", limit=100)
print(len(currencies))
cur_list=list()
for item in currencies:
    pass
    #currency_name=item.find('th').text
    #print(len(currency_name))
    #print(currency_name.encode('UTF8'))
    #currency_info=item.find_all('td') # [None,Alýþ,Satýþ,%change,saat]
    #item1=[str(i.text).encode('UTF8') for i in currency_info]
    #cur_list.append(item1)

#print(cur_list)
