x, y, n = map(int, input().strip().split())

if 3 * x < y:
    ans = n * x
else:
    ans = (n // 3) * y + (n % 3) * x

print(ans)
