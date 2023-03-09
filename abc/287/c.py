n, m = map(int, input().strip().split())

edges = []
for _ in range(m):
    u, v = map(int, input().strip().split())
    u -= 1
    v -= 1
    edges.append((u, v))

if n != m + 1:
    print('No')
    exit(0)

nodes = [[] for _ in range(n)]

for u, v in edges:
    nodes[u].append(v)
    nodes[v].append(u)

# edge が一つしかない node を探す
now = None
for i, node in enumerate(nodes):
    if len(node) == 1:
        now = i

if now is None:
    print('No')
    exit(0)

# グラフが連結か判定
from collections import deque
q = deque()
q.append(now)
visited = [False for _ in range(n)]
visited[now] = True
while len(q) > 0:
    n0 = q.popleft()
    next_nodes = nodes[n0]
    for n1 in next_nodes:
        if visited[n1]:
            continue
        else:
            visited[n1] = True
            q.append(n1)

if all(visited):
    print('Yes')
else:
    print('No')
