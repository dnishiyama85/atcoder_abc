n, k = map(int, input().strip().split())
hs = sorted([int(input()) for _ in range(n)])

ans = 1e15

for i in range(n - k + 1):
    h_max = hs[i + k - 1]
    h_min = hs[i]
    ans = min(h_max - h_min, ans)

print(ans)
