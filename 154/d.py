import numpy as np

n, k = map(int, input().strip().split())
ps = list(map(int, input().strip().split()))

expects = np.array([(p + 1) / 2 for p in ps])
partial_sum = np.sum(expects[:k])
mx = partial_sum

for i in range(1, n - k + 1):
    partial_sum = partial_sum - expects[i - 1] + expects[i + k - 1]
    mx = max(partial_sum, mx)

print(mx)
