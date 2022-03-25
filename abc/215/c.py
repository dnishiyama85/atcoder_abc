import itertools

s, k = input().strip().split()
k = int(k)
ss = list(s)

all = list(itertools.permutations(ss))
all = list(set([''.join(s) for s in all]))
all = (sorted(all))
print(all[k - 1])
