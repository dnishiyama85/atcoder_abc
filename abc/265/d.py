import numpy as np

n, p, q, r = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))

cumsum = np.cumsum(as_)

i = -1

def bisec(origin, target):
    base = 0 if origin < 0 else cumsum[origin]
    left = origin + 1
    right = n - 1
    while left < right:
        center = (left + right) // 2
        if cumsum[center] - base == target:
            return center
        if cumsum[center + 1] - base == target:
            return center + 1
        if cumsum[center] - base < target:
            left = center + 1
        else:
            right = center

    return None

found = False
while i <= n - 3:
    origin = i

    p_idx = bisec(origin, p)
    if p_idx:
        origin = p_idx
        q_idx = bisec(origin, q)
        if q_idx:
            origin = q_idx
            r_idx = bisec(origin, r)
            if r_idx:
                found = True
                break
            else:
                i += 1
        else:
            i += 1
    else:
        i += 1

if found:
    print('Yes')
else:
    print('No')



