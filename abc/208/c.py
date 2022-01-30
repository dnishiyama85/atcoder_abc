n, k = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))

as2 = []
for i, a in enumerate(as_):
    as2.append((i, a))

as2 = sorted(as2, key=lambda x: x[1])

ranking = [-1] * n
for rk, (i, a) in enumerate(as2):
    ranking[i] = rk

q = k // n
r = k % n

for i in range(n):
    if ranking[i] < r:
        print(q + 1)
    else:
        print(q)
