n = int(input())
as_ = list(map(int, input().strip().split()))

node = [0] * (2 * n + 2)
node[1] = -1

for i, a in enumerate(as_):
    node[2 * (i + 1)] = a
    node[2 * (i + 1) + 1] = a

# アメーバ k から何代遡るとアメーバ1になるか
dp = [-1] * (2 * n + 2)
dp[1] = 0
for k in range(2, 2 * n + 2):
    # k の親
    parent_of_k = node[k]
    dp[k] = dp[parent_of_k] + 1


for k in range(1, 2 * n + 2):
    print(dp[k])
