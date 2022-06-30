#用裝飾器來實現單例模式。

from functools import wraps


def singleton(cls):
    """裝飾類的裝飾器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President:
    """總統(單例類)"""
    pass
#提示：上面的代碼中用到了閉包（closure），不知道你是否已經意識到了。還沒有一個小問題就是，上面的代碼並沒有實現線程安全的單例，如果要實現線程安全的單例應該怎麼做呢？