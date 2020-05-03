import numpy as np
n, m, c = map(int, input().strip().split())
bs = np.array(list(map(int, input().strip().split())))
as_ = np.array([list(map(int, input().strip().split())) for _ in range(n)])

result = np.dot(as_, bs) + c
counts = np.ones_like(result)
ans = np.sum(counts[result > 0])

print(ans)
