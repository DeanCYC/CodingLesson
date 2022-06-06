from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 請自行修改下面的郵件發送者和接收者
    sender = 'abcdefg@126.com'
    receivers = ['uvwxyz@qq.com', 'uvwxyz@126.com']
    message = MIMEText('用Python發送郵件的示例代碼.', 'plain', 'utf-8')
    message['From'] = Header('A', 'utf-8')
    message['To'] = Header('B', 'utf-8')
    message['Subject'] = Header('示例代碼實驗郵件', 'utf-8')
    smtper = SMTP('smtp.126.com')
    # 請自行修改下面的登錄口令
    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    print('郵件發送完成!')


if __name__ == '__main__':
    main()