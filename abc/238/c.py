n = int(input())

# n の桁数
digits = len(str(n))

ans = 0
for d in range(1, digits + 1):
    a = 10**(d - 1)
    if d < digits:
        b = 10**d - 1
    else:
        b = n

    ans += ((b * (b + 1) - (a - 1) * a) // 2 - (a - 1) * (b - a + 1)) % 998244353

ans %= 998244353
print(ans)
