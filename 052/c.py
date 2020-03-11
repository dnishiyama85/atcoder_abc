from collections import defaultdict

n = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


factors = defaultdict(int)
for i in range(1, n + 1):
    ps = prime_factorize(i)
    for p in ps:
        factors[p] += 1

count = 1
for p, m in factors.items():
    count *= (1 + m)
    count %= 1000000007

print(count)
