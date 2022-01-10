n = int(input())
as_ = list(map(int, input().strip().split()))
x = int(input())

s = sum(as_)
m = x // s
x -= s * m
count = m * n
for i, a in enumerate(as_):
    x -= a
    count += 1
    if x < 0:
        break

print(count)
