import argparse
from PIL import Image, ImageDraw, ImageFont
import qrcode

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Create a JPEG image with text and QR code')
parser.add_argument('line1', type=str, help='the first line to add to the image')
parser.add_argument('line2', type=str, help='the second to add to the image')
parser.add_argument('line3', type=str, help='the third to add to the image')
parser.add_argument('qr_data', type=str, help='the data to encode in the QR code')
args = parser.parse_args()


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
