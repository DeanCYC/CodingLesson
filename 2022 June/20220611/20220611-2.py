#輸出函數執行時間的裝飾器。

def record_time(func):
    """自定義裝飾函數的裝飾器"""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start}秒')
        return result
        
    return wrapper