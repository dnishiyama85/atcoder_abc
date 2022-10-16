from collections import deque

Q = int(input())

queries = []
for _ in range(Q):
    q = list(map(int, input().strip().split()))
    queries.append(q)

queue = deque()

for q in queries:
    if q[0] == 1:
        x, c = q[1], q[2]
        queue.append([x, c])
    else:
        c = q[1]
        rest = c
        total = 0
        while True:
            if rest <= 0:
                break
            head = queue[0]
            xh = head[0]
            ch = head[1]
            if ch >= rest:
                total += rest * xh
                queue[0][1] -= rest
                rest = 0
            else:
                total += ch * xh
                queue.popleft()
                rest -= ch

        print(total)
