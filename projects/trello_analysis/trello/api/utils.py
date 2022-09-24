from typing import Dict
from dotenv import load_dotenv
import os

env_file_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=env_file_path)


def get_api_auth() -> Dict:
    """
    This method is used to get .env variables for trello auth
    :return: api_token and api_key
    :rtype: Dict
    """
    auth = dict()
    auth["api_token"], auth["api_key"] = os.getenv("API_TOKEN"), os.getenv(
        "API_KEY")
    return auth
