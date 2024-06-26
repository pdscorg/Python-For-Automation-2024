"""
Generate qr code for a given information.
"""

import qrcode

# Data to encode in qr code.
data = "https://www.linkedin.com/in/sandesh-pyakurel-714394154/"

# Output file path to store the generated qr code.
output_file = 'qrcode.png'

# QRCode function takes various arguments which are useful for generating
# qr code like the version to specify the size of qr code, error correction
# method, size of each box in pixels, border size in boxes.
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the data in the qr.
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="blue", back_color="white")

# Save the image.
img.save(output_file)

print("QR Code generated.")