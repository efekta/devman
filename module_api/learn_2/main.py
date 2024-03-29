import argparse
import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv

URL_INFO_BITLINK = 'https://api-ssl.bitly.com/v4/bitlinks/'

def shorten_link(token, args_link):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(URL_INFO_BITLINK, headers=headers, json={'long_url': args_link})
    response.raise_for_status()
    answer = response.json()
    short_link = answer['link']
    return short_link

def count_clicks(token, args_link):
    headers = {'Authorization': f'Bearer {token}'}
    parse_link = urlparse(args_link)
    domain = parse_link.netloc
    url_path = parse_link.path
    url_count_clicks_concat = f'{URL_INFO_BITLINK}{domain}{url_path}/clicks/summary'
    response_clicks = requests.get(url_count_clicks_concat, headers=headers)
    response_clicks.raise_for_status()
    response_clicks_answer = response_clicks.json()
    return response_clicks_answer

def is_bitlink(token, args_link):
    headers = {'Authorization': f'Bearer {token}'}
    parse_link = urlparse(args_link)
    domain = parse_link.netloc
    url_path = parse_link.path
    url_is_bitlink_concat = f'{URL_INFO_BITLINK}{domain}{url_path}'
    response_is_bitlink = requests.get(url_is_bitlink_concat, headers=headers)
    is_bitlink_answer = response_is_bitlink.ok
    return is_bitlink_answer

def main():
    load_dotenv()
    token = os.getenv("BITLINK_TOKEN")
    parser = argparse.ArgumentParser(description='Описание программы')
    parser.add_argument('link', type=str, help='Bitlink')
    args = parser.parse_args()
    args_link = args.link
    try:
        if is_bitlink(token, args_link):
            total_clicks = count_clicks(token, args_link)
            print('Количество переходов по ссылке битли: ', total_clicks['total_clicks'])
        else:
            bitlink = shorten_link(token, args_link)
            print(bitlink)

    except requests.exceptions.HTTPError:
        print('Вы ввели ссылку некорректно!')

if __name__ == '__main__':
    main()





