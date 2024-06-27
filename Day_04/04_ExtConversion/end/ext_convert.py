"""
Convert all the png images to jpg in a given source folder and store the converted image to the target folder.
"""

import os
from PIL import Image

# Source folder where images are present and target folder where output images
# are to be stored.
source_folder = './source_images'
target_folder = './target_images'

# Create the target folder if is does not exits.
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Get the list of all the images in the source folder.
images = os.listdir(source_folder)

for image in images:
    # Since we are converting png to jpg select images with .png extension.
    if image.endswith(".png"):

        # Split the image into base name and its extension and take base name.
        base = os.path.splitext(image)[0]

        # Construct new name by appending .jpg extension to the base name.
        new_name = base + ".jpg"

        img_path = os.path.join(source_folder, image)

        # Open the image and convert it to RGB from RGBA.
        img = Image.open(img_path).convert('RGB')

        dest_img_path = os.path.join(target_folder, new_name)

        # Save the image in the target folder.
        img.save(dest_img_path)


print("Extension Conversion completed.")
        