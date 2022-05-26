#用for循環實現1~100之間的偶數求和-1
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)