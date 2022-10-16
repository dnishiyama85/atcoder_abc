import numpy as np
import bisect

n, q = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))
xs = []
for _ in range(q):
    xs.append(int(input()))

as_ = sorted(as_)

cumsum = np.cumsum(as_)
for x in xs:
    x_ind = bisect.bisect(as_, x)
    if x_ind == n:
        ans = n * x - cumsum[-1]
    elif x_ind == 0:
        ans = cumsum[-1] - n * x
    else:
        sum1 = cumsum[x_ind - 1]
        sum2 = cumsum[-1] - cumsum[x_ind - 1]
        ans = (2 * x_ind - n) * x - sum1 + sum2

    print(ans)
