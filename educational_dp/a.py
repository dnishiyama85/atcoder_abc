n = int(input())
hs = list(map(int, input().strip().split()))

# 足場 i にたどり着くまでに支払うコストの総和の最小値
# 初期値として足場 0 にいるので dp[0] = 0
dp = [0] * n
# 足場 1 に行くための最小値は 0 → 1 と行く場合に当たるので
dp[1] = abs(hs[1] - hs[0])

# DP する
for i in range(2, n):
    cost_sum_1 = dp[i - 1] + abs(hs[i] - hs[i - 1])
    cost_sum_2 = dp[i - 2] + abs(hs[i] - hs[i - 2])
    dp[i] = min(cost_sum_1, cost_sum_2)

print(dp[n - 1])
