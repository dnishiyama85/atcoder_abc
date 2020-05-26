n = int(input())
as_ = list(map(int, input().strip().split()))

count = 0
for i, a in enumerate(as_):
    if as_[a - 1] == i + 1:
        count += 1

print(count // 2)
