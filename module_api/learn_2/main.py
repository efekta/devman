import os
import requests
import json
from pip import main
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()

url_info_bitlink = 'https://api-ssl.bitly.com/v4/bitlinks/'
token = os.getenv("TOKEN")
headers = {'Authorization': token}
domain_bitlink = 'bit.ly'

def main_func():
    user_input_link = input('Введите ссылку: ')
    parse_link = urlparse(user_input_link)
    domain = parse_link.netloc
    url_path = parse_link.path
    flag = domain_bitlink == domain

    def shorten_link(token, url):
        response = requests.post(url_info_bitlink, headers=headers, json={'long_url': user_input_link})
        response.raise_for_status()
        answer = response.json()
        short_link = answer['link']
        return short_link

    def count_clicks(token, url):
        url_count_clicks_concat = f'{url_info_bitlink}{domain}{url_path}/clicks'
        response_clicks = requests.get(url_count_clicks_concat, headers=headers)
        response_clicks.raise_for_status()
        response_clicks_answer = response_clicks.json()
        return response_clicks_answer

    def is_bitlink(token, url):
        url_is_bitlink_concat = f'{url_info_bitlink}{domain}{url_path}'
        response_is_bitlink = requests.get(url_is_bitlink_concat, headers=headers)
        response_is_bitlink.raise_for_status()
        response_is_bitlink_answer = response_is_bitlink.json()
        return response_is_bitlink_answer

    try:
        if flag:
            info_count_clicks = count_clicks(token, user_input_link)
            print(info_count_clicks)
            info_is_bitlink = is_bitlink(token, user_input_link)
            print(info_is_bitlink)
        else:
            bitlink = shorten_link(token, user_input_link)
            print(bitlink)
    except requests.exceptions.HTTPError:
        print('Вы ввели ссылку некорректно!')


if __name__ == '__main__':
    main_func()





