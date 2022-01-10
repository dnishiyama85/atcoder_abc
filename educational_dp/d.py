n, w = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(n)]

# i番目に重さがj以下となるように選んだときの価値の総和の最大値
dp = [[0] * (w + 1) for _ in range(n)]

for i in range(0, n):
    for j in range(w + 1):
        # i 番目の品物の重さと価値
        wi, vi = data[i]
        if i == 0:
            take = vi if j - wi >= 0 else 0
            miss = 0
            dp[i][j] = max(take, miss)
        else:
            # i番目の品物を入れる場合
            take = dp[i - 1][j - wi] + vi if j - wi >= 0 else 0
            # 入れない場合
            miss = dp[i - 1][j]
            dp[i][j] = max(take, miss)

print(max(dp[n - 1]))
