# 創建字典的字面量語法
scores = {'A': 95, 'B': 78, 'C': 82}
print(scores)
# 創建字典的構造器語法
items1 = dict(one=1, two=2, three=3, four=4)
# 通過zip函數將兩個序列壓成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 創建字典的推導式語法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# 通過鍵可以獲取字典中對應的值
print(scores['A'])
print(scores['C'])
# 對字典中所有鍵值對進行遍歷
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['B'] = 65
scores['D'] = 71
scores.update(G=67, H=85)
print(scores)
if 'E' in scores:
    print(scores['E'])
print(scores.get('E'))
# get方法也是通過鍵獲取對應的值但是可以設置默認值
print(scores.get('E', 60))
# 刪除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('A', 100))
# 清空字典
scores.clear()
print(scores)