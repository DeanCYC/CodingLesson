def main():
    try:
        with open('致橡樹.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('無法打開指定的文件!')
    except LookupError:
        print('指定了未知的編碼!')
    except UnicodeDecodeError:
        print('讀取文件時解碼錯誤!')


if __name__ == '__main__':
    main()