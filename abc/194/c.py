import numpy as np
N = int(input())
A = list(map(int, input().strip().split()))
A = np.array(A)

D = np.arange(1, N)
cumA = np.cumsum(A)
cumA2 = np.cumsum(A ** 2)

ans = np.sum(D * A[1:] ** 2) + np.sum(cumA2[:-1]) - 2 * np.sum(A[1:] * cumA[:-1])
print(ans)
