#輸入M和N計算C(M,N)-2

def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
# 當需要計算階乘的時候不用再寫循環求階乘而是直接調用已經定義好的函數
print(fac(m) // fac(n) // fac(m - n))