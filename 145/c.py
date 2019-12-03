import itertools
import math

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().strip().split())
    points.append((x, y))


total = 0
for perm in itertools.permutations(points):
    for i in range(n - 1):
        p1 = perm[i]
        p2 = perm[i + 1]
        dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        total += dist

avg = total / math.factorial(n)


print(avg)
