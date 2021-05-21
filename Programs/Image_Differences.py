from PIL import Image, ImageChops

import smtplib

img1 = Image.open(r'C:\Users\1022589\Desktop\image\image1.jpg')
img2 = Image.open(r'C:\Users\1022589\Desktop\image\image2.jpg')

diff = ImageChops.difference(img1, img2)

if diff.getbbox():
    diff.show()