n = int(input())
k = int(input())
xs = list(map(int, input().strip().split()))

total = 0

for i in range(n):
    x = xs[i]
    total += min(2 * x, 2 * (k - x))

print(total)
