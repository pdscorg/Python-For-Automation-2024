from bs4 import BeautifulSoup
import requests 
import os
url = "https://pcampus.edu.np/"

# Get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Parse the HTML content

# Find the img tags 
image_tags = soup.find_all('img')
# image source 

os.mkdir('images')

i = 1

for img_tag in image_tags:
    image_source_link = img_tag['src']

    if image_source_link.startswith('http'):
        print(f"IMAGE SOURCE LINK : {image_source_link}")

        image_data = requests.get(image_source_link).content

        with open(f'images/image_{i}.jpg', 'wb') as file:
            file.write(image_data)
        i += 1

# image content fetch 

# file system write 

