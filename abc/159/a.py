n, m = map(int, input().strip().split())
ans = n * (n - 1) // 2 + m * (m - 1) // 2
print(ans)
