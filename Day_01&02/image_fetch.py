from bs4 import BeautifulSoup

import requests

url = 'https://pcampus.edu.np/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')

i = 1
for image in images:
    image_source = image['src']
    if image_source.startswith('http'):
        print(image_source)
        image_content = requests.get(image_source).content

        with open(f"images/image_{i}.jpg", 'wb') as file:
            file.write(image_content)
            i += 1