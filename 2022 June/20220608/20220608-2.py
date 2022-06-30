#嵌套的列表的坑

names = ['關羽', '張飛', '趙雲', '馬超', '黃忠']
courses = ['語文', '數學', '英語']
# 錄入五個學生三門課程的成績
# 錯誤 - 參考 http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'請輸入{name}的{course}成績: '))
        print(scores)