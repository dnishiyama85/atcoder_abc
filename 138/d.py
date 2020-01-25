from collections import defaultdict
from collections import deque
import time
import sys

input = sys.stdin.readline

# start = time.time()
n, q = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(n - 1)]
values = [list(map(int, input().strip().split())) for _ in range(q)]

# elapsed = time.time() - start
# print("elapsed_time:{0}".format(elapsed) + "[sec]")

edge_dict = defaultdict(list)
value_dict = defaultdict(int)
total_value_dict = defaultdict(int)
visited = [False] * n

for a, b in edges:
    edge_dict[a].append(b)
    edge_dict[b].append(a)

for p, x in values:
    value_dict[p] += x


qu = deque([1])
total_value_dict[1] = value_dict[1]
visited[0] = True

while len(qu) > 0:
    node = qu.popleft()
    next_nodes = [m for m in edge_dict[node] if not visited[m - 1]]
    for m in next_nodes:
        total_value_dict[m] = total_value_dict[node] + value_dict[m]
        visited[m - 1] = True
        qu.append(m)

print(' '.join([str(total_value_dict[i]) for i in range(1, n + 1)]))
