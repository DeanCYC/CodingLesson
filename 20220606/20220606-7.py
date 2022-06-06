from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib


def main():
    # 創建一個帶附件的郵件消息對象
    message = MIMEMultipart()
    
    # 創建文本內容
    text_content = MIMEText('附件中有本月數據請查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月數據', 'utf-8')
    # 將文本內容添加到郵件消息對像中
    message.attach(text_content)

    # 讀取文件並將文件作為附件添加到郵件消息對像中
    with open('/Users/Hao/Desktop/hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    # 讀取文件並將文件作為附件添加到郵件消息對像中
    with open('/Users/Hao/Desktop/匯總數據.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)
    
    # 創建SMTP對象
    smtper = SMTP('smtp.126.com')
    # 開啟安全連接
    # smtper.starttls()
    sender = 'abcdefg@126.com'
    receivers = ['uvwxyz@qq.com']
    # 登錄到SMTP服務器
    # 請注意此處不是使用密碼而是郵件客戶端授權碼進行登錄
    # 對此有疑問的讀者可以聯繫自己使用的郵件服務器客服
    smtper.login(sender, 'secretpass')
    # 發送郵件
    smtper.sendmail(sender, receivers, message.as_string())
    # 與郵件服務器斷開連接
    smtper.quit()
    print('發送完成!')


if __name__ == '__main__':
    main()