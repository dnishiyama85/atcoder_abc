import math
n, k = map(int, input().strip().split())

total = 0
for i in range(1, n + 1):
    total += i * ((k // i) ** n) % 1000000007

print(total)
