n, m = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))
bs = list(map(int, input().strip().split()))

as_ = sorted(as_)
bs = sorted(bs)

b_idx = 0

min0 = 1e20

for a in as_:
    while b_idx < m:
        d1 = abs(a - bs[b_idx])
        if b_idx == m - 1:
            min1 = d1
            break
        else:
            d2 = abs(a - bs[b_idx + 1])
            if d1 < d2:
                min1 = d1
                break
            else:
                b_idx += 1

    min0 = min(min0, min1)

print(min0)
