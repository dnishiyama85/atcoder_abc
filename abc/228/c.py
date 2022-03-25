import numpy as np

n, k = map(int, input().strip().split())

ps = []
for _ in range(n):
    p = list(map(int, input().strip().split()))
    ps.append(p)

ps = np.array(ps)

subtotal_until_day3 = np.sum(ps[:, :3], axis=1)
# print(subtotal_until_day3)

# 自分が満点=300点をとって、他の人は全員0点
# 自分 day3 の点数 + 300 が何位に相当するか？

sorted_subtotal = sorted(subtotal_until_day3, reverse=True)
# k番目に大きいスコア
T = sorted_subtotal[k - 1]

for s in subtotal_until_day3:
    total_score = s + 300
    if total_score >= T:
        print('Yes')
    else:
        print('No')
