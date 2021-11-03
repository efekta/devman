import os
import requests
import json
from urllib.parse import urlsplit

user_long_link = input('Введите ссылку: ')
url_bitlink = 'https://api-ssl.bitly.com/v4/bitlinks'
token = '85e8233effe0a218a3f9564c03cbb876159c3f24'
headers = {'Authorization': token}

def shorten_link(token, url_bitlink):
    response = requests.post(
        url_bitlink,
        headers=headers,
        json={'long_url': user_long_link}
    )
    response.raise_for_status()
    answer = response.json()
    short_link = answer['id']
    return short_link

try:
    bitlink = shorten_link(token, url_bitlink)
    print(bitlink)
except requests.exceptions.HTTPError:
    print('Вы ввели ссылку некорректно!')

