import numpy as np

H, W = map(int, input().strip().split())
A = np.array([list(map(int, input().strip().split())) for _ in range(H)])
minA = np.min(A)
ans = np.sum(A - minA)
print(ans)
