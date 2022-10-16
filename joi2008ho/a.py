n = int(input())

table = []

for i in range(1, n + 1):
    stone = int(input()) # 0 = 白, 1 = 黒
    if i == 1:
        table.append([stone, 1])
    elif i % 2 == 1:
        # i が奇数の場合
        prev_stone, num = table[-1]
        if stone == prev_stone:
            table[-1][1] += 1
        else:
            table.append([stone, 1])
    else:
        # i が偶数の場合
        prev_stone, num = table[-1]
        if stone == prev_stone:
            table[-1][1] += 1
        else:
            # 違う色が来た。
            if len(table) == 1:
                table[-1][0] = stone
                table[-1][1] += 1
            else:
                prev_num = table[-1][1]
                table.pop(-1)
                table[-1][1] += prev_num + 1

total = 0
for stone, num in table:
    if stone == 0:
        total += num

# print(table)
print(total)
