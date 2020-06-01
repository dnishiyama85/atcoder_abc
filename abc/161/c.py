n, k = map(int, input().strip().split())

min_n = 1000000000000000000000000000
for i in range(1000):
    if n > k:
        n %= k
    n = abs(n - k)
    min_n = min(min_n, n)

print(min_n)
