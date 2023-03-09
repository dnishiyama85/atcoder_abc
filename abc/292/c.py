n = int(input())

count = 0

memo = {}

def count_pair(t):
    global memo

    if t in memo:
        return memo[t]

    d = 1
    c = 0
    while d * d <= t:
        if t % d == 0:
            if t // d == d:
                c += 1
            else:
                c += 2

        d += 1

    memo[t] = c
    return c


for m in range(1, n + 1):
    k = n - m
    count += count_pair(m) * count_pair(k)

print(count)
