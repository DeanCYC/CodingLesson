import urllib.parse
import http.client
import json


def main():
    host  = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的參數需要填入自己註冊的帳號和密碼
    params = urllib.parse.urlencode({'account': '你自己的帳號', 'password' : '你自己的密碼', 'content': '您的驗證碼是：147258。請不要把驗證碼洩露給其他人。', 'mobile': '接收者的手機號碼', 'format':'json' })
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == '__main__':
    main()