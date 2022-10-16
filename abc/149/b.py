a, b, k = map(int, input().strip().split())
if a >= k:
    ans = a - k, b
else:
    ans = 0, max(b - (k - a), 0)

print(ans[0], ans[1])
