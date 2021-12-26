"""
Twitter class helper methods
@Hasan Özdemir 2021
"""


def filter_by_country(country):
    """
    This method used to filter query by country name
    :param country: <str> Name of country for top trends query
    :return: <str> query link to fetch data
    """
    if country != '':
        country = country.lower()
        # update the query
        initial_link = f'https://trends24.in//{country}/'
        return initial_link
    else:
        # fetch worldwide top trends
        initial_link = "https://trends24.in/"
        return initial_link


def filter_by_quantity(limit: int, trends_hourly_data: list) -> int:
    """
    This method used to filter query by number of data from last hour to till given limit
    :param limit: <int> fetch limit
    :param trends_hourly_data: bs4 object to get size of limit if not user passed
    :return: <int> fetch limit
    """
    if limit:
        # update query limit
        limit = limit
    else:
        # query all top trends
        limit = len(trends_hourly_data)
    return limit


def format_time(trend_time: str) -> str:
    """
    This method is used to format query time. Formatting includes space replacements and deleting second
    :param trend_time: <str> not formatted datetime
    :return: <str> formatted datetime
    """
    # datatime old format -> dd:mm:yyyy hh:mm:ss
    # datetime new format -> dd:mm:yyyy_hh:mm
    trend_time = trend_time.replace(' ', '_')[:-3]
    return trend_time


if '__main__' == __name__:
    print('Twitter Helpers Test')
