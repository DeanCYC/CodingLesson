#百錢百雞問題
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公雞: %d隻, 母雞: %d隻, 小雞: %d隻' % (x, y, z))