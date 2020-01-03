import numpy as np

n, m = map(int, input().strip().split())
array = [int(input()) for _ in range(m)]
is_broken = np.zeros(n + 1, dtype=np.bool)
for a in array:
    is_broken[a] = 1

a0 = 0
a1 = 1

if n == 1:
    if is_broken[n]:
        print(0)
    else:
        print(1)

else:
    for i in range(1, n + 1):
        if is_broken[i]:
            a2 = 0
        else:
            a2 = (a1 + a0) % 1000000007

        a0 = a1
        a1 = a2

    print(a1)
