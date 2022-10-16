n, k = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))
bs = list(map(int, input().strip().split()))

max_oishii = max(as_)
max_oishii_as_idx = []
for i, a in enumerate(as_):
    if a == max_oishii:
        max_oishii_as_idx.append(i + 1)

possible = False
for b in bs:
    if b in max_oishii_as_idx:
        possible = True
        break

print('Yes') if possible else print('No')
