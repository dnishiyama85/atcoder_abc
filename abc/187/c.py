from collections import defaultdict
n = int(input())
ss = [input().strip() for _ in range(n)]

data = defaultdict(lambda: [0, 0])

for s in ss:
    if s[0] == '!':
        data[s[1:]][1] += 1
    else:
        data[s][0] += 1

for s, v in data.items():
    if v[0] * v[1] > 0:
        print(s)
        exit(0)

print('satisfiable')
