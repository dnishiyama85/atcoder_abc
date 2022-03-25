from collections import defaultdict

n = int(input())
as_ = list(map(int, input().strip().split()))

d = defaultdict(int)
for a in as_:
    d[a] += 1

print(len(d.keys()))
