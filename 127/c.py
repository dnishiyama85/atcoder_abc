import numpy as np

n, m = map(int, input().strip().split())
data = [map(int, input().strip().split()) for _ in range(m)]

left = np.zeros(n + 1, dtype=np.int32)
right = np.zeros(n + 1, dtype=np.int32)

for l, r in data:
    left[l] += 1
    right[r] += 1

card = 0
count = 0
for i in range(n + 1):
    count += left[i]
    if count == m:
        card += 1
    count -= right[i]

print(card)
