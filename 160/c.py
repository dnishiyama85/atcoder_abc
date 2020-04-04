k, n = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))

total = k

minimum = 10000000000000
for i in range(n):
    if i == 0:
        dist = total - ((k - as_[-1]) + as_[0])
    else:
        dist = total - (as_[i] - as_[i - 1])

    minimum = min(minimum, dist)

print(minimum)
