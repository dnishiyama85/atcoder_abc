from collections import deque

h, w = map(int, input().strip().split())
grid = ['#' * (w + 2)]

for _ in range(h):
    row = input().strip()
    row = '#' + row + '#'
    grid.append(row)

grid.append('#' * (w + 2))


q = deque()
q.append((1, 1))

mx = 1
distance = [[-1] * (w + 2) for _ in range(h + 1)]
distance[1][1] = 1

while len(q) > 0:
    y, x = q.popleft()
    next_yx = [(y + 1, x), (y, x + 1)]
    for ny, nx in next_yx:
        if grid[ny][nx] == '.' and distance[ny][nx] == -1:
            distance[ny][nx] = distance[y][x] + 1
            mx = max(mx, distance[ny][nx])
            q.append((ny, nx))

print(mx)
