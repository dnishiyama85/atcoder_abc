import pprint
from collections import deque

h, w, n = map(int, input().strip().split())
map_array = [['X' for _ in range(w + 2)] for _ in range(h + 2)]

for i in range(h):
    row = list(input().strip())
    map_array[i + 1][1:-1] = row

# pprint.pprint(map_array)

route = ['S', '1', '2', '3', '4', '5', '6', '7', '8', '9']
point_to_coordinate = {}

for i in range(h + 2):
    for j in range(w + 2):
        for r in route:
            if map_array[i][j] == r:
                point_to_coordinate[r] = (i, j)

now = 0

total = 0
cheese = 0

while cheese < n:
    start = route[now]
    goal = route[now + 1]
    start_ij = point_to_coordinate[start]
    si, sj = start_ij
    goal_ij = point_to_coordinate[goal]

    distance = [[-1] * (w + 2) for _ in range(h + 2)]

    queue = deque()
    queue.append(start_ij)
    distance[si][sj] = 0
    while len(queue) > 0:
        pi, pj = queue.popleft()
        next_cells = [(pi - 1, pj), (pi + 1, pj), (pi, pj - 1), (pi, pj + 1)]
        for ni, nj in next_cells:
            if distance[ni][nj] == -1 and map_array[ni][nj] != 'X':
                # 未探索の場所に到達
                distance[ni][nj] = distance[pi][pj] + 1
                if (ni, nj) == goal_ij:
                    # チーズを見つけた
                    total += distance[ni][nj]
                    cheese += 1
                    now += 1
                else:
                    queue.append((ni, nj))

print(total)

