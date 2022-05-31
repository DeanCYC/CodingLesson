#函數的重組-1
from random import randint


def roll_dice(n=2):
    # 搖骰子
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    # 三個數相加
    return a + b + c


# 如果沒有指定參數就使用默認姪僥兩顆骰子
print(roll_dice())
# 搖三顆骰子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 傳遞參數時可以不按照設定的順序進行傳遞
print(add(c=50, a=100, b=200))