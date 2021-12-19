import requests
import os.path
from os import listdir
from dotenv import load_dotenv
import time
import random

load_dotenv()

tg_token = os.getenv('TG_TOKEN')
tg_chat_id = os.getenv('TG_CHAT_ID')
channel_id = os.getenv('CHANEL_ID')
sleep_time_test = 10
sleep_time = 86400

def send_telegram():
    while True:
        photos_list = listdir('images')
        url = f'https://api.telegram.org/bot{tg_token}/sendPhoto'

        with open(f'images/{random.choice(photos_list)}', 'rb') as file:
            files = {'photo': file}
            response = requests.post(url, data={'chat_id': channel_id}, files=files)
            time.sleep(sleep_time_test)

        if response.ok:
            raise Exception('post_text error')

