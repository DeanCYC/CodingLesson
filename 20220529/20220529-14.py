# 定義元組
t = ('小叮', 30, True, '桃園')
print(t)
# 獲取元組中的元素
print(t[0])
print(t[3])
# 遍曆元組中的值
for member in t:
    print(member)
# 重新給元組賦值
# t[0] = '王大錘'  # TypeError
# 變量t重新引用了新的元組原來的元組將被垃圾回收
t = ('A', 20, True, '台北')
print(t)
# 將元組轉換成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = 'B'
person[1] = 25
print(person)
# 將列表轉換成元組
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)