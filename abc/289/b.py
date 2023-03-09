n, m = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))

for i, a in enumerate(as_):
    as_[i] = a - 1

as_ = set(as_)

components = []
i = 0
comp = [i]
while i < n:
    if i in as_:
        i += 1
        comp.append(i)
    else:
        components.append(comp)
        i += 1
        comp = [i]

for comp in components:
    comp = sorted(comp, reverse=True)
    for c in comp:
        print(c + 1)


