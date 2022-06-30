list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]
# 乘號表示列表元素的重複
list2 = ['hello'] * 3
print(list2) # ['hello', 'hello', 'hello']
# 計算列表長度(元素個數)
print(len(list1)) # 5
# 下標(索引)運算
print(list1[0]) # 1
print(list1[4]) # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1]) # 100
print(list1[-3]) # 5
list1[2] = 300
print(list1) # [1, 3, 300, 7, 100]
# 通過循環用下標遍歷列表元素
for index in range(len(list1)):
    print(list1[index])
# 通過for循環遍歷列表元素
for elem in list1:
    print(elem)
# 通過enumerate函數處理列表之後再遍歷可以同時獲得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
    
#待解 Pending
