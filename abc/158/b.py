n, a, b = map(int, input().strip().split())
q = n // (a + b)
r = n % (a + b)

if r > a:
    res_b = a
else:
    res_b = r

ans = q * a + res_b
print(ans)
