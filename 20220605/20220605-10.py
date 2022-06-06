#使用多進程對複雜任務進行“分而治之”
#我們來完成1~100000000求和的計算密集型任務，這個問題本身非常簡單，有點循環的知識就能解決，代碼如下所示。

from time import time


def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()