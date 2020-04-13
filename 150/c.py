import itertools

n = int(input())
ps = list(map(int, input().strip().split()))
qs = list(map(int, input().strip().split()))

perms = itertools.permutations(range(1, n + 1))

for idx, perm in enumerate(perms):
    perm_l = list(perm)
    if ps == perm_l:
        a = idx + 1
    if qs == perm_l:
        b = idx + 1

print(abs(a - b))
