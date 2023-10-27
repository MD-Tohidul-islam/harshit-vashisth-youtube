import os
from PIL import Image
image_path = input('enter your image: ')
img1 = Image.open(image_path)

#to resize image
size = tuple(map(int,input('enter the dimension to resize ').split()))
max_size = (size[0],size[1])
img1.thumbnail(max_size)
image_name = input('enter name with extension to rename your image: ')
img1.save(image_name)