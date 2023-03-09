n, q = map(int, input().strip().split())
points = [0] * (n + 1)

for i in range(q):
    e, x = map(int, input().strip().split())
    if e == 1:
        points[x] += 1
    elif e == 2:
        points[x] += 2
    elif e == 3:
        if points[x] >= 2:
            print('Yes')
        else:
            print('No')
