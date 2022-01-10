S = int(input())

mod = 1000000007

dp = [0] * 2001

dp[0] = 0
dp[1] = 0
dp[2] = 0
dp[3] = 1

for s in range(4, S + 1):
    total = 1
    for k in range(3, s + 1):
        total += dp[s - k] % mod

    dp[s] = total % mod

print(dp[S])
