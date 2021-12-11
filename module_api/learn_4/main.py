from os.path import splitdrive
from urllib.parse import urlsplit

import requests
from urllib import parse
import os
import os.path
from pathlib import Path
from dotenv import load_dotenv

Path('images').mkdir(parents=True, exist_ok=True)
path_img = 'images/'
url_spacex = 'https://api.spacexdata.com/v4/rockets'
spacex_list_links = []

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

# fetch_spacex_last_launch(url_spacex, path_img)



def extension_file(link):
    extension_link = urlsplit(link)
    url_path = extension_link.path
    extension_file = os.path.splitext(url_path)[-1]
    print(extension_file)
    return extension_file

extension_file('https://example.com/txt/hello%20world.txt?v=9#python')


