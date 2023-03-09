n, q = map(int, input().strip().split())
follows = set()

for _ in range(q):
    t, a, b = map(int, input().strip().split())
    if t == 1:
        follows.add((a, b))
    elif t == 2:
        if (a, b) in follows:
            follows.remove((a, b))
    elif t == 3:
        if (a, b) in follows and (b, a) in follows:
            print('Yes')
        else:
            print('No')
