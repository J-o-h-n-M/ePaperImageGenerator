import argparse
from PIL import Image, ImageDraw, ImageFont
import qrcode
import requests

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Create a JPEG image with text and QR code')
parser.add_argument('line1', type=str, help='the first line to add to the image')
parser.add_argument('line2', type=str, help='the second to add to the image')
parser.add_argument('line3', type=str, help='the third to add to the image')
parser.add_argument('qr_data', type=str, help='the data to encode in the QR code')
parser.add_argument('mac', type=str, help='MAC of the display')
parser.add_argument('AP_IP', type=str, help='IP addressof the AP')
args = parser.parse_args()



mac = args.mac   # destination mac address
dither = 0   # set dither to 1 is you're sending photos etc
apip = args.AP_IP   # ip address of your access point

# Create a new image with white background
img = Image.new('RGB', (296, 128), color='white')

# Add 3 lines of text to image
draw = ImageDraw.Draw(img)

font = ImageFont.truetype('arial.ttf', size=20)
x = 5
y = 10
draw.text((x, y), args.line1, font=font, fill='red')

font = ImageFont.truetype('arial.ttf', size=20)
x = 5
y = 50
draw.text((x, y), args.line2, font=font, fill='black')

font = ImageFont.truetype('arial.ttf', size=20)
x = 5
y = 90
draw.text((x, y), args.line3, font=font, fill='black')


# Add QR code to the image
qr = qrcode.QRCode(version=1, box_size=3, border=0)
qr.add_data(args.qr_data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color='black', back_color='white')
qr_pos_x = 185
qr_pos_y = 15
img.paste(qr_img, (qr_pos_x, qr_pos_y))

# Save the image as a JPEG file
img.save('QRcode.jpg')

# Save the image as JPEG with maximum quality
image_path = 'QRcode.jpg'

# Prepare the HTTP POST request
url = "http://" + apip + "/imgupload"
payload = {"dither": dither, "mac": mac}  # Additional POST parameter
files = {"file": open(image_path, "rb")}  # File to be uploaded

# Send the HTTP POST request
response = requests.post(url, data=payload, files=files)

# Check the response status
if response.status_code == 200:
    print("Image uploaded successfully!")
else:
    print("Failed to upload the image.")