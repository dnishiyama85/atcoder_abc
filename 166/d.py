x = int(input())

p = 1
while p * p <= x:
    if x % p != 0:
        p += 1
        continue

    q = x // p
    a = 0
    while a < 1000:
        b = a - p
        f = a**4 + a**3 * b + a**2 * b**2 + a * b**3 + b**4
        if f == q:
            print(a, b)
            exit(0)
        a += 1
    p += 1
