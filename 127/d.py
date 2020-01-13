import heapq

n, m = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))
heapq.heapify(as_)
data = [list(map(int, input().strip().split())) for _ in range(m)]

for b, c in data:
    for _ in range(b):
        smallest = as_[0]
        if smallest < c:
            heapq.heapreplace(as_, c)
        else:
            break

maximum = sum(as_)
print(maximum)
