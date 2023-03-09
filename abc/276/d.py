import numpy as np
n = int(input())
as_ = list(map(int, input().strip().split()))

factor_others = np.ones(n, dtype=np.int64)
powers_2 = np.zeros(n, dtype=np.int64)
powers_3 = np.zeros(n, dtype=np.int64)

for i, a in enumerate(as_):
    while a > 1 and a % 2 == 0:
        powers_2[i] += 1
        a //= 2
    while a > 1 and a % 3 == 0:
        powers_3[i] += 1
        a //= 3

    factor_others[i] = a

if not np.all(factor_others == factor_others[0]):
    print(-1)
else:
    min_power_2 = np.min(powers_2)
    min_power_3 = np.min(powers_3)

    ans = np.sum(powers_2 - min_power_2) + np.sum(powers_3 - min_power_3)
    print(ans)
