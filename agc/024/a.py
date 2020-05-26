import numpy as np

a, b, c, k = map(int, input().strip().split())


def mono(a, b, c):
    return b + c, c + a, a + b


# ダブリング
def doubling(a, b, c, coeff):
    vec = np.array([a, b, c])
    result = np.dot(coeff, vec)
    return result


def doubling_n_times(a, b, c, n):
    coeff = np.array([
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ], dtype=np.int)
    for i in range(n - 1):
        coeff = np.dot(coeff, coeff)

    a, b, c = doubling(a, b, c, coeff)

    return a, b, c


def solve(a, b, c, k):
    pow = 0
    while k > 0:
        bit = k % 2
        k //= 2
        pow += 1
        if bit == 0:
            continue

        a, b, c = doubling_n_times(a, b, c, pow)

    return a, b, c


def solve_naively(a, b, c, k):
    for i in range(k):
        a, b, c = mono(a, b, c)
        if i + 1 in (1, 2, 4, 8, 16, 32):
            print("a, b, c, i + 1 = ", a, b, c, i + 1)

    return a, b, c


a, b, c = solve(a, b, c, k)

ans = a - b
if abs(ans) > 1e18:
    print('Unfair')
else:
    print(ans)
