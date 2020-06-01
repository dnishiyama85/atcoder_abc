from collections import defaultdict

n = int(input())
ds = map(int, input().strip().split())
m = int(input())
ts = map(int, input().strip().split())

prepared = defaultdict(int)

for d in ds:
    prepared[d] += 1

for t in ts:
    if prepared[t] > 0:
        prepared[t] -= 1
    else:
        print('NO')
        exit(0)

print('YES')
