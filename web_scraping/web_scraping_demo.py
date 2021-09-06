import csv

import requests,re
from bs4 import BeautifulSoup
import os,pickle

PAGE="http://localhost:8000/auto_mpg.html"

def process_car_block(soup):
    """Extract information from repeated divisions"""
    car_blocks=soup.find_all("div", class_="car_block")
    rows=[]
    for c_b in car_blocks:
        row = extract_data(c_b, soup)
        rows.append(row)

    print(f'We have {len(rows)} rows of scraped car data')
    print(rows[0])
    print(rows[-1])


    # Export a CSV file
    with open('scraped_cars.csv','w') as file:
        writer=csv.DictWriter(file,fieldnames=row.keys())
        writer.writeheader()
        writer.writerows(rows)

    # Create a Pandas DF

    # Review our data

    # Investigate relationships graphically

def extract_data(c_b, soup):
    name: str = c_b.find('span', class_='car_name').text

    cylinders = extract_cylinders(c_b)

    weight = extract_weight(c_b)

    territory, year = extract_territory_year(soup)

    acceleration = float(c_b.find('span', class_='acceleration').text)
    assert acceleration > 0, f'Expecting acceleration to be a positive not{acceleration}'

    mpg = extract_mpg(c_b)

    horse_power = extract_hp(c_b)

    displacement = extract_displacement(c_b.text)
    row = dict(name=name, cylinders=cylinders, weight=weight, year=year, territory=territory, \
               accelaration=acceleration, mpg=mpg, horse_power=horse_power, displacement=displacement)
    return row

def extract_cylinders(c_b):
    cylinders: str = c_b.find('span', class_='cylinders').text
    cylinders: int = int(cylinders)
    assert cylinders > 0, f'Expecting cylinders to be positive not {cylinders}'
    return cylinders

def extract_weight(c_b):
    weight: str = c_b.find('span', class_="weight").text
    weight: int = int(weight.replace(',', ''))
    assert weight > 0, f'Expecting weight to be positive not {weight}'
    return weight

def extract_territory_year(soup):
    car_from: str = soup.find('span', class_='from').text
    year, territory = car_from.strip('()').split(',')
    year: int = int(year.strip())
    assert year > 0, f'Expecting year to be a positive not {year}'
    territory: str = territory.strip()
    assert len(territory) > 0, f'Expecting territory to be useful string not {territory}'
    return territory, year

def extract_hp(c_b):
    horse_power = c_b.find('span', class_='horsepower').text
    try:
        horse_power = float(horse_power)
        assert horse_power > 30, f'Expecting reasonable horse power not {horse_power}'
    except ValueError:
        horse_power = 'NULL'
    return horse_power

def extract_mpg(c_b):
    try:
        mpg: str = c_b.find('span', class_='mpg').text
        mpg: float = float(mpg.split(' ')[0])
    except ValueError:
        mpg = "NULL"
    return mpg

def extract_displacement(text):
    displacement = re.findall(r'.* (\d+.\d+) cubic inches', text)[0]
    displacement = float(displacement)
    assert displacement > 60, f'Expecting a reasonable displacement not [{displacement}'
    return displacement


if __name__=="__main__":
    filename = 'scraped_page_result.pickle'
    if os.path.exists(filename):
        with open(filename,'rb') as file:
            print(f'Loading cached {filename}')
            result=pickle.load(file)
    else:
        print(f'Fetching {PAGE} from the internet')
        result = requests.get(PAGE)
        with open(filename,'wb') as file:
            print(f'Writing cached {filename}')
            pickle.dump(result,file)

    assert result.status_code==200, f'Got status code{result.status_code}\'' \
                                    f'which isn"t a success'
    source=result.text
    soup=BeautifulSoup(source,"html.parser")
    process_car_block(soup)


