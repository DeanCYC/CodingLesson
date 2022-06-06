from random import randint
from time import time, sleep


def download_task(filename):
    print('開始下載%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下載完成! 花了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python從入門到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('總共花了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()