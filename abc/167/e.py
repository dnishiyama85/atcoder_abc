n, m, k = map(int, input().strip().split())

ways = [0] * n

for i in range(n):
    if i == 0:
        ways[i] = m
    else:
        way = ways[i - 1] * (m - 1)
        way %= 998244353
        ways[i] = way

total = 0
nCr = 1
for i in range(k + 1):
    nCr *= (n - i) // (i + 1) if i > 0 else 1
    total += ways[-(i + 1)] * nCr
    total %= 998244353

print(total % 998244353)
