import os

from PIL import Image, ImageEnhance, ImageFilter

path = './images'
pathOut = 'editedImages'

for filename in os.listdir(path):
    img = Image.open(path + '/' + filename)
    img = img.convert('L')
    img = img.filter(ImageFilter.SHARPEN)
    img = ImageEnhance.Contrast(img).enhance(1.25)
    img = ImageEnhance.Brightness(img).enhance(1.5)
    img.save(pathOut + '/' + filename)
