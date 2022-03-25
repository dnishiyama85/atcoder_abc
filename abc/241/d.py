import heapq
a = []
b = []
heapq.heapify(a)
heapq.heapify(b)

q = int(input())
for _ in range(q):
    query = list(map(int, input().strip().split()))
    q0 = query[0]
    if q0 == 1:
        heapq.heappush(a, query[1])
        heapq.heappush(b, -query[1])
    elif q0 == 2:
    elif q0 == 3:



