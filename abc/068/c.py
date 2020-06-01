from collections import defaultdict

n, m = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(m)]


# 島iから行ける島のリスト
reachables = defaultdict(set)
for a, b in data:
    reachables[a].add(b)
    reachables[b].add(a)

# 島1から行けるところ
reachables_from1 = reachables[1]
possible = False
for i in reachables_from1:
    if n in reachables[i]:
        possible = True
        break

if possible:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
