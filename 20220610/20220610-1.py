# 公雞5元一隻 母雞3元一隻 小雞1元三隻
# 用100元買100隻雞 問公雞/母雞/小雞各多少只
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(x, y, z)

# A、B、C、D、E五人在某天夜里合夥捕魚 最後疲憊不堪各自睡覺
# 第二天A第一個醒來 他將魚分為5份 扔掉多餘的1條 拿走自己的一份
# B第二個醒來 也將魚分為5份 扔掉多餘的1條 拿走自己的一份
# 然後C、D、E依次醒來也按同樣的方式分魚 問他們至少捕了多少條魚
fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5