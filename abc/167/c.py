import numpy as np

n, m, x = map(int, input().strip().split())
cs = []
aij = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    cs.append(row[0])
    aij.append(row[1:])


def check(bits, n, m, x):
    cost = 0
    skills = np.zeros(m, dtype=np.int)
    for i in range(n):
        bit = bits & (2 ** i)
        if bit:
            cost += cs[i]
            skills += aij[i]

    if np.all(skills >= x):
        return cost
    else:
        return False


min_cost = 1e30


for bits in range(2**n):
    result = check(bits, n, m, x)
    if not result:
        continue

    min_cost = min(min_cost, result)


if min_cost == 1e30:
    print(-1)
else:
    print(min_cost)
