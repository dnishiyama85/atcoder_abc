from collections import defaultdict

n = int(input())
ss = [input().strip() for _ in range(n)]

counts = defaultdict(int)

for s in ss:
    counts[s] += 1

items = list(counts.items())
items = sorted(items, key=lambda c: c[1], reverse=True)

max_value = items[0][1]
max_items = [item for item in items if item[1] == max_value]

keys = [item[0] for item in max_items]
keys = sorted(keys)

for key in keys:
    print(key)
