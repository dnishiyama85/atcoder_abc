import math

n, k = map(int, input().strip().split())


prob = 0
for m in range(1, n + 1):
    if m >= k:
        prob += 1 / n
    else:
        p = math.ceil(math.log(k / m) / math.log(2))
        prob += (1 / n) / (2 ** p)

print(prob)
