import numpy as np

n, m = map(int, input().strip().split())
as_ = list(reversed(list(map(int, input().strip().split()))))
cs = list(reversed(list(map(int, input().strip().split()))))

as_ = np.array(as_, dtype=np.int)
cs = np.array(cs, dtype=np.int)

div = np.polydiv(cs, as_)
q = reversed(div[0].astype(np.int).tolist())
print(' '.join(map(str, q)))
