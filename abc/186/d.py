import numpy as np

n = int(input())
as_ = map(int, input().strip().split())
as_ = np.array(sorted(as_, reverse=True))
cum = np.cumsum(as_)
C = cum[-1] - cum

ans = np.sum(as_ * (n - 1 - np.arange(0, n)) - C)

print(ans)
