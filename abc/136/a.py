a, b, c = list(map(int, input().strip().split()))
ans = max(c - (a - b), 0)
print(ans)
