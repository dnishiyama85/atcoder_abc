from collections import defaultdict
n, q = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))
queries = []
for _ in range(q):
    x, k = map(int, input().strip().split())
    queries.append((x, k))

d = {}
a_counts = defaultdict(int)
for i, a in enumerate(as_):
    prev_count = a_counts[a]
    a_counts[a] += 1
    d[(a, prev_count + 1)] = i + 1

for x, k in queries:
    if (x, k) in d:
        print(d[(x, k)])
    else:
        print(-1)
