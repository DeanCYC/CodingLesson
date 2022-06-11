#將函數視為“一等公民”
'''
函數可以賦值給變量
函數可以作為函數的參數
函數可以作為函數的返回值
高階函數的用法（filter、map以及它們的替代品）
'''
items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
items2 = [x ** 2 for x in range(1, 10) if x % 2]

'''
位置參數、可變參數、關鍵字參數、命名關鍵字參數
參數的元信息（代碼可讀性問題）
匿名函數和內聯函數的用法（lambda函數）
閉包和作用域問題
Python搜索變量的LEGB順序（Local >>> Embedded >>> Global >>> Built-in）
global和nonlocal關鍵字的作用
global：聲明或定義全局變量（要么直接使用現有的全局作用域的變量，要么定義一個變量放到全局作用域）。
nonlocal：聲明使用嵌套作用域的變量（嵌套作用域必須存在該變量，否則報錯）。
裝飾器函數（使用裝飾器和取消裝飾器）
'''