N, W = map(int, input().strip().split())
vs = []
ws = []
for _ in range(N):
    v, w = map(int, input().strip().split())
    vs.append(v)
    ws.append(w)

memo = {}
# i 番目まで入れる入れないを決めて、空き容量jとなったときに、
# 残りの選択で最大の価値を返す
def knapsack(i, j):
    if (i, j) in memo:
        return memo[(i, j)]

    if i == N - 1:
        memo[(i, j)] = 0
        return 0

    if j >= ws[i + 1]:
        # i + 1 番目の品物を入れるばあい
        v1 = knapsack(i + 1, j - ws[i + 1]) + vs[i + 1]
        # 入れないばあい
        v2 = knapsack(i + 1, j)
        ret = max(v1, v2)
    else:
        # 入らないので見送るしかない
        ret = knapsack(i + 1, j)

    memo[(i, j)] = ret
    return ret

print(knapsack(-1, W))
