"""
說明：子列表指的是列表中索引（下標）連續的元素構成的列表；列表中的元素是int類型，可能包含正整數、0、負整數；程序輸入列表中的元素，輸出子列表元素求和的最大值，例如：
輸入：1 -2 3 5 -3 2
輸出：8
輸入：0 -2 3 5 -1 2
輸出：9
輸入：-9 -2 -3 -5 -3
輸出：-2
"""
def main():
    items = list(map(int, input().split()))
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)


if __name__ == '__main__':
    main()
