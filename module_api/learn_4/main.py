from os.path import splitdrive
from urllib.parse import urlsplit

import requests
from urllib import parse
import os
import os.path
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
nasa_token = os.getenv('NASA_TOKEN')

Path('images').mkdir(parents=True, exist_ok=True)
path_img = 'images/'
url_spacex = 'https://api.spacexdata.com/v4/rockets'
url_nasa = f'https://api.nasa.gov/planetary/apod?api_key={nasa_token}&count=50'
file_name = 'hubble.jpeg'
spacex_list_links = []
nasa_list_links = []
count = 50

def upload_image_nasa(url_nasa):
    response_nasa = requests.get(url_nasa)
    response_nasa.raise_for_status()
    response_nasa_list = response_nasa.json()
    for link_num, link in enumerate(response_nasa_list):
        link = link['url']
        # print(link_num, link)
        nasa_list_links.append(link)

upload_image_nasa(url_nasa)

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
    extension_link = os.path.splitext(url_path)[-1]
    return extension_link

# extension_file('https://example.com/txt/hello%20world.txt?v=9#python')

# print(nasa_token)

def upload_img(url, path_img):
    response = requests.get(url)
    response.raise_for_status()

    with open(f'{path_img}{file_name}', 'wb') as file:
        file.write(response.content)

# upload_img('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', path_img)
