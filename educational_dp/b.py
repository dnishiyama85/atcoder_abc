# PyPy で提出しないと通らない
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
hs = list(map(int, input().strip().split()))

dp = [0] * n

for i in range(1, n):
    min_cost = 1e19
    for j in range(1, min(k + 1, i + 1)):
        cost = dp[i - j] + abs(hs[i] - hs[i - j])
        min_cost = min(cost, min_cost)
    dp[i] = min_cost

print(dp[n - 1])
