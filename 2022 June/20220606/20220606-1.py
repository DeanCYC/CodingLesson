from time import time
from threading import Thread

import requests


# 繼承Thread類創建自定義的執行緒類
class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Hao/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 通過requests模塊的get函數獲取網絡資源
    # 下面的代碼中使用了天行數據接口提供的網絡API
    # 要使用該數據接口需要在天行數據的網站上註冊
    # 然後用自己的Key替換掉下面代碼的中APIKey即可
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=APIKey&num=10')
    # 將服務器返回的JSON格式的數據解析為字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通過多執行緒的方式實現圖片下載
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main()