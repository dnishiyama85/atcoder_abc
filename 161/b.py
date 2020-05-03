n, m = map(int, input().strip().split())
as_ = map(int, input().strip().split())

as_ = sorted(as_, reverse=True)

boundary = as_[m - 1]
if boundary < sum(as_) /(4 * m):
    print('No')
else:
    print('Yes')
