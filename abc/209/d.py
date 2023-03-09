n, q = map(int, input().strip().split())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().strip().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

queries = []
for _ in range(q):
    c, d = map(int, input().strip().split())
    queries.append((c - 1, d - 1))

# 木をトラバースして、各ノードの深さと親を調べる。
# 0 をルートとする。
parents = [None] * n
depths = [0] * n

parents[0] = None
depths[0] = 0

stack = [(0, 0, None)]
while len(stack) > 0:
    node, depth, parent = stack.pop()
    children = [c for c in edges[node] if c != parent]
    for c in children:
        parents[c] = node
        depths[c] = depth + 1
        stack.append((c, depth + 1, node))

# print(parents)
# print(depths)

for c, d in queries:
    # c の深さ + d の深さが偶数なら街で出会う奇数なら道路で出会う
    if (depths[c] + depths[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
