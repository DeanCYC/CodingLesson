#線程安全的單例裝飾器

from functools import wraps
from threading import RLock


def singleton(cls):
    """線程安全的單例裝飾器"""
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
'''
提示：上面的代碼用到了with上下文語法來進行鎖操作，因為鎖對象本身就是上下文管理器對象（支持__enter__和__exit__魔術方法）。在wrapper函數中，我們先做了一次不帶鎖的檢查，然後再做帶鎖的檢查，這樣做比直接加鎖檢查性能要更好，如果對像已經創建就沒有必須再去加鎖而是直接返回該對象就可以了。
'''