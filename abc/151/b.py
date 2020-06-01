n, k, m = map(int, input().strip().split())
as_ = map(int, input().strip().split())

sum1 = sum(as_)
x = max(n * m - sum1, 0)

if x <= k:
    print(x)
else:
    print(-1)
