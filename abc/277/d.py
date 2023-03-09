import numpy as np
from collections import defaultdict

n, m = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))
group = defaultdict(int)

for a in as_:
    group[a % m] += 1



min_as = np.min(as_)

if min_as > 0:
