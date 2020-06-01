from collections import deque

n = int(input())
as_ = map(int, input().strip().split())

d = deque()

reversed = False
for a in as_:
    if reversed:
        d.appendleft(a)
    else:
        d.append(a)
    reversed = not reversed

if reversed:
    d.reverse()

ans = ' '.join(map(str, d))

print(ans)
