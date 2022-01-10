import itertools
import numpy as np

N, K = map(int, input().strip().split())

cities = np.arange(1, N)
T = [list(map(int, input().strip().split())) for _ in range(N)]
T = np.array(T)

count = 0
for travel in itertools.permutations(cities):
    travel = [0] + list(travel)
    total_time = 0
    for i in range(N):
        start = travel[i]
        end = travel[(i + 1) % N]
        total_time += T[start][end]

    if total_time == K:
        count += 1

print(count)
