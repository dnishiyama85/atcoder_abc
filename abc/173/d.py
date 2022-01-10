n = int(input())
as_ = list(map(int, input().strip().split()))
as_ = sorted(as_, reverse=True)


comfort = 0
for i in range(1, n):
    parent = i // 2
    comfort += as_[parent]

print(comfort)
