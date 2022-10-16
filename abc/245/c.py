import numpy as np

n, k = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))
bs = list(map(int, input().strip().split()))

dp = np.zeros((n, 2), dtype=np.int)  # i 番目に a, b を選んだ場合に条件を満たせるか
dp[0] = [1, 1]

for i in range(1, n):
    if dp[i - 1, 0] == 1:
        # 前に A を選べた。→ 次に A または B を選べるか？
        if abs(as_[i - 1] - as_[i]) <= k:
            dp[i, 0] = 1
        if abs(as_[i - 1] - bs[i]) <= k:
            dp[i, 1] = 1
    if dp[i - 1, 1] == 1:
        # 前に B を選べた。
        if abs(bs[i - 1] - as_[i]) <= k:
            dp[i, 0] = 1
        if abs(bs[i - 1] - bs[i]) <= k:
            dp[i, 1] = 1

if dp[n - 1, 0] == 1 or dp[n - 1, 1] == 1:
    print('Yes')
else:
    print('No')
