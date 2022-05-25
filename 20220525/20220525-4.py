#英吋跟毫米互換
value = float(input('請輸入長度: '))
unit = input('請輸入單位: ')
if unit == 'in' or unit == '英吋':
    print('%f英吋 = %f毫米' % (value, value * 2.54))
elif unit == 'cm' or unit == '毫米':
    print('%f毫米 = %f英吋' % (value, value / 2.54))
else:
    print('請輸入有效的單位')