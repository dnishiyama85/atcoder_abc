import numpy as np

n, k = map(int, input().strip().split())
ss = [input().strip() for _ in range(n)]

counts = np.zeros((n, 26), dtype=int)

int_a = ord('a')
for i, s in enumerate(ss):
    for c in list(s):
        counts[i][ord(c) - int_a] = 1

ans = 0
# 全探索
for num in range(1, 2**n):
    bits = np.zeros(n, dtype=bool)
    b = 0
    while num > 0:
        bits[b] = num % 2
        num //= 2
        b += 1

    # print(bits)
    counts_of_chosen = np.sum(counts[bits], axis=0)
    #print(kinds)
    ans = max(ans, np.count_nonzero(counts_of_chosen == k))

print(ans)
