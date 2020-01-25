n = int(input())
ps = list(map(int, input().strip().split()))

cum_min = [0] * n

min_p = 1e9
for i in range(n):
    cum_min[i] = min(min_p, ps[i])
    min_p = cum_min[i]

count = 0
for i in range(n):
    if cum_min[i] == ps[i]:
        count += 1

print(count)
