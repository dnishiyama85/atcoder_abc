n = int(input())
tree = [[] for _ in range(n + 1)]
ds = [-1] * (n + 1)

for _ in range(n):
    line = list(map(int, input().strip().split()))
    node_id = line[0]
    num_edges = line[1]
    if num_edges > 0:
        children = line[2:]
    else:
        children = []

    tree[node_id] = children


queue = [1]
ds[1] = 0
while len(queue) > 0:
    node_id = queue.pop(0)
    previous_d = ds[node_id]
    children = tree[node_id]
    for child_id in children:
        if ds[child_id] < 0:
            ds[child_id] = previous_d + 1
            queue.append(child_id)

for node_id in range(1, n + 1):
    print(node_id, ds[node_id])
