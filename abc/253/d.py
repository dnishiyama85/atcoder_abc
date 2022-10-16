import math

n, a, b = map(int, input().strip().split())

s1 = n * (n + 1) // 2

# 1以上n以下であるkの倍数で最大のものは k * (n // k)
# 最小のものは k
# 個数は n // k
def sum_of_mult_k(k):
    min_mul = k
    max_mul = k * (n // k)
    return (n // k) * (min_mul + max_mul) // 2

sa = sum_of_mult_k(a)
sb = sum_of_mult_k(b)
sab = sum_of_mult_k(a * b // math.gcd(a, b))

ans = s1 - sa - sb + sab

print(ans)
