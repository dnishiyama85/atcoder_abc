a, b = map(int, input().strip().split())
if any([s % 3 == 0 for s in [a, b, a + b]]):
    print('Possible')
else:
    print('Impossible')
