from collections import defaultdict

n = int(input())
as_ = map(int, input().strip().split())

counts = defaultdict(int)

for a in as_:
    counts[a] += 1

if max(counts.values()) > 1:
    print('NO')
else:
    print('YES')
