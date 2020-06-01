import numpy as np

h, w = map(int, input().strip().split())
table = [input().strip() for _ in range(h)]

numbers = np.zeros((h, w), dtype=np.int)

for i in range(h):
    for j in range(w):
        # 上
        up    = 1 if i > 0 and table[i - 1][j] == '#' else 0
        # 下
        down  = 1 if i < h - 1 and table[i + 1][j] == '#' else 0
        # 左
        left  = 1 if j > 0 and table[i][j - 1] == '#' else 0
        # 右
        right = 1 if j < w - 1 and table[i][j + 1] == '#' else 0
        # 左上
        left_up = 1 if j > 0 and i > 0 and table[i - 1][j - 1] == '#' else 0
        # 左下
        left_down = 1 if j > 0 and i < h - 1 and table[i + 1][j - 1] == '#' else 0
        # 右下
        right_down = 1 if j < w - 1 and i < h - 1 and table[i + 1][j + 1] == '#' else 0
        # 右上
        right_up = 1 if j < w - 1 and i > 0 and table[i - 1][j + 1] == '#' else 0

        numbers[i][j] = up + down + left + right \
                      + left_up + left_down + right_down + right_up


for i in range(h):
    for j in range(w):
        if table[i][j] == '#':
            print('#', end='')
        else:
            print(numbers[i][j], end='')
    print('')

