import numpy as np

h, w = map(int, input().strip().split())

maze = np.ones((h + 2, w + 2), dtype=np.int)

for i in range(1, h + 1):
    row = input().strip()
    for j in range(1, w + 1):
        maze[i, j] = 0 if row[j - 1] == '.' else 1


def bfs(maze, si, sj):
    assert maze[si, sj] == 0
    infty = -1
    distances = np.full((h + 2, w + 2), infty, dtype=np.int)
    queue = []
    queue.append((si, sj))
    distances[si, sj] = 0
    while len(queue) > 0:
        ci, cj = queue.pop(0)
        d = distances[ci, cj]
        left = (ci, cj - 1)
        right = (ci, cj + 1)
        up = (ci - 1, cj)
        down = (ci + 1, cj)
        nexts = [left, right, up, down]
        for ni, nj in nexts:
            if not (1 <= ni and ni <= h \
               and 1 <= nj and nj <= w):
                continue
            if distances[ni, nj] != infty:
                continue
            if maze[ni, nj] == 1:
                continue
            distances[ni, nj] = d + 1
            queue.append((ni, nj))

    return distances


max_dist = 0
for si in range(1, h + 1):
    for sj in range(1, w + 1):
        if maze[si, sj] == 0:
            distances = bfs(maze, si, sj)
            mx = np.max(distances)
            max_dist = max(max_dist, mx)

print(max_dist)
