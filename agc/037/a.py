import numpy as np

s = input().strip()
dp = np.zeros((len(s), 2), dtype=np.int)

# 初期値
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 2 if s[0] != s[1] else 0
dp[1][1] = 1

for i in range(2, len(s)):
    d00 = dp[i - 1][0] + 1 if s[i] != s[i - 1] else -1
    d01 = dp[i - 1][1] + 1
    dp[i][0] = max(d00, d01)

    if i >= 3:
        d10 = dp[i - 2][0] + 1
        d11 = dp[i - 2][1] + 1 if s[i-1:i+1] != s[i-3:i-1] else -1
    else:
        d10 = dp[i - 2][0] + 1
        d11 = -1
    dp[i][1] = max(d10, d11)

ans = max(dp[-1][0], dp[-1][1])
print(ans)
