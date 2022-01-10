from collections import defaultdict

n = int(input())
as_ = map(int, input().strip().split())

d = defaultdict(int)

for a in as_:
    d[a] += 1

counts = 0
for k, v in d.items():
    if k < v:
        counts += v - k
    elif k > v:
        counts += v

print(counts)
