from collections import deque
import numpy as np

r, c = map(int, input().strip().split())
sy, sx = map(int, input().strip().split())
sy -= 1
sx -= 1
gy, gx = map(int, input().strip().split())
gy -= 1
gx -= 1

cells = []
for _ in range(r):
    row = input().strip()
    cells.append(row)

# 数値に変換
cells2 = [[0] * c for _ in range(r)]
for y in range(r):
    for x in range(c):
        if cells[y][x] == '.':
            cells2[y][x] = 1

# 訪問済みフラグ(最短距離格納）
visited = [[-1] * c for _ in range(r)]

q = deque()
q.append((sy, sx))
visited[sy][sx] = 0

ans = None

# print(np.array(cells2))

while len(q) > 0:
    y, x = q.popleft()
    # そのマスの最短距離
    d = visited[y][x]

    if y == gy and x == gx:
        # ゴールに着いた
        ans = d
        break

    adjacents = [
        (y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)
    ]
    # print(np.array(visited))
    for next_y, next_x in adjacents:
        # print("next_y, next_x = ", (next_y, next_x))
        # if next_y < 0 or r <= next_y or next_x < 0 or c <= next_x:
        #     continue
        if cells2[next_y][next_x] == 0:
            continue
        if visited[next_y][next_x] >= 0:
            continue
        # 最短距離確定
        visited[next_y][next_x] = d + 1
        # 探索キューに追加
        q.append((next_y, next_x))


print(ans)
