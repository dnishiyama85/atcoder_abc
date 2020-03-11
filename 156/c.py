import numpy as np

n = int(input())
xs = list(map(int, input().strip().split()))
mn = min(xs)
mx = max(xs)
xs = np.array(xs)
diffs = np.empty((100, n), dtype=np.int)
for p in range(100):
    diffs[p] = xs - (p + 1)

ans = np.min(np.sum(diffs**2, axis=1))

print(ans)
