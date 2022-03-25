n = int(input())
as_ = list(map(int, input().strip().split()))

cumsum = [0] * n
subtotal = 0
for i in range(n):
    subtotal += as_[i]
    cumsum[i] = subtotal

for k in range(1, n + 1):
    mx = 0
    for s in range(0, n - k + 1):
        subtract = cumsum[s - 1] if s > 0 else 0
        mx = max(mx, cumsum[s + k - 1] - subtract)

    print(mx)
