n = int(input())
as_ = list(map(int, input().strip().split()))

inf = 1e100
# 最初の行動は取る約束
# 行動iを取らない場合/取る場合の費用の最小値
dp1 = [[0] * 2 for _ in range(n)]

# 最後(i == n - 1)の行動
dp1[n - 1][0] = 0
dp1[n - 1][1] = as_[n - 1]

for i in range(n-2, -1, -1):
    if i == 0:
        dp1[i][0] = inf
        dp1[i][1] = as_[i] + min(dp1[i + 1][0], dp1[i + 1][1])
    else:
        # i 番目の行動を取らない場合、i + 1 番目の行動は取るしかない。
        dp1[i][0] = dp1[i + 1][1]
        # i 番目の行動を取る場合、 i + 1 番目の行動は取る場合と取らない場合の可能性がある
        dp1[i][1] = as_[i] + min(dp1[i + 1][0], dp1[i + 1][1])

min1 = dp1[0][1]


# 最初の行動は取らない約束
dp1 = [[0] * 2 for _ in range(n)]

# 最後(i == n - 1)の行動は取るしかない。
dp1[n - 1][0] = inf
dp1[n - 1][1] = as_[n - 1]

for i in range(n-2, -1, -1):
    if i == 0:
        dp1[i][0] = dp1[i + 1][1]
        dp1[i][1] = inf
    else:
        # i 番目の行動を取らない場合、i + 1 番目の行動は取るしかない。
        dp1[i][0] = dp1[i + 1][1]
        # i 番目の行動を取る場合、 i + 1 番目の行動は取る場合と取らない場合の可能性がある
        dp1[i][1] = as_[i] + min(dp1[i + 1][0], dp1[i + 1][1])

min2 = dp1[0][0]

print(min(min1, min2))
