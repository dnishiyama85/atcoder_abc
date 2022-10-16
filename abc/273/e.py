from collections import defaultdict

q = int(input())

a = []
note = defaultdict(list)
out = []
for _ in range(q):
    query = input().split()
    com = query[0]
    if com == 'ADD':
        x = query[1]
        a.append(x)
    elif com == 'DELETE':
        a.pop(-1)
    elif com == 'SAVE':
        y = query[1]
        note[y] = a.copy()
    elif com == 'LOAD':
        z = query[1]
        a = note[z]

    out.append(a[-1] if len(a) > 0 else -1)

print(' '.join(map(str, out)))
