w, h = map(int, input().strip().split())

MOD = 1000000007


def factorial(k):
    f = 1
    for i in range(1, k + 1):
        f *= i
        f %= MOD
    return f


C = factorial(w + h - 2) // factorial(w - 1) // factorial(h - 1)
C %= MOD
print(C)
