import os
from PIL import Image
img1 = Image.open('image1.jpg')
# to change extension
#img1.save('image1.png')

# to show image
#img1.show()

# to resize image
# max_size = (250,250)
# img1.thumbnail(max_size)
# img1.save('image1_small.jpg')

# to change all image from jpg to png or from other to other
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename, extension = os.path.splitext(item)
#         img1.save(f'{filename}.png')

# to sharpness image
from PIL import ImageEnhance
# img2 =Image.open('image2.jpg')
# enhancer = ImageEnhance.Sharpness(img2)
# enhancer.enhance(0).save('image2edited.jpg')  # 0 for blurry image , 1 for original image, 2.... for increased sharpness


# to change color
img2 =Image.open('image3.jpg')
enhancer = ImageEnhance.Color(img2)
enhancer.enhance(0).save('image3edited.jpg')  # 0 for gray image , 1 for original image, 2.... for increased color

# to change brightness
# img2 =Image.open('image3.jpg')
# enhancer = ImageEnhance.Brightness(img2)
# enhancer.enhance(0).save('image3edited.jpg')  # 0 for gray image , 1 for original image, 2.... for increased color
#
# # to change contrast
# img2 =Image.open('image3.jpg')
# enhancer = ImageEnhance.Contrast(img2)
# enhancer.enhance(0).save('image3edited.jpg')  # 0 for gray image , 1 for original image, 2.... for increased color

# to filter
from PIL import ImageFilter
img2 =Image.open('image3.jpg')
img2.filter(ImageFilter.GaussianBlur(radius=3)).save('image3.png')


