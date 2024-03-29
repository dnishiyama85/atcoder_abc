n = int(input())

rs = []
cs = []
for _ in range(n):
    r, c = map(int, input().strip().split())
    rs.append(r)
    cs.append(c)

# 区間DP [l, r)
dp = [[0] * n for _ in range(n)]

# 区間の長さが 2 の部分を初期化
for i in range(n - 1):
    dp[i][i + 1] = rs[i] * cs[i] * cs[i + 1]  # M_i * M_{i+1} とするしかない

# 区間の長さが3以上の部分をDPしていく
for length in range(3, n + 1):
    for l in range(0, n - length + 1):
        r = l + length - 1
        # どこで分けるのが最適か
        min_mul = 1000000000
        for j in range(l, r):
            # print(f"length = {length}, l = {l}, r = {r}, j = {j}")
            left_r = rs[l]
            left_c = cs[j]
            right_r = rs[j + 1]
            right_c = cs[r]
            num_mul = left_r * left_c * right_c + dp[l][j] + dp[j + 1][r]
            min_mul = min(min_mul, num_mul)
        dp[l][r] = min_mul


print(dp[0][n - 1])

