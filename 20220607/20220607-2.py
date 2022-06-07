#裁減圖片

image = Image.open('./res/guido.jpg')
rect = 80, 20, 310, 360
image.crop(rect).show()