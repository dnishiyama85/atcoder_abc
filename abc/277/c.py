from sys import stdin
from collections import  defaultdict
input = stdin.readline

n = int(input())
nodes = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().strip().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = set()

stack = [1]
max_floor = 1
visited.add(1)
while len(stack) > 0:
    now = stack.pop()
    max_floor = max(max_floor, now)
    floors = nodes[now]
    for f in floors:
        if f not in visited:
            visited.add(f)
            stack.append(f)

print(max_floor)
