"""
@hasanozdemir 09-24-2022
"""
from typing import Dict
import requests
import backoff
from utils import get_api_auth

API_BASE_URL = "https://api.trello.com/"
API_TOKEN = get_api_auth()["api_token"]
API_KEY = get_api_auth()["api_key"]


@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_time=3)
def get_trello_obj(base_url: str, request_params: Dict):
    return requests.get(base_url, params=request_params)


if __name__ == "__main__":
    pass
