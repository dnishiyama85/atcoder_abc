n, c, k = map(int, input().strip().split())
ts = sorted([int(input()) for _ in range(n)])

buses = 0
passengers = 1
first = ts[0]
for t in ts[1:]:
    if t > first + k or passengers == c:
        buses += 1
        passengers = 1
        first = t
    else:
        passengers += 1

if passengers > 0:
    buses += 1

print(buses)
