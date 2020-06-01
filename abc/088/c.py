import numpy as np

v = []
for i in range(3):
    v.extend(input().split())

v = np.array([int(x) for x in v])



coeffs = np.array([
    [1, 0, 0, 1, 0, 0, v[0]],
    [1, 0, 0, 0, 1, 0, v[1]],
    [1, 0, 0, 0, 0, 1, v[2]],
    [0, 1, 0, 1, 0, 0, v[3]],
    [0, 1, 0, 0, 1, 0, v[4]],
    [0, 1, 0, 0, 0, 1, v[5]],
    [0, 0, 1, 1, 0, 0, v[6]],
    [0, 0, 1, 0, 1, 0, v[7]],
    [0, 0, 1, 0, 0, 1, v[8]],
])

rank = np.linalg.matrix_rank(coeffs)
if rank < 6:
    print("Yes")
else:
    print("No")
