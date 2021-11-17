import requests
from pathlib import Path

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
img_file = 'hubble.jpeg'

path = Path('images').mkdir(parents=True, exist_ok=True)
response = requests.get(url)
response.raise_for_status()
with open(f'images/{img_file}', 'wb') as file:
    file.write(response.content)







