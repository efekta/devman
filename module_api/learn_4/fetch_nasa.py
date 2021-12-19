import requests
import os.path
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import urllib.parse

load_dotenv()
nasa_token = os.getenv('NASA_TOKEN')
count = 10
url_nasa = f'https://api.nasa.gov/planetary/apod'
url_nasa_epic = f'https://api.nasa.gov/EPIC/api/natural'
path_img = 'images/'
Path('images').mkdir(parents=True, exist_ok=True)

payload_nasa = {
    'api_key': nasa_token,
    'count': count
}

payload_epic = {
    'api_key': nasa_token,
    'count': count
}

def upload_image_epic(url_nasa_epic):
    epic_nasa_links = []
    response_nasa_epic = requests.get(url_nasa_epic, params=payload_epic)
    response_nasa_epic.raise_for_status()
    response_nasa_epic_list = response_nasa_epic.json()

    for item in response_nasa_epic_list:
        date_item = item['date']
        date_time = datetime.fromisoformat(date_item)
        date = date_time.date()
        now_date = date.strftime("%Y/%m/%d")
        image_name = item['image']
        format_url = f'https://api.nasa.gov/EPIC/archive/natural/' \
                     f'{now_date}/png/{image_name}.png?api_key={nasa_token}'
        epic_nasa_links.append(format_url)

    for epic_link_number, epic_link in enumerate(epic_nasa_links):
        image_name = f'nasa_epic{epic_link_number}.png'
        response_nasa = requests.get(epic_link, params=payload_epic)
        response_nasa.raise_for_status()
        with open(f'{path_img}{image_name}', 'wb') as file:
            file.write(response_nasa.content)

def upload_image_nasa(url_nasa):
    nasa_links = []
    response_nasa = requests.get(url_nasa, params=payload_nasa)
    response_nasa.raise_for_status()
    response_nasa_list = response_nasa.json()
    for link in response_nasa_list:
        link = link['url']
        nasa_links.append(link)
    for link_number, link in enumerate(nasa_links):
        image_name = f'nasa{link_number}.jpg'
        response_nasa = requests.get(link)
        response_nasa.raise_for_status()
        with open(f'{path_img}{image_name}', 'wb') as file:
            file.write(response_nasa.content)
