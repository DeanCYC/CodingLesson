from functools import wraps
from time import time


class Record():
    """通過定義類的方式定義裝飾器"""

    def __init__(self, output):
        self.output = output

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output(func.__name__, time() - start)
            return result

        return wrapper
#說明：由於對帶裝飾功能的函數添加了@wraps裝飾器，可以通過func.__wrapped__方式獲得被裝飾之前的函數或類來取消裝飾器的作用。