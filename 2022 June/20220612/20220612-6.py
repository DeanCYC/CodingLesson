#面向對象設計原則
'''
單一職責原則 （SRP）- 一個類只做該做的事情（類的設計要高內聚）
開閉原則 （OCP）- 軟件實體應該對擴展開發對修改關閉
依賴倒轉原則（DIP）- 面向抽象編程（在弱類型語言中已經被弱化）
里氏替換原則（LSP） - 任何時候可以用子類對象替換掉父類對象
接口隔離原則（ISP）- 接口要小而專不要大而全（Python中沒有接口的概念）
合成聚合復用原則（CARP） - 優先使用強關聯關係而不是繼承關係復用代碼
最少知識原則（迪米特法則，LoD）- 不要給沒有必然聯繫的對象發消息
說明：上面加粗的字母放在一起稱為面向對象的SOLID原則。

GoF設計模式

創建型模式：單例、工廠、建造者、原型
結構型模式：適配器、門面（外觀）、代理
行為型模式：迭代器、觀察者、狀態、策略
'''

#例子：可插拔的哈希算法（策略模式）。

class StreamHasher():
    """哈希摘要生成器"""

    def __init__(self, alg='md5', size=4096):
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__('hashlib'), alg.lower())()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成十六進制形式的摘要"""
        for buf in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(buf)
        return self.hasher.hexdigest()

def main():
    """主函數"""
    hasher1 = StreamHasher()
    with open('Python-3.7.6.tgz', 'rb') as stream:
        print(hasher1.to_digest(stream))
    hasher2 = StreamHasher('sha1')
    with open('Python-3.7.6.tgz', 'rb') as stream:
        print(hasher2(stream))


if __name__ == '__main__':
    main()