import requests
from pathlib import Path

url = 'https://api.spacexdata.com/v4/launches'

Path('images').mkdir(parents=True, exist_ok=True)
img_file = 'hubble.jpeg'
path = f'images/{img_file}'
item_links = []

def upload_img(url):
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    for item in response:
        link_item = item['links']
        item_links.append(link_item['patch'])

    # with open(path, 'wb') as file:
    #     file.write(response.content)
    #     img = file
    # return img

upload_img(url)
print(item_links)






