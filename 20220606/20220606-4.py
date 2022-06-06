from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():
    
    # 自定義執行緒類
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON是純文本不能攜帶二進制數據
            # 所以圖片的二進制數據要處理成base64編碼
            my_dict['filedata'] = data
            # 通過dumps函數將字典處理成JSON字符串
            json_str = dumps(my_dict)
            # 發送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.創建套接字對象並指定使用哪種傳輸服務
    server = socket()
    # 2.綁定IP地址和端口(區分不同的服務)
    server.bind(('192.168.1.2', 5566))
    # 3.開啟監聽 - 監聽客戶端連接到服務器
    server.listen(512)
    print('服務器啟動開始監聽...')
    with open('guido.jpg', 'rb') as f:
        # 將二進制數據處理成base64再解碼成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 啟動一個執行緒來處理客戶端的請求
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()