from collections import deque

n = int(input())
s = list(reversed(list(input().strip())))

q = deque([n])

for d in s:
    n -= 1
    if d == 'L':
        q.append(n)
    else:
        q.appendleft(n)

ans = map(str, q)
print(' '.join(ans))

