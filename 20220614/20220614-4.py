#多進程：多進程可以有效的解決GIL的問題，實現多進程主要的類是Process，其他輔助的類跟threading模塊中的類似，進程間共享數據可以使用管道、套接字等，
#在multiprocessing模塊中有一個Queue類，它基於管道和鎖機制提供了多個進程共享的隊列。下面是官方文檔上關於多進程和進程池的一個示例。

"""
多進程和進程池的使用
多線程因為GIL的存在不能夠發揮CPU的多核特性
對於計算密集型任務應該考慮使用多進程
time python3 example22.py
real    0m11.512s
user    0m39.319s
sys     0m0.169s
使用多進程後實際執行時間為11.512秒，而用戶時間39.319秒約為實際執行時間的4倍
這就證明我們的程序通過多進程使用了CPU的多核特性，而且這台計算機配置了4核的CPU
"""
import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def is_prime(n):
    """判斷素數"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    """主函數"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()

'''
重點：多線程和多進程的比較。

以下情況需要使用多線程：

程序需要維護許多共享的狀態（尤其是可變狀態），Python中的列表、字典、集合都是線程安全的，所以使用線程而不是進程維護共享狀態的代價相對較小。
程序會花費大量時間在I/O操作上，沒有太多並行計算的需求且不需佔用太多的內存。
以下情況需要使用多進程：

程序執行計算密集型任務（如：字節碼操作、數據處理、科學計算）。
程序的輸入可以並行的分成塊，並且可以將運算結果合併。
程序在內存使用方面沒有任何限制且不強依賴於I/O操作（如：讀寫文件、套接字等）。
'''