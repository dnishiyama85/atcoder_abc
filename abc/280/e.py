import numpy as np

n, p = map(int, input().strip().split())

dp = np.zeros((n, 3), dtype=np.int64)

dp[n//2, 0] = (p / 100) ** (n//2)
dp[n//2, 1] = n * ((p / 100) ** (n//2 - 1)) * ((1 - p) / 100)
dp[n//2, 2] = n * (n - 1) / 2 * ((p / 100) ** (n//2 - 2)) * (((1 - p) / 100) ** 2)

for k in range(n // 2 + 1, n + 1):
    dp[k, 0] =