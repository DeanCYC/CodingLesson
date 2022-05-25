#用戶身份驗證
username = input('請輸入用戶名: ')
password = input('請輸入密碼: ')
# 用戶名是admin且密碼是123456則身份驗證成功否則身份驗證失敗
if username == 'admin' and password == '123456':
    print('身份驗證成功!')
else:
    print('身份驗證失敗!')