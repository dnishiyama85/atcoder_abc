import sys
from collections import deque

input = sys.stdin.readline

n, x, y = map(int, input().strip().split())

x -= 1
y -= 1

edges = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().strip().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)


def bfs(v, goal, visited, prev):

    q = deque()

    q.append((v, prev))

    while len(q) > 0:
        v, prev = q.popleft()

        visited[v] = prev

        if v == goal:
            return visited

        for v_next in edges[v]:
            if visited[v_next]:
                continue

            q.append((v_next, v))

visited = [None] * n
prev = x
path = bfs(x, y, visited, prev)

v = y
forward_path = []
while True:
    forward_path.append(v + 1)
    if v == x:
        break
    v = visited[v]

forward_path = forward_path[::-1]
forward_path = map(str, forward_path)
print(' '.join(forward_path))

