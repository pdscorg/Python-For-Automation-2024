"""
Convert the given images in a folder into pdf using img2pdf library. Images are
available in ./images folder. Generated pdf should be stored at the current
directory.
"""

import os
import img2pdf

# Define A4 size to have uniform page size for each image even when images are
# of different sizes.
a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
layout = img2pdf.get_layout_fun(a4inpt)

# Specify input and output path.
img_path = './images'
output_file_path = 'output.pdf'

img_list = os.listdir(img_path)

# List to store image paths to pass to img2pdf.convert function.
img_path_list = []

# Iterate over the list of images and append it's path.
for img in img_list:
    img_path_list.append(os.path.join(img_path, img))

# List of images and layout is passed to the img2pdf.convert function and it 
# returns binary data which is written to output file.
pdf_bytes = img2pdf.convert(img_path_list, layout_fun=layout)
with open(output_file_path, "wb") as f:
    f.write(pdf_bytes)

print("Successfully converted to pdf.")