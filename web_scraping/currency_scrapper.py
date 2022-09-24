from requests import get
from bs4 import BeautifulSoup


def currency_calculate(rate_of_currency: float,
                       amount_of_money: float) -> float:
    """
    This method is used to convert TRY to EURO
    :rate: <float>  rate of currency
    :amount_try: <float> amount of currency
    return <float> converted amount
    """
    calculated_amount = rate_of_currency * amount_of_money
    return calculated_amount


# example -> currency_from=TRY, currency_to=USD -> 0.067
def get_currency_rate(currency_from: str, currency_to: str) -> float:
    """
    This method is used to scrap real time currency from x-rates.com. This method return us rate of given comparision
    @param currency_from: <str> currency from
    @param currency_to: <str> currency to
    return rate: <float> rate of target currency
    """
    currency_from = currency_from.upper()
    currency_to = currency_to.upper()
    request_str: str = f"https://www.x-rates.com/calculator/?from={currency_from}&to={currency_to}&amount=1"
    page = get(request_str)
    soup = BeautifulSoup(page.text, "html.parser")

    part1 = soup.find(class_="ccOutputTrail").previous_sibling
    part2 = soup.find(class_="ccOutputTrail").get_text(strip=True)
    rate = "{}{}".format(part1, part2)
    return float(rate)
