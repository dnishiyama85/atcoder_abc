from collections import defaultdict

n = int(input())
as_ = list(map(int, input().strip().split()))
ds = defaultdict(int)

for a in as_:
    ds[a] += 1

all = n * (n - 1) // 2
dup = 0
for d in ds.values():
    dup += d * (d - 1) // 2

ans = all - dup
print(ans)
