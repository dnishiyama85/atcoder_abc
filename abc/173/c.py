import numpy as np
h, w, k = map(int, input().strip().split())
cs = [list(input().strip()) for _ in range(h)]
grid = np.zeros((h, w), dtype=np.int)
for i, row in enumerate(cs):
    for j, cell in enumerate(row):
        if cell == '#':
            grid[i, j] = 1


def count_black(grid, bits_row, bits_col):
    mask = np.ones((h, w), dtype=np.int)
    for i in range(h):
        bit = bits_row >> i & 1
        if bit:
            mask[i] = 0
    for j in range(w):
        bit = bits_col >> j & 1
        if bit:
            mask[:, j] = 0

    return np.sum(grid * mask)

count = 0
for b_row in range(2 ** h):
    for b_col in range(2 ** w):
        c = count_black(grid, b_row, b_col)
        if c == k:
            count += 1

print(count)
