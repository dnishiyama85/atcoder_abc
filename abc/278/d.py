from collections import defaultdict

n = int(input())
as_ = list(map(int, input().strip().split()))
q = int(input())

diff = defaultdict(int)
base = None

for _ in range(q):
    row = list(map(int, input().strip().split()))
    if row[0] == 1:
        x = row[1]
        base = x
        diff = defaultdict(int)
    elif row[0] == 2:
        i, x = row[1], row[2]
        diff[i - 1] += x
    elif row[0] == 3:
        i = row[1]
        d = diff[i - 1]
        if base is None:
            print(as_[i - 1] + d)
        else:
            print(base + d)
