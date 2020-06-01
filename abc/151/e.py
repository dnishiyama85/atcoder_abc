from scipy.special import comb

n, k = map(int, input().strip().split())
as_ = sorted(map(int, input().strip().split()))

mod = 1000000000 + 7
total = 0
for mn in range(n - k + 1):
    min_x = as_[mn]
    for mx in range(n - 1, mn + k - 1, -1):
        max_x = as_[mx]
        print("min = ", min_x, ", max = ", max_x)
        comb_ = comb(mx - mn, k, exact=True)
        print("comb = ", comb_)
        total += (comb_ * (max_x - min_x)) % mod

print(total)
