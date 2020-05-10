import numpy as np
import math

n, d = map(int, input().strip().split())
points = np.array([list(map(int, input().strip().split())) for _ in range(n)])


def is_square(num):
    root = int(math.sqrt(num))
    return root ** 2 == num

counts = 0
for i in range(n):
    for j in range(i + 1, n):
        pi = points[i]
        pj = points[j]
        d2 = np.sum((pi - pj) ** 2)
        if is_square(d2):
            counts += 1

print(counts)
