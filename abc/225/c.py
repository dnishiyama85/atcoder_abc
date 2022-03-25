import numpy as np

n, m = map(int, input().strip().split())
bij = []
for _ in range(n):
    raw = list(map(int, input().strip().split()))
    bij.append(raw)

bij = np.array(bij)
diff_raw = np.diff(bij, axis=0)
diff_col = np.diff(bij, axis=1)

if n == 1 and m == 1:
    print('Yes')
elif n == 1:
    if np.all(diff_col == 1):
        print('Yes')
    else:
        print('No')
elif m == 1:
    if np.all(diff_raw == 7):
        print('Yes')
    else:
        print('No')
else:
    if np.all(diff_raw == 7) and np.all(diff_col == 1):
        rotated = False
        for j in range(m - 1):
            if bij[0, j] % 7 == 0 and bij[0, j + 1] % 7 == 1:
                rotated = True
                break
        if rotated:
            print('No')
        else:
            print('Yes')
    else:
        print('No')
