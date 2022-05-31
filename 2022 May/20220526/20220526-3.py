#用for循環實現1~100之間的偶數求和-2
sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)