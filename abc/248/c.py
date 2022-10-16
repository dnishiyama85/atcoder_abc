n, m, k = map(int, input().strip().split())
J = n * m
# 長さ i で和が j であるものの個数 = 整数 j をちょうど i 個に分割する方法の個数
# ただし順序が異なるものは異なる分割とみなす。
dp = [[0] * (J + 1) for _ in range(n + 1)]

# dp[i][j] = dp[i - 1][j - 1] + dp[i][j - i]

for j in range(1, J + 1):
    dp[1][j] = 1 if j <= m else 0

for i in range(2, n + 1):
    for j in range(i, J + 1):
        for j1 in range(max(0, j - m), j):
            dp[i][j] += dp[i - 1][j1]
            dp[i][j] %= 998244353

ans = 0
for j in range(1, k + 1):
    ans += dp[n][j]

ans %= 998244353
print(ans)
