l, r = list(map(int, input().strip().split()))

if r - l >= 2019:
    print(0)
else:
    min_prod = 1e9
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            min_prod = min(min_prod, (i * j) % 2019)
    print(min_prod)
