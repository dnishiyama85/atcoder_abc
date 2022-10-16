x, k = map(int, input().strip().split())

for i in range(k):
    d = x % (10 ** (i + 1))

    if d // (10 ** i) >= 5:
        x = x - d + 10 ** (i + 1)
    else:
        x = x - d


print(int(x))
