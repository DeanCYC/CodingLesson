#混入（Mixin）
#例子：自定義字典限制只有在指定的key不存在時才能在字典中設置鍵值對。

class SetOnceMappingMixin:
    """自定義混入類"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定義字典"""
    pass


my_dict= SetOnceDict()
try:
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError:
    pass
print(my_dict)