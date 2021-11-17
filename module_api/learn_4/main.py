import requests
from pathlib import Path

url = 'https://api.spacexdata.com/v4/launches'

response = requests.get(url)
response.raise_for_status()
response = response.json()
print(response)

img_file = 'hubble.jpeg'
path = Path('images').mkdir(parents=True, exist_ok=True)

def upload_img(url, path):
    response = requests.get(url)
    response.raise_for_status()

    with open(f'images/{img_file}', 'wb') as file:
        file.write(response.content)
        img = file
    return img








