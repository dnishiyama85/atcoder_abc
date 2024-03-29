n = int(input())
data = []

# 木の構築フェーズ
tree = [[] for _ in range(n + 1)]
f = [None] * (n + 1)
v = [None] * (n + 1)

for _ in range(n):
    line = list(map(int, input().strip().split()))
    node_id = line[0]
    num_edges = line[1]
    if num_edges > 0:
        children = line[2:]
    else:
        children = []

    tree[node_id] = children


# 木の探索フェーズ
time = 0
def dfs(node_id):
    global time
    if v[node_id] is not None:
        # 訪問済み
        return

    time += 1
    v[node_id] = time
    children = sorted(tree[node_id])

    for child_id in children:
        dfs(child_id)

    time += 1
    f[node_id] = time


dfs(1)
while any([_v is None for _v in v[1:]]):
    node_ids = [i for i in range(1, n + 1) if v[i] is None]
    node_id = node_ids[0]
    dfs(node_id)


for node_id in range(1, n + 1):
    print(node_id, v[node_id], f[node_id])
