from collections import deque
from sys import stdin
input = stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().strip().split())
    cs = list(map(int, input().strip().split()))

    edges = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().strip().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)


    visited = {}
    q = deque([(0, n - 1)])
    visited[(0, n - 1)] = 0
    reach = False
    while len(q) > 0:
        tak, aok = q.popleft()
        if tak == n - 1 and aok == 0:
            print(visited[(tak, aok)])
            reach = True
            break
        next_tak = edges[tak]
        next_aok = edges[aok]
        for next_t in next_tak:
            for next_a in next_aok:
                if (next_t, next_a) in visited:
                    continue
                else:
                    next_t_color = cs[next_t]
                    next_a_color = cs[next_a]
                    if next_t_color != next_a_color:
                        visited[(next_t, next_a)] = visited[(tak, aok)] + 1
                        q.append((next_t, next_a))

    if not reach:
        print(-1)
