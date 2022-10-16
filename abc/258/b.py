import numpy as np

n = int(input())
cells = []
for _ in range(n):
    row = list(map(int, list(input().strip())))
    cells.append(row)

cells = np.array(cells)

pi, pj = 0, 0
mx = -1
# スタート地点の探索
for i0 in range(n):
    for j0 in range(n):
        pi = i0
        pj = j0
        # 方向の探索
        vxs = [-1, 0, 1]
        vys = [-1, 0, 1]
        dir_x = None
        dir_y = None
        for vx in vxs:
            for vy in vys:
                if vx == 0 and vy == 0:
                    continue
                pi1 = pi
                pj1 = pj
                s = []
                for i in range(n):
                    s.append(str(cells[pi1, pj1]))
                    pi1 = pi1 + vy
                    if pi1 < 0:
                        pi1 = n - 1
                    if pi1 >= n:
                        pi1 = 0
                    pj1 = pj1 + vx
                    if pj1 < 0:
                        pj1 = n - 1
                    if pj1 >= n:
                        pj1 = 0

                s = int(''.join(s))
                if s > mx:
                    mx = s

print(mx)

