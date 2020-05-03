a, b, m = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))
bs = list(map(int, input().strip().split()))
xyc = [list(map(int, input().strip().split())) for _ in range(m)]

min_no_discount = min(as_) + min(bs)

min_discount = 1e20
for x, y, c in xyc:
    min_discount = min(min_discount, as_[x - 1] + bs[y - 1] - c)

print(min(min_discount, min_no_discount))
