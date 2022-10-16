import heapq
Q = int(input())

q_max = []
q_min = []
heapq.heapify(q_max)
heapq.heapify([q_min])
counts = {}

for _ in range(Q):
    query = list(map(int, input().strip().split()))
    if query[0] == 1:
        x = query[1]
        heapq.heappush(q_max, -x)
        heapq.heappush(q_min, x)
        if x not in counts:
            counts[x] = 0

        counts[x] += 1

    elif query[0] == 2:
        x = query[1]
        c = query[2]
        if x not in counts:
            counts[x] = 0

        counts[x] = max(counts[x] - c, 0)
    else:
        while True:
            _max = -q_max[0]
            if counts[_max] > 0:
                break
            else:
                heapq.heappop(q_max)

        while True:
            _min = q_min[0]
            if counts[_min] > 0:
                break
            else:
                heapq.heappop(q_min)

        print(_max - _min)
