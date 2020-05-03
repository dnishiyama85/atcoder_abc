from collections import defaultdict

n = int(input())
ss = [input().strip() for _ in range(n)]

d = defaultdict(int)

for s in ss:
    d[s] += 1

cnt = len(d.keys())

print(cnt)
