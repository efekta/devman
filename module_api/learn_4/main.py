from urllib.parse import urlsplit
import requests
import os.path
from pathlib import Path
from datetime import datetime
import telegram
from dotenv import load_dotenv
load_dotenv()

nasa_token = os.getenv('NASA_TOKEN')
tg_token = os.getenv('TG_TOKEN')
tg_chat_id = 273352787
bot = telegram.Bot(token=f'{tg_token}')
print(bot.get_me())

updates = bot.get_updates()
print(updates[0])

bot.send_message(text='Hi Bot!', chat_id=tg_chat_id)
bot.send_message(chat_id=tg_chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
# update.message.reply_text("I'm sorry Dave I'm afraid I can't do that.")



Path('images').mkdir(parents=True, exist_ok=True)
spacex_list_links = []
nasa_list_links = []
epic_nasa_list_links = []
count = 10
path_img = 'images/'
file_name = 'hundle.jpg'
url_spacex = 'https://api.spacexdata.com/v4/rockets'
url_nasa = f'https://api.nasa.gov/planetary/apod?api_key={nasa_token}&count={count}'
url_nasa_epic = f'https://api.nasa.gov/EPIC/api/natural?api_key={nasa_token}'

def upload_img(url, path_img):
    response = requests.get(url)
    response.raise_for_status()

    with open(f'{path_img}{file_name}', 'wb') as file:
        file.write(response.content)

# upload_img('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', path_img)

def upload_image_nasa(url_nasa_epic):
    response_nasa_epic = requests.get(url_nasa_epic)
    response_nasa_epic.raise_for_status()
    response_nasa_epic_list = response_nasa_epic.json()

    for item in response_nasa_epic_list:
        # print(item)
        date_item = item['date']
        date_time = datetime.fromisoformat(date_item)
        date = date_time.date()
        now_date = date.strftime("%Y/%m/%d")
        # print(now_date)
        image_name = item['image']
        # print(image_name)
        format_url = f'https://api.nasa.gov/EPIC/archive/natural/' \
                     f'{now_date}/png/{image_name}.png?' \
                     f'api_key={nasa_token}&count={count}'
        # print(format_url)
        epic_nasa_list_links.append(format_url)

    for epic_link_number, epic_link in enumerate(epic_nasa_list_links):
        # print(epic_link)
        image_name = f'nasa_epic{epic_link_number}.png'
        response_nasa = requests.get(epic_link)
        response_nasa.raise_for_status()
        with open(f'{path_img}{image_name}', 'wb') as file:
            file.write(response_nasa.content)

# upload_image_nasa(url_nasa_epic)

def upload_image_nasa(url_nasa):
    response_nasa = requests.get(url_nasa)
    response_nasa.raise_for_status()
    response_nasa_list = response_nasa.json()
    for link in response_nasa_list:
        link = link['url']
        nasa_list_links.append(link)
    for link_number, link in enumerate(nasa_list_links):
        image_name = f'nasa{link_number}.jpg'
        response_nasa = requests.get(link)
        response_nasa.raise_for_status()
        with open(f'{path_img}{image_name}', 'wb') as file:
            file.write(response_nasa.content)

# upload_image_nasa(url_nasa)

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

