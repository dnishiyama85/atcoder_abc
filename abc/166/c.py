n, m = map(int, input().strip().split())
hs = list(map(int, input().strip().split()))
edges = [list(map(int, input().strip().split())) for _ in range(m)]

matrix = [[] for _ in range(n)]
for a, b in edges:
    matrix[a - 1].append(b - 1)
    matrix[b - 1].append(a - 1)

good = 0
for a in range(n):
    bs = matrix[a]
    h = hs[a]
    highest = all([hs[b] < h for b in bs])
    if len(bs) == 0 or highest:
        good += 1

print(good)
