n = int(input())
bs = list(map(int, input().strip().split()))

as_ = [0] * n

for i in range(n):
    if i == 0:
        as_[i] = bs[i]
    elif i < n - 1:
        as_[i] = min(bs[i - 1], bs[i])
    else:
        as_[i] = bs[i - 1]

print(sum(as_))
