n = int(input())

# dp = np.zeros((n, 10), dtype=np.int)
dp = [[0] * 10 for _ in range(n)]

for j in range(1, 10):
    dp[0][j] = 1

for i in range(1, n):
    for j in range(1, 10):
        if j == 1:
            dp[i][j] = dp[i - 1][1] + dp[i - 1][2]
        elif j == 9:
            dp[i][j] = dp[i - 1][8] + dp[i - 1][9]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]

        dp[i][j] %= 998244353

ans = 0
for j in range(10):
    ans += dp[n - 1][j]

print(ans % 998244353)
