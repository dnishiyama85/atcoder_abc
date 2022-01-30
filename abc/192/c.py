n, k = list(map(int, input().strip().split()))


def g1(x):
    x_str = str(x)
    digits = list(x_str)
    digits = sorted(digits, reverse=True)
    g1_str = int(''.join(digits))
    return int(g1_str)


def g2(x):
    x_str = str(x)
    digits = list(x_str)
    digits = sorted(digits)
    g1_str = int(''.join(digits))
    return int(g1_str)


def f(x):
    return g1(x) - g2(x)

a = n
for _ in range(k):
    a = f(a)

print(a)
