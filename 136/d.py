import numpy as np

s = input().strip()

mode = 'R'
start = 0
counts = np.zeros(len(s), dtype=np.int)
for i in range(1, len(s)):
    if mode == 'R':
        if s[i] == 'R':
            pass
        elif s[i] == 'L':
            counts[i - 1] += (i - start + 1) // 2
            counts[i] += (i - start) // 2
            mode = 'L'
            start = i
    if mode == 'L':
        if i == len(s) - 1:
            counts[start - 1] += (i - start + 1) // 2
            counts[start] += (i - start + 2) // 2
        elif s[i] == 'L':
            pass
        elif s[i] == 'R':
            counts[start - 1] += (i - start) // 2
            counts[start] += (i - start + 1) // 2
            mode = 'R'
            start = i

print(' '.join(map(str, counts.tolist())))
