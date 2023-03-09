import numpy as np

h, w = map(int, input().strip().split())
ss = []
for _ in range(h):
    s = input().strip()
    ss.append([0 if c == '.' else 1 for c in list(s)])
np_ss = np.array(ss)

ts = []
for _ in range(h):
    t = input().strip()
    ts.append([0 if c == '.' else 1 for c in list(t)])
np_ts = np.array(ts)

sorted_ss = np.sort(np_ss, axis=1)
sorted_ts = np.sort(np_ts, axis=1)

if np.all(sorted_ss == sorted_ts):
    print('Yes')
else:
    print('No')
