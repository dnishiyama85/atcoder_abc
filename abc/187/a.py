a, b = list(input().strip().split())
sa = sum([int(d) for d in a])
sb = sum([int(d) for d in b])

if sa >= sb:
    print(sa)
else:
    print(sb)
