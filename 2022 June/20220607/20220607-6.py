#變更像素
image = Image.open('./res/guido.jpg')
for x in range(80, 310):
     for y in range(20, 360):
         image.putpixel((x, y), (128, 128, 128))
image.show()