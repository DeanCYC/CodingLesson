#生成器進化為協程。

#生成器對象可以使用send()方法發送數據，發送的數據會成為生成器函數中通過yield表達式獲得的值。
#這樣，生成器就可以作為協程使用，協程簡單的說就是可以相互協作的子程序。

def calc_avg():
    """流式計算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter


gen = calc_avg()
next(gen)
print(gen.send(10))
print(gen.send(20))
print(gen.send(30))