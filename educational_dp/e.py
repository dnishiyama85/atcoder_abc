INF = 1e10
n, w = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(n)]
data = [[INF, INF]] + data

max_value = n * 1000
# i番目に価値の総和がj以上となるように選んだときの重さの最小値 双対問題？
dp = [[INF] * (max_value + 1) for _ in range(n + 1)]

dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(max_value + 1):
        wi, vi = data[i][0], data[i][1]
        # i番目の品物を入れる場合
        take = dp[i - 1][j - vi] + wi if j - vi >= 0 else INF
        # 入れない場合
        dismiss = dp[i - 1][j]
        dp[i][j] = min(take, dismiss)


result = dp[-1]
for j in reversed(range(max_value + 1)):
    if result[j] <= w:
        print(j)
        break

