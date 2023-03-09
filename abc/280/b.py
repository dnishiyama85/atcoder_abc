n = int(input())
ss = list(map(int, input().strip().split()))
as_ = []
for i, s in enumerate(ss):
    if i == 0:
        as_.append(s)
    else:
        as_.append(s - ss[i - 1])

print(*as_)
