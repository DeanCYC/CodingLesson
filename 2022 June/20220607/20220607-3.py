#生成縮圖

image = Image.open('./res/guido.jpg')
size = 128, 128
image.thumbnail(size)
image.show()