import numpy as np

n, m = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))
cs = list(map(int, input().strip().split()))

as_ = np.array(as_, dtype=np.int)
cs = np.array(cs, dtype=np.int)

bs = np.zeros(m + 1)
for d in range(0, n):
