import sys
import threading

sys.setrecursionlimit(67108864)  # 64MB
threading.stack_size(1024*1024)  # 2の20乗のstackを確保=メモリの確保

n, q = map(int, input().strip().split())

# 木の構築
nodes = [[] for _ in range(n + 1)]
counter = [0] * (n + 1)
total_counter = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().strip().split())
    nodes[a].append(b)
    nodes[b].append(a)

# クエリの処理
for _ in range(q):
    p, x = map(int, input().strip().split())
    counter[p] += x


# クエリの集計 (= 木の探索)
def dfs(node, count, parent):
    # このノードが持つカウンター
    x = counter[node]
    total_counter[node] = count + x
    # 子の探索
    next_nodes = nodes[node]
    for c in next_nodes:
        if c != parent:
            dfs(c, count + x, node)


dfs(1, 0, None)

print(' '.join(map(str, total_counter[1:])))
