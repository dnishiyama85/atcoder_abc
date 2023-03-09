n, m = map(int, input().strip().split())
edges = [[] for _ in range(n)]

for edge_id in range(m):
    u, v = map(int, input().strip().split())
    u -= 1
    v -= 1
    edges[u].append((v, edge_id))
    edges[v].append((u, edge_id))


checked_edges = set()
checked_nodes = set()

# 深さ優先探索を行う
def search(u):
    global checked_edges, checked_nodes

    num_nodes = 0
    num_edges = 0
    if u in checked_nodes:
        return -1

    stack = [u]
    while len(stack) > 0:
        u = stack.pop()
        if u in checked_nodes:
            continue
        num_nodes += 1
        checked_nodes.add(u)
        vs = edges[u]
        for v, eid in vs:
            if eid not in checked_edges:
                num_edges += 1
                checked_edges.add(eid)

            if v not in checked_nodes:
                stack.append(v)
    # print(f"nn = {num_nodes}, num_edges = {num_edges}")
    return num_nodes > 0 and (num_nodes == num_edges)


node = 0
ans = True
while node < n:
    # import pdb; pdb.set_trace()
    ret = search(node)
    # print("ret = ", ret)
    if ret == -1:
        node += 1
        continue
    else:
        ans = ans and ret

    node += 1

if ans:
    print('Yes')
else:
    print('No')
