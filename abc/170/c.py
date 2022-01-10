x, n = map(int, input().strip().split())
ps = list(map(int, input().strip().split()))

min_m = -1
min_diff = 1e9
for m in range(102):
    diff = abs(m - x)
    if diff < min_diff and m not in ps:
        min_m = m
        min_diff = diff

print(min_m)
