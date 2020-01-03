# import math
import fractions
from functools import reduce

n, x = map(int, input().strip().split())
xs = list(map(int, input().strip().split()))

for i in range(n):
    xs[i] = abs(xs[i] - x)

ans = reduce(fractions.gcd, xs)

print(ans)
