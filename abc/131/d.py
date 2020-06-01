n = int(input())
data = [list(map(int, input().strip().split())) for _ in range(n)]

data = sorted(data, key=lambda d: d[1])

work_time = 0
impossible = False
for a, b in data:
    deadline = b
    work_time += a
    if work_time > b:
        impossible = True
        break

if impossible:
    print('No')
else:
    print('Yes')

