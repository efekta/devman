from send_telegram import send_telegram
import os
import argparse
import requests
from dotenv import load_dotenv

def main():
    load_dotenv()
    channel_id = os.getenv('CHANEL_ID')
    parser = argparse.ArgumentParser(description='Описание программы')
    parser.add_argument('link', type=str, help='CHANEL_ID')
    args = parser.parse_args()
    args_channel_id = args.link

    try:
        if args_channel_id == channel_id:
            send_telegram()
        else:
            print('Некорректный ввод!')
    except requests.exceptions.HTTPError:
        print('Некорректный ввод!')


if __name__ == '__main__':
    main()
