n = int(input())
as_ = list(map(int, input().strip().split()))

cum_alt_sum = [0] * n
for i in range(n):
    if i == 0:
        prev = 0
    else:
        prev = cum_alt_sum[i - 1]
    if i % 2 == 0:
        cum_alt_sum[i] = prev + as_[i]
    else:
        cum_alt_sum[i] = prev - as_[i]

ans = [0] * n
for i in range(n):
    if i == 0:
        ans[i] = cum_alt_sum[-1]
    else:
        ans[i] = - cum_alt_sum[i - 1] + (cum_alt_sum[-1] - cum_alt_sum[i - 1])
        if i % 2 == 1:
            ans[i] *= -1


print(' '.join(map(str, ans)))
