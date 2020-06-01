a, b = map(int, input().strip().split())


def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


factors_a = factorize(a)
factors_b = factorize(b)

factors_a = {f[0] for f in factors_a}
factors_b = {f[0] for f in factors_b}

commons = factors_a & factors_b

print(len(commons) + 1)
