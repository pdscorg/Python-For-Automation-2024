"""
Rename all the images in the ./images folder. There are images of .jpg, .png
extensions. The images should be renamed to 001_image.jpg(or .png according to 
original extension), 002_image.jpg and so on.
"""

import os

# specify the path where images are located. In this case, it is located at
# images folder in the current directory.
img_path = "./images"

# list all the images present in the images folder.
img_list = os.listdir(img_path)

# Iterate over this list and rename images.
count = 0  # To track the number to append in the new name.
for img in img_list:
    count = count + 1
    # Convert count to string and append 0s from the left.
    num = str(count).zfill(3)

    # Split the image name into name and extension and take extension.
    ext = os.path.splitext(img)[1]

    new_name = f"{num}_image" + ext

    source = os.path.join(img_path, img)
    destination = os.path.join(img_path, new_name)

    os.rename(source, destination)

print("Renaming completed.")