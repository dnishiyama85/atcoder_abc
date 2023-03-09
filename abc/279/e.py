import numpy as np
n, m = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))

as_ = np.array(as_, dtype=np.int64)
as_ = as_ - 1


# まず full の互換の積を求める。
full = np.array([j for j in range(n)])

for k in range(m):
    ind = as_[k]
    full[ind], full[ind + 1] = full[ind + 1], full[ind]

R = np.array([j for j in range(n)])
Q = full.copy()

for i in range(m):
    if i > 0:
        ind = as_[i]
        R[ind], R[ind + 1] = R[ind + 1], R[ind]
