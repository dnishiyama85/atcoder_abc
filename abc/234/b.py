import math

n = int(input())

xy = []
for _ in range(n):
    x, y = list(map(int, input().strip().split()))
    xy.append((x, y))

mx = 0
for x1, y1 in xy:
    for x2, y2 in xy:
        len2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
        mx = max(mx, len2)

print(math.sqrt(mx))
