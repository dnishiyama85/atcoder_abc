import numpy as np
n = int(input())
ss = []
for _ in range(n):
    raw = [0] * n
    s = input().strip()
    for j, c in enumerate(s):
        raw[j] = 0 if c == '.' else 1
    ss.append(raw)

success = False
for i in range(n):
    for j in range(n):
        c = ss[i][j]
        # 右・下・右下・左下 について6つ以上連続できるか
        if c == 1:
            # 右
            length = 1
            pos = j
            rest = 2
            while True:
                if length == 6:
                    success = True
                    break
                if pos + 1 >= n:
                    break
                if ss[i][pos + 1] == 1 or rest > 0:
                    if ss[i][pos + 1] == 0:
                        rest -= 1
                    pos = pos + 1
                    length += 1
                else:
                    break

            # 下
            length = 1
            pos = i
            rest = 2
            while True:
                if length == 6:
                    success = True
                    break
                if pos + 1 >= n:
                    break
                if ss[i + 1][j] == 1 or rest > 0:
                    if ss[i + 1][j] == 0:
                        rest -= 1
                    pos = pos + 1
                    length += 1
                else:
                    break

            # # 右下
            # length = 1
            # pos_x, pos_y = j, i
            # rest = 2
            # while True:
            #     if length == 6:
            #         success = True
            #         break
            #     if pos_x + 1 >=n or pos_y + 1 >= n:
            #         break
            #     if ss[pos_y + 1][pos_x + 1] == 1 or rest > 0:
            #         if ss[pos_y + 1][pos_x + 1] == 0:
            #             rest -= 1
            #         pos_y, pos_x = pos_y + 1, pos_x + 1
            #         length += 1
            #     else:
            #         break
            #
            # # 左下
            # length = 1
            # pos_x, pos_y = j, i
            # rest = 2
            # while True:
            #     if length == 6:
            #         success = True
            #         break
            #     if pos_x - 1 < 0 or pos_y + 1 >= n:
            #         break
            #     if ss[pos_y + 1][pos_x - 1] == 1 or rest > 0:
            #         if ss[pos_y + 1][pos_x - 1] == 0:
            #             rest -= 1
            #         pos_y, pos_x = pos_y + 1, pos_x - 1
            #         length += 1
            #     else:
            #         break

if success:
    print('Yes')
else:
    print('No')

