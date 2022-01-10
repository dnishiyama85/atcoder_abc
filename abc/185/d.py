import numpy as np
n, m = map(int, input().strip().split())
a = sorted(map(int, input().strip().split()))

if m == 0:
    ans = 1
else:
    d = np.diff([0] + a + [n + 1]) - 1
    if np.max(d) == 0:
        ans = 0
    else:
        k = np.min(d[d > 0])

        if k == 0:
            ans = 0
        else:
            ans = np.sum((d + k - 1) // k)

print(ans)
