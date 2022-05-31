#當我們定義好一個類之後，可以通過下面的方式來創建對象並給對象發消息

def main():
    # 創建學生對象並指定姓名和年齡
    stu1 = Student('A', 38)
    # 給對象發study消息
    stu1.study('Python程序設計')
    # 給對象發watch_av消息
    stu1.watch_movie()
    stu2 = Student('B', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()