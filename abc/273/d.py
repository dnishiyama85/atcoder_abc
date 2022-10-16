from collections import defaultdict
import bisect

h, w, rs, cs = map(int, input().strip().split())
n = int(input())

# r 行目にある壁の x 座標
walls_x = defaultdict(list)

# c 列目にある壁の y 座標
walls_y = defaultdict(list)

for _ in range(n):
    r, c = map(int, input().strip().split())
    r -= 1
    c -= 1
    walls_x[r].append(c)
    walls_y[c].append(r)


for r in walls_x:
    walls_x[r] = sorted(walls_x[r])

for c in walls_y:
    walls_y[c] = sorted(walls_y[c])

q = int(input())
current_y = rs - 1
current_x = cs - 1

for _ in range(q):
    d, l = input().strip().split()
    l = int(l)
    if d == 'L':
        ind = bisect.bisect_right(walls_x[current_y], current_x)
        current_x -= l
        if len(walls_x[current_y]) == 0 or ind == 0:
            # 左に壁はない
            current_x = max(current_x, 0)
        else:
            current_x = max(current_x, walls_x[current_y][ind - 1] + 1)

    elif d == 'R':
        # import pdb; pdb.set_trace()
        ind = bisect.bisect_left(walls_x[current_y], current_x)
        current_x += l
        if len(walls_x[current_y]) == 0 or ind == len(walls_x[current_y]):
            # 右に壁はない
            current_x = min(current_x, w - 1)
        else:
            current_x = min(current_x, walls_x[current_y][ind] - 1)

    elif d == 'U':
        # import pdb; pdb.set_trace()
        ind = bisect.bisect_right(walls_y[current_x], current_y)
        current_y -= l
        if len(walls_y[current_x]) == 0 or ind == 0:
            # 上に壁はない
            current_y = max(current_y, 0)
        else:
            current_y = max(current_y, walls_y[current_x][ind - 1] + 1)
    elif d == 'D':
        # import pdb; pdb.set_trace()
        ind = bisect.bisect_left(walls_y[current_x], current_y)
        current_y += l
        if len(walls_y[current_x]) == 0 or ind == len(walls_y[current_x]):
            # 下に壁はない
            current_y = min(current_y, h - 1)
        else:
            current_y = min(current_y, walls_y[current_x][ind] - 1)

    print(current_y + 1, current_x + 1)
