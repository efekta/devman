import requests
import os.path
from os import listdir
from dotenv import load_dotenv
import time
import random

load_dotenv()

tg_token = os.getenv('TG_TOKEN')
tg_chat_id = os.getenv('TG_CHAT_ID')
sleep_time_test = 10
sleep_time = 86400

def send_telegram():
    while True:
        photos_list = listdir('images')
        random_index = random.randint(0, len(photos_list) - 1)
        url = "https://api.telegram.org/bot"
        channel_id = "@uploadphotos"
        url += tg_token
        method = url + "/sendPhoto"
        files = {'photo': open(f'images/{photos_list[random_index]}', 'rb')}
        r = requests.post(method, data={"chat_id": channel_id}, files=files)
        time.sleep(sleep_time_test)

        if r.status_code != 200:
            raise Exception("post_text error")

