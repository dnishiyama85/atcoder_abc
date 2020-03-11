n, k = map(int, input().strip().split())
hs = map(int, input().strip().split())
hs = list(sorted(hs, reverse=True))

n_attack = sum(hs[k:]) if k < n else 0
print(n_attack)
