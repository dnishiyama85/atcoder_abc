import numpy as np

n = int(input())
hs = list(map(int, input().strip().split()))

# これまでを単調非減少にできるか
dp = np.zeros(n, dtype=np.bool)
dp[0] = True

for idx in range(1, n):
    if not dp[idx - 1]:
       dp[idx] = False
    elif hs[idx - 1] == hs[idx]:
        dp[idx] = True
    elif hs[idx - 1] < hs[idx]:
        dp[idx] = True
        hs[idx] -= 1
    else:
        dp[idx] = False

if dp[-1]:
    print('Yes')
else:
    print('No')
