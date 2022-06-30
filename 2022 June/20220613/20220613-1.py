#迭代器和生成器
#迭代器是實現了迭代器協議的對象。

#Python中沒有像protocol或interface這樣的定義協議的關鍵字。
#Python中用魔術方法表示協議。
#__iter__和__next__魔術方法就是迭代器協議。
class Fib(object):
    """迭代器"""
    
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0
   
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()