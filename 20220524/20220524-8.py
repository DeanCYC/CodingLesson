#輸入年份判斷是不是閏年
year = int(input('請輸入年份: '))
# 如果代碼太長寫成一行不便於閱讀 可以使用\對代碼進行折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(is_leap)