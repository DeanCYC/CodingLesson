#異步處理：從調度程序的任務隊列中挑選任務，該調度程序以交叉的形式執行這些任務，我們並不能保證任務將以某種順序去執行，
#因為執行順序取決於隊列中的一項任務是否願意將CPU處理時間讓位給另一項任務。異步任務通常通過多任務協作處理的方式來實現，由於執行時間和順序的不確定，
#因此需要通過回調式編程或者future對象來獲取任務執行的結果。 Python 3通過asyncio模塊和await和async關鍵字（在Python 3.7中正式被列為關鍵字）來支持異步處理。

"""
異步I/O - async / await
"""
import asyncio


def num_generator(m, n):
    """指定範圍的數字生成器"""
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """素數過濾器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main():
    """主函數"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
    main()
#說明：上面的代碼使用get_event_loop函數獲得系統默認的事件循環，通過gather函數可以獲得一個future對象
#future對象的add_done_callback可以添加執行完成時的回調函數，loop對象的run_until_complete方法可以等待通過future對象獲得協程執行結果。