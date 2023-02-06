from datetime import datetime

import requests
from bs4 import BeautifulSoup


def download_public_image(image_url: str):
    print(f"Downloading image from {image_url} ...")
    soup = BeautifulSoup(requests.get(image_url).content, "html.parser")
    # The image URL is in the content field of the first meta tag with property og:image
    image_url = soup.find("meta", {"property": "og:image"})["content"]
    image_data = requests.get(image_url).content
    file_name = f"{datetime.now():%Y-%m-%d_%H:%M:%S}.jpg"
    with open(file_name, "wb") as fp:
        fp.write(image_data)
    print(f"Done. Image saved to disk as {file_name}.")


if __name__ == "__main__":
    download_public_image(image_url="put-instagram-link")
