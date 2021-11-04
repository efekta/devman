import os
import requests
import json
from urllib.parse import *

user_long_link = input('Введите ссылку: ')
url_bitlink = 'https://api-ssl.bitly.com/v4/bitlinks'
url_count_clicks = 'https://api-ssl.bitly.com/v4/bitlinks/'
token = '85e8233effe0a218a3f9564c03cbb876159c3f24'
headers = {'Authorization': token}

def shorten_link(token, url_bitlink):
    response = requests.post(url_bitlink, headers=headers, json={'long_url': user_long_link})
    response.raise_for_status()
    answer = response.json()
    short_link = answer['link']
    return short_link

def count_clicks(token, url):
    parse_bitlink = urlparse(bitlink)
    bitlink_netloc = parse_bitlink.netloc
    bitlink_path = parse_bitlink.path
    url_count_clicks_concat = f'{url_count_clicks}{bitlink_netloc}{bitlink_path}/clicks'
    response_clicks = requests.get(url_count_clicks_concat, headers=headers)
    response_clicks.raise_for_status()
    response_clicks_answer = response_clicks.json()
    return response_clicks_answer

try:
    bitlink = shorten_link(token, url_bitlink)
    print(bitlink)
    count_clicks = count_clicks(token, url_count_clicks)
    print(count_clicks)
except requests.exceptions.HTTPError:
    print('Вы ввели ссылку некорректно!')



