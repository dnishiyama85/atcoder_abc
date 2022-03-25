from collections import defaultdict

# n は高々 2^n <= 10^5 なる n しかない → 16くらい
n, x = map(int, input().strip().split())
data = []
for _ in range(n):
    line = list(map(int, input().strip().split()))
    as_ = line[1:]
    data.append(as_)

# i 番目の袋まで取り出したときにそれまでの数の総積が y になる組み合わせの数
# d[i, y] = sum_j d[i - 1, y // a_ij]

max_num = 10 ** 5 + 1
dp = {}
for i in range(17):
    dp[i] = defaultdict(int)

for i, as_ in enumerate(data):
    if i == 0:
        for a in as_:
            dp[i][a] += 1
    else:
        non_zero_prev_ys = dp[i - 1].keys()
        for prev_y in non_zero_prev_ys:
            for a in as_:
                y = prev_y * a
                dp[i][y] += dp[i - 1][prev_y]

print(dp[n - 1][x])
