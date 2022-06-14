#多個線程競爭資源的情況。

"""
多線程程序如果沒有競爭資源處理起來通常也比較簡單
當多個線程競爭臨界資源的時候如果缺乏必要的保護措施就會導致數據錯亂
說明：臨界資源就是被多個線程競爭的資源
"""
import time
import threading

from concurrent.futures import ThreadPoolExecutor


class Account(object):
    """銀行賬戶"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        # 通過鎖保護臨界資源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance


def main():
    """主函數"""
    account = Account()
    # 創建線程池
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(100):
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    # 關閉線程池
    pool.shutdown()
    for future in futures:
        future.result()
    print(account.balance)


if __name__ == '__main__':
    main()