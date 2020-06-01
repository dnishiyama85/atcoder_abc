n, k, q = map(int, input().strip().split())
ans = []
for i in range(q):
    ans.append(int(input()))

# ポイントが減らなかった回数
saved = [0] * n
for a in ans:
    saved[a - 1] += 1

for s in saved:
    if k - q + s > 0:
        print('Yes')
    else:
        print('No')
