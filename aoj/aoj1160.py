import sys
import threading

sys.setrecursionlimit(67108864) #64MB
threading.stack_size(1024*1024)  #2の20乗のstackを確保=メモリの確保

while True:
    w, h = map(int, input().strip().split())
    if w == 0 and h == 0:
        break

    c = []
    for _ in range(h):
        row = list(map(int, input().strip().split()))
        c.append(row)

    # 番兵を配置
    c2 = [[0] * (w + 2) for _ in range(h + 2)]
    for x in range(w):
        for y in range(h):
            c2[y + 1][x + 1] = c[y][x]

    # チェック済みマス
    checked = [[0] * (w + 2) for _ in range(h + 2)]

    # 深さ優先探索
    def dfs(x, y):
        global checked
        # 現在値がチェック済みならリターン
        if checked[y][x] == 1:
            return

        # 現在値が海ならリターン
        if c2[y][x] == 0:
            return

        # そうでなければチェック済みにする。
        checked[y][x] = 1
        # 隣接マスの探索
        adjacents = [(x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
                     (x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1)]
        for next_x, next_y in adjacents:
            if c2[next_y][next_x] == 1:
                dfs(next_x, next_y)

    count = 0
    # マスを一つずつ見ていく
    for x in range(1, w + 1):
        for y in range(1, h + 1):
            if c2[y][x] == 1 and checked[y][x] == 0:
                # 未チェックの陸地を発見
                count += 1
                dfs(x, y)

    print(count)
