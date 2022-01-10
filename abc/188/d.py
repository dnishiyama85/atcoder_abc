import numpy as np
import sys
input = sys.stdin.readline

N, C = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(N)]
data = np.array(data, dtype=np.int64)

compressed = [None] * (len(data) * 2)
for i, (a, b, c) in enumerate(data):
    A = (a, i, +1)
    B = (b + 1, i, -1)
    compressed[2 * i] = A
    compressed[2 * i + 1] = B

compressed = sorted(compressed, key=lambda c: c[0])

imos = np.zeros(len(compressed), dtype=np.int64)
for c, (a, i, t) in enumerate(compressed):
    cost = data[i][2]
    imos[c] += t * cost

# current_cost = 0
# total_cost = 0
# for c in range(len(imos) - 1):
#     im = imos[c]
#     current_cost += im
#     abc = compressed[c]
#     next_abc = compressed[c + 1]
#     duration = next_abc[0] - abc[0]
#     total_cost += min(current_cost, C) * duration
#
costs = np.cumsum(imos)
costs = costs[:-1]
duration = np.diff(np.array([c[0] for c in compressed]))
# print(duration)
# print(costs)
total_cost = np.sum(np.minimum(costs, C) * duration)

print(total_cost)
