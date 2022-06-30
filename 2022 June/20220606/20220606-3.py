from socket import socket


def main():
    # 1.創建套接字對象默認使用IPv4和TCP協議
    client = socket()
    # 2.連接到服務器(需要指定IP地址和端口)
    client.connect(('192.168.1.2', 6789))
    # 3.從服務器接收數據
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()