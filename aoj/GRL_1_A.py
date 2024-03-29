# ダイクストラ法

import heapq

v, e, r = map(int, input().strip().split())
edges = []
for _ in range(e):
    s, t, d = map(int, input().strip().split())
    edges.append((s, t, d))


class Node:

    def __init__(self):
        self.edges_to = []
        self.edges_cost = []
        self.cost = None    # このノードへの現時点で判明している最小コスト

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost


# グラフの構築
nodes = [Node() for _ in range(v)]
for s, t, d in edges:
    nodes[s].edges_to.append(t)
    nodes[s].edges_cost.append(d)

# スタート地点はコスト0
origin = nodes[r]
origin.cost = 0

# 優先度付きキュー
queue = [origin]
heapq.heapify(queue)

# コストを確定していくループ
while len(queue) > 0:
    # コスト最小のノードを取り出し、確定にする。
    min_node = heapq.heappop(queue)

    # 確定ノードに繋がっているノードまでのコストを計算し、
    # 現在値より小さければ更新
    for to_id, d in zip(min_node.edges_to, min_node.edges_cost):
        node = nodes[to_id]
        new_cost = min_node.cost + d
        if (node.cost is None) or node.cost > new_cost:
            node.cost = new_cost
            heapq.heappush(queue, node)

for node in nodes:
    if node.cost is None:
        print('INF')
    else:
        print(node.cost)









