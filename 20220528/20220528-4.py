#函數的重組-2

# 在參數名前面的*表示args是一個可變參數
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
# 在調用add函數時可以傳入0個或多個參數
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))