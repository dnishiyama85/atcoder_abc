from collections import defaultdict

n, m, t = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))

data = defaultdict(int)
for _ in range(m):
    x, y = map(int, input().strip().split())
    data[x - 1] = y

now = 0
arrived = False
while True:
    if now == n - 1:
        arrived = True
        break

    t += data[now]

    if t > as_[now]:
        t -= as_[now]
        now += 1
    else:
        break

if arrived:
    print('Yes')
else:
    print('No')
