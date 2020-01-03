import numpy as np

s = list(map(int, input().strip()))
s = np.array(s, dtype=np.bool)
len_s = len(s)

p = 0
count = 0

while p < len_s - 1:
    if s[p] != s[p + 1]:
        count += 2
        if p < len_s - 2:
            s[p:-2] = s[p + 2:]
        if p > 0:
            p -= 1
        else:
            p = 0

        len_s -= 2
    else:
        p += 1

print(count)
