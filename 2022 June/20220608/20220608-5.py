#collections模塊

'''
常用的工具類：

namedtuple：命令元組，它是一個類工廠，接受類型的名稱和屬性列表來創建一個類。
deque：雙端隊列，是列表的替代實現。 Python中的列表底層是基於數組來實現的，而deque底層是雙向鍊錶，因此當你需要在頭尾添加和刪除元素時，deque會表現出更好的性能，漸近時間複雜度為。
Counter：dict的子類，鍵是元素，值是元素的計數，它的most_common()方法可以幫助我們獲取出現頻率最高的元素。 Counter和dict的繼承關係我認為是值得商榷的，按照CARP原則，Counter跟dict的關係應該設計為關聯關係更為合理。
OrderedDict：dict的子類，它記錄了鍵值對插入的順序，看起來既有字典的行為，也有鍊錶的行為。
defaultdict：類似於字典類型，但是可以通過默認的工廠函數來獲得鍵對應的默認值，相比字典中的setdefault()方法，這種做法更加高效。
'''
"""
找出序列中出現次數最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))