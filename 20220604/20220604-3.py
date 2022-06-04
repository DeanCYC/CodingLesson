#替換字符串中的不良內容
import re


def main():
    sentence = 'Fuck you.'
    purified = re.sub('[幹]|fuck|shit',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  #* you.


if __name__ == '__main__':
    main()