import requests
from pathlib import Path

url = 'https://api.spacexdata.com/v4/launches'

Path('images').mkdir(parents=True, exist_ok=True)
img_file = 'hubble.jpeg'
path = f'images/{img_file}'

def upload_img(url, path):
    response = requests.get(url)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)
        img = file
    return img


upload_img(url, path)





