a, b = map(int, input().strip().split())

sa = ''.join([str(a) for _ in range(b)])
sb = ''.join([str(b) for _ in range(a)])

ss = sorted([sa, sb])
print(ss[0])
