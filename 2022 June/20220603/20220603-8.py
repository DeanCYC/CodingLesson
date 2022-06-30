import json


def main():
    mydict = {
        'name': 'A',
        'age': 38,
        'qq': 957658,
        'friends': ['B', 'C'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存數據完成!')


if __name__ == '__main__':
    main()