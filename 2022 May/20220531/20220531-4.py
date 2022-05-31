class Student(object):

    # __init__是一個特殊方法用於在創建對象時進行初始化操作
    # 通過這個方法我們可以為學生對象綁定name和age兩個屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在學習%s.' % (self.name, course_name))

    # PEP 8要求標識符的名字用全小寫多個單詞用下劃線連接
    # 但是部分程序員和公司更傾向於使用駝峰命名法(駝峰標識)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能觀看《熊出沒》.' % self.name)
        else:
            print('%s正在觀看島國愛情大電影.' % self.name)

#說明： 寫在類中的函數，我們通常稱之為（對象的）方法，這些方法就是對象可以接收的消息。