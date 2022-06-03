def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件無法打開.')
    except IOError as e:
        print('讀寫文件時出現錯誤.')
    print('程序執行結束.')


if __name__ == '__main__':
    main()