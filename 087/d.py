import numpy as np

n, m = list(map(int, input().split()))
# data = []
# for i in range(m):
#     l, r, d = list(map(int, input().split()))
#     row = [0] * (n + 1)
#     row[l - 1] = -1
#     row[r - 1] = 1
#     row[-1] = d
#     data.append(row)
data = np.zeros


if m == 0:
    print('Yes')
else:
    extended = np.array(data, dtype='int64')

    #print(extended)

    coeffs = extended[:,0:2]

    r_ex = np.linalg.matrix_rank(extended)
    r_cf = np.linalg.matrix_rank(coeffs)

    #print("r_ex = {}".format(r_ex))
    print("r_cf = {}".format(r_cf))

    print('Yes' if r_ex == r_cf else 'No')
