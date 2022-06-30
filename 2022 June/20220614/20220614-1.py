#多線程：Python中提供了Thread類並輔以Lock、Condition、Event、Semaphore和Barrier。
#Python中有GIL來防止多個線程同時執行本地字節碼，這個鎖對於CPython是必須的，因為CPython的內存管理並不是線程安全的，因為GIL的存在多線程並不能發揮CPU的多核特性。

"""
面試題：進程和線程的區別和聯繫？
進程 - 操作系統分配內存的基本單位 - 一個進程可以包含一個或多個線程
線程 - 操作系統分配CPU的基本單位
並發編程（concurrent programming）
1. 提升執行性能 - 讓程序中沒有因果關係的部分可以並發的執行
2. 改善用戶體驗 - 讓耗時間的操作不會造成程序的假死
"""
import glob
import os
import threading

from PIL import Image

PREFIX = 'thumbnails'

def generate_thumbnail(infile, size, format='PNG'):
    """生成指定圖片文件的縮略圖"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('/') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
	img = Image.open(infile)
	img.thumbnail(size, Image.ANTIALIAS)
	img.save(outfile, format)


def main():
    """主函數"""
	if not os.path.exists(PREFIX):
		os.mkdir(PREFIX)
	for infile in glob.glob('images/*.png'):
		for size in (32, 64, 128):
            # 創建並啟動線程
			threading.Thread(
				target=generate_thumbnail, 
				args=(infile, (size, size))
			).start()
			

if __name__ == '__main__':
	main()