import sys
sys.setrecursionlimit(2000000)

n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().strip().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

for i in range(n):
    edges[i] = sorted(edges[i])


visited = {0}
path = []
# 深さ優先探索
def dfs(current):
    global visited, path
    path.append(current + 1)
    children = edges[current]
    for c in children:
        if c not in visited:
            visited.add(c)
            dfs(c)
            path.append(current + 1)


dfs(0)
print(' '.join(map(str, path)))
