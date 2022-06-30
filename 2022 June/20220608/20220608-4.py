#itertools模塊

"""
迭代工具
"""
import itertools

# 產生ABCD的全排列
itertools.permutations('ABCD')
# 產生ABCDE的五選三組合
itertools.combinations('ABCDE', 3)
# 產生ABCD和123的笛卡爾積
itertools.product('ABCD', '123')
# 產生ABC的無限循環序列
itertools.cycle(('A', 'B', 'C'))
