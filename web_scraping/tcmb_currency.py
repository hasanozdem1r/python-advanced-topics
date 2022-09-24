import requests
from bs4 import BeautifulSoup
from time import sleep

initial_link = "https://www.dunya.com/finans/doviz/banka-gise-fiyatlari"
page_content = requests.get(initial_link).content
soup_obj = BeautifulSoup(page_content, "html.parser")
currencies = soup_obj.find("tbody").find_all("tr", limit=100)
cur_list = list()
print(len(currencies))
for currency in currencies:
    currency_name = str(currency.find("th").text)
    print(currency_name)
