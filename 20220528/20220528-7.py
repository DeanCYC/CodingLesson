#實現計算求最大公約數和最小公倍數的函數。
def gcd(x, y):
    #求最大公约数
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def is_palindrome(num):
    #判断一个数是不是迴文數
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

def lcm(x, y):
    #求最小公倍数
    return x * y // gcd(x, y)

#實現判斷一個數是不是質數的函數
def is_prime(num):
    #判斷一個數是不是質數
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

#寫一個程序判斷輸入的正整數是不是迴文質數
if __name__ == '__main__':
    num = int(input('請輸入正整數: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是迴文質數' % num)
    else:
        print('%d不是迴文質數' % num)