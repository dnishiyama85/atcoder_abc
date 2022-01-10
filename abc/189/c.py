import numpy as np

N = int(input())
A = list(map(int, input().strip().split()))

min_cum = np.zeros_like(A)

for i, a in enumerate(A):
    if i == 0:
        min_cum[i] = a
    else:
        min_cum[i] = min(min_cum[i - 1], a)

for l in range(N):
    # ここで r についてにぶたん
    r1 = l
    r2 = N - 1
    min_ = min(min_cum[r2], min_cum[l])
    while r1 < r2:
        c = (r1 + r2) // 2
