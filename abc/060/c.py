N, T = map(int, input().strip().split())
ts = list(map(int, input().strip().split()))

total = 0

for i in range(N):
    if i == N - 1:
        total += T
    else:
        total += min(T, ts[i + 1] - ts[i])

print(total)
