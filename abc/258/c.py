N, Q = map(int, input().strip().split())
s = list(input().strip())
len_s = len(s)
pointer = 0
for q in range(Q):
    query = list(map(int, input().strip().split()))
    if query[0] == 1:
        x = query[1]
        pointer -= x
        pointer %= len_s
    else:
        x = query[1]
        print(s[(pointer + x - 1) % len_s])
