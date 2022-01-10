a, b, c, d = map(int, input().strip().split())

ans = max(a * c, a * d, b * c, b * d)
print(ans)
