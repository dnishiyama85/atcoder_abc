from collections import defaultdict

n, x, y = map(int, input().strip().split())

x -= 1
y -= 1

dist_counts = defaultdict(int)
for i in range(n):
    for j in range(i + 1, n):
        path1 = abs(j - i)
        path2 = abs(x - i) + 1 + abs(y - j)
        dist = min(abs(j - i), path2)
        dist_counts[dist] += 1

for k in range(1, n):
    print(dist_counts[k])
