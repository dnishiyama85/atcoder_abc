import numpy as np

n = int(input())
data = [list(map(int, input().strip().split())) for _ in range(n)]

# i 日目に 活動 j をして夏休みを終了した
# ばあいの幸福の総和の最大値
dp = np.zeros((n, 3), dtype=np.int)
dp[0] = np.array(data[0], dtype=np.int)

for i in range(1, n):
    dp[i][0] = data[i][0] + max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = data[i][1] + max(dp[i - 1][2], dp[i - 1][0])
    dp[i][2] = data[i][2] + max(dp[i - 1][0], dp[i - 1][1])

ans = np.max(dp[n - 1])
print(ans)
