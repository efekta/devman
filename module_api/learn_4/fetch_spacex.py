from urllib.parse import urlsplit
import requests
import os.path
from pathlib import Path
from datetime import datetime
import telegram
from os import listdir
from dotenv import load_dotenv
import time
Path('images').mkdir(parents=True, exist_ok=True)

spacex_list_links = []
url_spacex = 'https://api.spacexdata.com/v4/rockets'
path_img = 'images/'

def fetch_spacex_last_launch(url_spacex, path_img):
    response_spacex = requests.get(url_spacex)
    response_spacex.raise_for_status()
    response_spacex_list = response_spacex.json()

    for item in response_spacex_list:
        item_link = item['flickr_images']
        for link in item_link:
            spacex_list_links.append(link)

    for link_number, link in enumerate(spacex_list_links):
        image_name = f'spacex{link_number}.jpg'
        response_spacex = requests.get(link)
        response_spacex.raise_for_status()
        with open(f'{path_img}{image_name}', 'wb') as file:
            file.write(response_spacex.content)

fetch_spacex_last_launch(url_spacex, path_img)