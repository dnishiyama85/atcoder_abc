import heapq

n, m = map(int, input().strip().split())
heap = list(map(lambda a: -int(a), input().strip().split()))

heapq.heapify(heap)

for i in range(m):
    highest = heap[0]
    heapq.heapreplace(heap, highest / 2.0)

ans = -sum(map(int, heap))
print(ans)
