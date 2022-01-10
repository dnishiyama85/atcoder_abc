import numpy as np

L = int(input())

max_partition = 12

# dp[i, j] = 長さ i の棒を j 個に分割する方法
dp = np.zeros((L + 1, max_partition + 1), dtype=np.int)
dp[:, :] = 0
dp[:, 1] = 1

for i in range(2, L + 1):
    for j in range(2, max_partition + 1):
        if i < j:
            dp[i, j] = 0
        else:
            dp[i, j] = 0
            for k in range(1, i):
                dp[i, j] += dp[i - k, j - 1]

# print(dp)
print(dp[L, max_partition])

